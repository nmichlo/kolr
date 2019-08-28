
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


from kolr.util.util import SingletonMeta
import sys


# ========================================================================= #
# BASE                                                                      #
# ========================================================================= #


class ITermOutput(object, metaclass=SingletonMeta):
    def set_cursor_hidden(self, enable): raise NotImplementedError()
    def set_alternate_buffer(self, enable): raise NotImplementedError()
    def set_mouse_support(self, enable): raise NotImplementedError()
    def set_bracket_paste(self, enable): raise NotImplementedError()
    def set_auto_wrap(self, enable): raise NotImplementedError()
    def reset(self): raise NotImplementedError()

    def clear(self): raise NotImplementedError()
    def write_unsafe(self, string): raise NotImplementedError()
    def write(self, string): raise NotImplementedError()
    def flush(self): raise NotImplementedError()

    def cursor_goto(self, x, y): raise NotImplementedError()
    def get_size(self): raise NotImplementedError()


# ========================================================================= #
# UNIX                                                                      #
# ========================================================================= #


def _create_unix():
    """
    https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
    http://code.activestate.com/recipes/134892
    http://man7.org/linux/man-pages/man3/termios.3.html
    """
    import os
    import kolr.term.escape_codes as ec


    class _Unix(ITermOutput):
        def set_cursor_hidden(self, enable):
            self.write_unsafe(ec.csi.decset.DECTCEM if enable else ec.csi.decrst.DECTCEM)
        def set_alternate_buffer(self, enable):
            self.write_unsafe(ec.csi.decset.RESOURCE_SAVE_CURSOR_ALT_BUFFER if enable else ec.csi.decrst.RESOURCE_SAVE_CURSOR_ALT_BUFFER)
        def set_mouse_support(self, enable):
            self.write_unsafe(ec.csi.decset.MOUSE_EVENTS_X10 if enable else ec.csi.decrst.MOUSE_EVENTS_X10)
            self.write_unsafe(ec.csi.decset.MOUSE_EVENTS_X11 if enable else ec.csi.decrst.MOUSE_EVENTS_X11)
            self.write_unsafe(ec.csi.decset.MOUSE_MODE_URXVT if enable else ec.csi.decrst.MOUSE_MODE_URXVT)
            self.write_unsafe(ec.csi.decset.MOUSE_MODE_SGR if enable else ec.csi.decrst.MOUSE_MODE_SGR)
        def set_bracket_paste(self, enable):
            self.write_unsafe(ec.csi.decset.BRACKET_PASTE if enable else ec.csi.decrst.BRACKET_PASTE)
        def set_auto_wrap(self, enable):
            self.write_unsafe(ec.csi.decset.DECAWM if enable else ec.csi.decrst.DECAWM)
        def reset(self):
            self.write_unsafe(ec.esc.RIS)

        def clear(self):
            self.write_unsafe(ec.csi.ed.ERASE_SAVED)
            self.write_unsafe(ec.csi.ed.ERASE_ALL)
        def write_unsafe(self, string):
            sys.stdout.write(string)
        def write(self, string):
            self.write_unsafe(string.replace(ec.esc.ESC, '§'))
        def flush(self):
            sys.stdout.flush()

        def cursor_goto(self, x, y):
            self.write_unsafe(ec.csi.cup(y+1, x+1))
        def get_size(self):
            x, y = os.get_terminal_size()
            return x, y

    return _Unix

# ========================================================================= #
# WINDOWS                                                                   #
# ========================================================================= #


def _create_windows():
    import msvcrt

    class _Windows(ITermOutput):
        pass

    raise NotImplementedError('Windows is unsupported')

    return _Windows


# ========================================================================= #
# INTERFACE                                                                 #
# ========================================================================= #


if sys.platform in ('win32', 'cygwin'):
    TermOutput = _create_windows()
else:
    TermOutput = _create_unix()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


