
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
from kolr.term.interface import TerminalInterface
from kolr.util.events import Emitter
from kolr.term import escape_codes as ec
from kolr.util.loop import RenderLoop
from sys import stdout, stdin, stderr
import readchar
import os
import atexit


# ========================================================================= #
# TERMINAL CONTROLLER                                                       #
# ========================================================================= #


EVENT_RESIZE = 'resize'
EVENT_MOUSE = 'mouse'
EVENT_KEY = 'key'
EVENT_RENDER = 'render'
EVENT_UPDATE = 'update'


class TerminalController(RenderLoop):

    def __init__(self, frame_rate=10, tick_rate=0):
        super().__init__(frame_rate=frame_rate, tick_rate=tick_rate, max_frame_skip=-1)
        # callbacks TODO: replace with event manager
        self._emitter = Emitter([EVENT_RESIZE, EVENT_MOUSE, EVENT_KEY, EVENT_RENDER])
        # loop vars
        self._term_size = (None, None)
        self._term_interface = TerminalInterface()

    # - - - - - - - - - - - - - - - - EVENT - - - - - - - - - - - - - - - - #

    def on(self, key, observer=None):
        return self._emitter.on(key, observer)

    def off(self, key, observer):
        return self._emitter.off(key, observer)

    # - - - - - - - - - - - - - - - -NCURSES- - - - - - - - - - - - - - - - #

    def _initialise(self):
        # Raw Input
        self._term_interface.init_term()
        # CSI Params
        # stdout.write(ec.csi.CH)   # Cursor        : Hide
        # stdout.write(ec.csi.BPE)  # Bracket Paste : Enable
        # stdout.write(ec.csi.SBE)  # Screen Buffer : Enable
        # stdout.flush()

    def _finalise(self):
        # CSI Params
        # stdout.write(ec.csi.SBD)  # Screen Buffer : Disable
        # stdout.write(ec.csi.BPD)  # Bracket Paste : Disable
        # stdout.write(ec.csi.CS)   # Cursor        : Show
        # stdout.flush()
        # Raw Input
        self._term_interface.reset_term()

    def _exit_finalise(self):
        self._finalise()
        print("Encountered Unknown Error")

    # - - - - - - - - - - - - - - - -LOOPING- - - - - - - - - - - - - - - - #

    def _on_loop_start(self):
        self._initialise()
        atexit.register(self._exit_finalise)

    def _on_loop_event(self) -> bool:
        self._process_events()
        return True

    def _process_events(self):
        # TERMINAL SIZE
        term_size = os.get_terminal_size()
        if term_size != self._term_size:
            self._term_size = term_size
            self._emitter.emit(EVENT_RESIZE, term_size[0], term_size[1])  # w, h
        # KEY PRESSES
        while self._term_interface.has_char():
            self._emitter.emit(EVENT_KEY, readchar.readkey(self._term_interface.get_char))
        # MOUSE PRESSES
        pass
        # CONTINUE RUNNING
        return True

    def _on_loop_update(self):
        self._process_events()
        self._emitter.emit(EVENT_UPDATE)

    def _on_loop_render(self, delta):
        self._emitter.emit(EVENT_RENDER, delta)

    def _on_loop_end(self):
        atexit.unregister(self._exit_finalise)
        self._finalise()

    # - - - - - - - - - - - - - - - INTERFACE - - - - - - - - - - - - - - - #

    def clear(self):
        stdout.write(ec.csi.ed(2))

    def write_str(self, string, x=0, y=0):
        stdout.write(ec.csi.cup(y + 1, x + 1))
        stdout.write(string)

    def write_char(self, char, x=0, y=0):
        assert len(char) == 1
        self.write_str(char, x + 1, y + 1)

    def flush(self):
        stdout.flush()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
