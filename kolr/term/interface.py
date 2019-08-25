
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


import sys
from typing import Type


# ========================================================================= #
# BASE                                                                      #
# ========================================================================= #


class ITerminalInterface(object):
    def init_term(self):
        pass
    def reset_term(self):
        pass
    def get_char(self):
        raise NotImplementedError('Override Me')
    def has_char(self):
        raise NotImplementedError('Override Me')


# ========================================================================= #
# WINDOWS                                                                   #
# ========================================================================= #


def _create_interface_windows():
    import msvcrt

    class TerminalInterfaceWindows(ITerminalInterface):
        def get_char(self):
            return msvcrt.getch().decode('mbcs')

        def has_char(self):
            return msvcrt.kbhit()

    return TerminalInterfaceWindows


# ========================================================================= #
# UNIX                                                                      #
# ========================================================================= #


def _create_interface_unix():
    from select import select
    import sys
    import termios
    import tty

    class TerminalInterfaceUnix(ITerminalInterface):
        """
        https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
        http://code.activestate.com/recipes/134892
        http://man7.org/linux/man-pages/man3/termios.3.html
        """

        def __init__(self):
            self._old_term_settings = None

        def init_term(self):
            # Save the terminal settings
            self._old_term_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdin)  # Responds to ctrl-c
            # tty.setraw(sys.stdin)   # Captures ctrl-c and more

        def reset_term(self):
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self._old_term_settings)
            self._old_term_settings = None

        def get_char(self):
            return sys.stdin.read(1)

        def has_char(self):
            # rlist: wait for reading | wlist: wait for writing | xlist: wait ``exceptional condition''
            rlist, wlist, xlist = select([sys.stdin], [], [], 0)
            return rlist != []

    return TerminalInterfaceUnix


# ========================================================================= #
# INTERFACE                                                                 #
# ========================================================================= #


if sys.platform in ('win32', 'cygwin'):
    TerminalInterface: Type[ITerminalInterface] = _create_interface_windows()
    raise Exception('Windows is not yet supported')
else:
    TerminalInterface: Type[ITerminalInterface] = _create_interface_unix()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
