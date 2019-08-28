
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#  MIT License
#
#  Copyright (c) 2019 Nathan Juraj Michlo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
from prompt_toolkit.input.vt100_parser import Vt100Parser

from kolr.util.util import SingletonMeta
import sys


# ========================================================================= #
# BASE                                                                      #
# ========================================================================= #


class ITermInput(object, metaclass=SingletonMeta):
    def set_raw_mode(self, enable): raise NotImplementedError()

    def get_chars(self): raise NotImplementedError()
    def has_chars(self): raise NotImplementedError()


# ========================================================================= #
# UNIX                                                                      #
# ========================================================================= #


def _create_unix():
    """
    https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
    http://code.activestate.com/recipes/134892
    http://man7.org/linux/man-pages/man3/termios.3.html
    """
    import tty
    import termios
    import select
    import os
    from codecs import getincrementaldecoder

    class _Unix(ITermInput):
        def __init__(self):
            self._old_term_settings = None
            # self._key_buffer = deque()
            self._decoder = getincrementaldecoder('utf-8')()

        def set_raw_mode(self, enable):
            assert bool(self._old_term_settings is None) == bool(enable)
            if enable:
                self._old_term_settings = termios.tcgetattr(sys.stdin)
                tty.setraw(sys.stdin)       # Captures ctrl-c and more | tty.setcbreak(sys.stdin) # Responds to ctrl-c
            else:
                termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self._old_term_settings)
                self._old_term_settings = None

        # def get_chars(self):
        #     if self.has_chars():
        #         return self._key_buffer.popleft()  # KeyPress
        #     return None
        #
        # def has_chars(self):
        #     chars = self._input.read_keys()  # List[KeyPress]
        #     self._key_buffer.extend(chars)
        #     return len(self._key_buffer) > 0

        # def get_chars(self):
        #     if self.has_chars():
        #         return sys.stdin.read(1) # Buffered Read - Blocks if no data.
        #     return None

        def get_chars(self):
            data = os.read(sys.stdin.fileno(), 1024)  # Unbuffered Read - continues if no data.
            return self._decoder.decode(data)

        def has_chars(self):
            rlist, wlist, xlist = select.select([sys.stdin], [], [], 0)
            return rlist != []

    return _Unix

# ========================================================================= #
# WINDOWS                                                                   #
# ========================================================================= #


def _create_windows():
    import msvcrt

    class _Windows(ITermInput):
        pass

    raise NotImplementedError('Windows is unsupported')

    return _Windows


# ========================================================================= #
# INTERFACE                                                                 #
# ========================================================================= #


if sys.platform in ('win32', 'cygwin'):
    TermInput = _create_windows()
else:
    TermInput = _create_unix()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


