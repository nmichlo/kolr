
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


class ITermInput(object, metaclass=SingletonMeta):
    def set_raw_mode(self, enable): raise NotImplementedError()

    def get_char(self): raise NotImplementedError()
    def has_char(self): raise NotImplementedError()

    def get_size(self): raise NotImplementedError()


class ITermOutput(object, metaclass=SingletonMeta):
    def set_cursor_hidden(self, enable): raise NotImplementedError()
    def set_alternate_buffer(self, enable): raise NotImplementedError()
    def set_mouse_support(self, enable): raise NotImplementedError()
    def set_bracket_paste(self, enable): raise NotImplementedError()
    def set_auto_wrap(self, enable): raise NotImplementedError()

    def clear(self): raise NotImplementedError()

    def cursor_goto(self, x, y): raise NotImplementedError()

    def write_unsafe(self, string): raise NotImplementedError()
    def write(self, string): raise NotImplementedError()

    def flush(self): raise NotImplementedError()


# ========================================================================= #
# PromptToolkit                                                             #
# ========================================================================= #


# TODO: REMOVE prompt_toolkit DEPENDENCY
class _TermInputPromptToolkit(ITermInput):
    def __init__(self, term_input):
        self._input = term_input
        self._raw_input_control = None
        self._key_buffer = []

    def set_raw_mode(self, enable):
        self._input.raw_mode().__enter__() if enable else self._input.raw_mode().__exit__()

    def get_char(self):
        if self.has_char():
            char = self._key_buffer[0]
            self._key_buffer = self._key_buffer[1:]
            return char  # KeyPress
        return None

    def has_char(self):
        chars = self._input.read_keys()  # List[KeyPress]
        self._key_buffer.extend(chars)
        return len(self._key_buffer) > 0

    def get_size(self):
        size = self._output.get_size()
        w, h = (size.columns, size.rows)
        return w, h


# TODO: REMOVE prompt_toolkit DEPENDENCY
class _TerminalOutputPromptToolkit(ITermOutput):
    def __init__(self, term_output):
        self._output = term_output

    def set_cursor_hidden(self, enable):
        self._output.hide_cursor() if enable else self._output.show_cursor()
    def set_alternate_buffer(self, enable):
        self._output.enter_alternate_screen() if enable else self._output.quit_alternate_screen()
    def set_mouse_support(self, enable):
        self._output.enable_mouse_support() if enable else self._output.disable_mouse_support()
    def set_bracket_paste(self, enable):
        self._output.enable_bracketed_paste() if enable else self._output.disable_bracketed_paste()
    def set_auto_wrap(self, enable):
        self._output.enable_autowrap() if enable else self._output.disable_autowrap()

    def clear(self):
        self._output.erase_screen()
    def cursor_goto(self, x, y):
        self._output.cursor_goto(y + 1, x + 1)

    def write_unsafe(self, string):
        self._output.write_raw(string)
    def write(self, string):
        self._output.write(string)

    def flush(self):
        self._output.flush()


# ========================================================================= #
# UNIX                                                                      #
# ========================================================================= #


def _create_interfaces_unix():
    """
    https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
    http://code.activestate.com/recipes/134892
    http://man7.org/linux/man-pages/man3/termios.3.html
    """

    import os
    import tty
    import termios
    import select
    import kolr.term.escape_codes as ec

    class TermInputUnix(ITermInput):
        def __init__(self):
            self._old_term_settings = None

        def set_raw_mode(self, enable):
            if enable:
                assert self._old_term_settings is None
                # INIT
                self._old_term_settings = termios.tcgetattr(sys.stdin)
                tty.setraw(sys.stdin)       # Captures ctrl-c and more
                # tty.setcbreak(sys.stdin)  # Responds to ctrl-c
            else:
                assert self._old_term_settings is not None
                # RESET
                termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self._old_term_settings)
                self._old_term_settings = None

        def get_char(self):
            if self.has_char():
                return sys.stdin.read(1)
            return None

        def has_char(self):
            # rlist: wait for reading | wlist: wait for writing | xlist: wait ``exceptional condition''
            rlist, wlist, xlist = select.select([sys.stdin], [], [], 0)
            return rlist != []

        def get_size(self):
            x, y = os.get_terminal_size()
            return x, y

    class TermOutputUnix(ITermOutput):
        def set_cursor_hidden(self, enable):
            self.write_unsafe(ec.csi.CH if enable else ec.csi.CS)

        def set_alternate_buffer(self, enable):
            self.write_unsafe(ec.csi.SBE if enable else ec.csi.SBD)

        def set_mouse_support(self, enable):
            # TODO: add mouse support
            pass

        def set_bracket_paste(self, enable):
            self.write_unsafe(ec.csi.BPE if enable else ec.csi.BPD)

        def set_auto_wrap(self, enable):
            self.write_unsafe(ec.csi.BPE if enable else ec.csi.BPD)

        def clear(self):
            self.write_unsafe(ec.csi.ed(2))

        def cursor_goto(self, x, y):
            self.write_unsafe(ec.csi.cup(y+1, x+1))

        def write_unsafe(self, string):
            sys.stdout.write(string)

        def write(self, string):
            self.write_unsafe(string.replace(ec.esc.ESC, '§'))

        def flush(self):
            sys.stdout.flush()

    return TermInputUnix, TermOutputUnix


# TODO: REMOVE prompt_toolkit DEPENDENCY
def _create_interfaces_unix_prompt_toolkit():
    from prompt_toolkit.input.vt100 import Vt100Input
    from prompt_toolkit.output.vt100 import Vt100_Output
    from prompt_toolkit.layout.screen import Size
    import os

    class TermInputUnixPromptToolkit(_TermInputPromptToolkit):
        def __init__(self):
            super().__init__(Vt100Input(sys.stdin))
            self._old_term_settings = None

    class TermOutputUnixPromptToolkit(_TerminalOutputPromptToolkit):
        def __init__(self):
                super().__init__(Vt100_Output(sys.stdout, TermOutputUnixPromptToolkit.get_size))

        @staticmethod
        def get_size():
            columns, rows = os.get_terminal_size()
            return Size(rows, columns)

    return TermInputUnixPromptToolkit, TermOutputUnixPromptToolkit

# ========================================================================= #
# WINDOWS                                                                   #
# ========================================================================= #


# def _create_interfaces_windows():
#     import msvcrt
#
#     class TerminalInterfaceWindows(ITerminalInterface):
#         def get_char(self):
#             return msvcrt.getch().decode('mbcs')
#
#         def has_char(self):
#             return msvcrt.kbhit()
#
#     return TerminalInterfaceWindows


# TODO: REMOVE prompt_toolkit DEPENDENCY
def _create_interfaces_windows_prompt_toolkit():
    from prompt_toolkit.input.win32 import Win32Input
    from prompt_toolkit.output.win32 import Win32Output

    class TermInputWindows(_TermInputPromptToolkit):
        def __init__(self):
            super().__init__(Win32Input(sys.stdin))

    class TermOutputWindows(_TerminalOutputPromptToolkit):
        def __init__(self):
            super().__init__(Win32Output(sys.stdout))

    return TermInputWindows, TermOutputWindows


# ========================================================================= #
# INTERFACE                                                                 #
# ========================================================================= #


if sys.platform in ('win32', 'cygwin'):
    TermInput, TermOutput = _create_interfaces_windows_prompt_toolkit()
else:
    TermInput, TermOutput = _create_interfaces_unix_prompt_toolkit()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


