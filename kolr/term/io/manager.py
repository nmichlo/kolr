
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


from kolr.term.io.input import TermInput
from kolr.term.io.key_proc import KeyProc
from kolr.term.io.output import TermOutput
from kolr.util.events import Emitter
from kolr.util.loop import UpdateRenderLoop
import atexit


# ========================================================================= #
# TERMINAL CONTROLLER                                                       #
# ========================================================================= #


EVENT_RESIZE = 'resize'
EVENT_MOUSE = 'mouse'
EVENT_KEY = 'key'

EVENT_APP_START = 'app_start'
EVENT_APP_END = 'app_end'

EVENT_RENDER = 'render'
EVENT_UPDATE = 'update'


class TermManager(object):

    def __init__(self, frame_rate=5, tick_rate=2):
        super().__init__()

        # INIT: event manager
        self._emitter = Emitter([EVENT_RESIZE, EVENT_MOUSE, EVENT_KEY, EVENT_APP_START, EVENT_APP_END, EVENT_RENDER, EVENT_UPDATE])

        # INIT: terminal interface
        self._term_size = (None, None)
        self._term_input = TermInput()
        self._term_output = TermOutput()

        # INIT: game loop
        self._loop = UpdateRenderLoop(
            frame_rate=frame_rate,
            tick_rate=tick_rate,
            max_frame_skip=-1,
            on_start=self._on_start,
            on_loop_event=self._on_loop_event,
            on_loop_update=self._emitter.emit_func(EVENT_UPDATE),
            on_loop_render=self._on_loop_render,
            on_end=self._on_end,
        )

        # EXTEND: UpdateRenderLoop
        self.start = self._loop.start
        self.stop = self._loop.stop

        # EXTEND: Emitter
        self.on = self._emitter.on
        self.off = self._emitter.off

        # EXTEND: TerminalInterface
        self.clear = self._term_output.clear
        self.cursor_goto = self._term_output.cursor_goto

        # Keys
        self._key_proc = KeyProc()
        self._key_emitter = Emitter()

        # EXTEND: Emitter (Key Bindings)
        self.on_key = self._key_emitter.on
        self.off_key = self._key_emitter.off

    # - - - - - - - - - - - - - - - INTERFACE - - - - - - - - - - - - - - - #

    def write(self, string, x=None, y=None, unsafe=False):
        if x is not None or y is not None:
            self.cursor_goto(x or 0, y or 0)
        if unsafe:
            self._term_output.write(string)
        else:
            self._term_output.write_unsafe(string)

    def print(self, *strings, x=None, y=None, unsafe=False):
        self.write(''.join(str(s) for s in strings), x=x, y=y, unsafe=unsafe)

    # - - - - - - - - - - - - - - - TERMINALS - - - - - - - - - - - - - - - #

    def _set_term_defaults(self, enable):
        # INPUT
        self._term_input.set_raw_mode(enable)
        # OUTPUT
        self._term_output.set_alternate_buffer(enable)
        self._term_output.set_mouse_support(enable)
        self._term_output.set_bracket_paste(enable)
        self._term_output.set_auto_wrap(not enable)

    def _initialise(self):
        self._set_term_defaults(True)
        self._term_output.flush()

    def _finalise(self):
        self._set_term_defaults(False)
        self._term_output.flush()

    def _exit_finalise(self):
        self._finalise()
        print("Encountered Unknown Error")

    # - - - - - - - - - - - - - - - - EVENT - - - - - - - - - - - - - - - - #

    def _do_size_polling(self):
        # continuously poll for updates
        size = self._term_output.get_size()
        if size != self._term_size:
            self._term_size = size
            self._emitter.emit(EVENT_RESIZE, size[0], size[1])  # w, h

    def _do_character_polling(self):
        # Read from input stream
        while self._term_input.has_chars():
            chars = self._term_input.get_chars()
            self._key_proc.push_chars(chars)
        # process raw characters into keys
        for key in self._key_proc.pop_keys():
            self._emitter.emit(EVENT_KEY, key)  # TODO: remove, or move key_processing elsewhere?
            self._key_emitter.emit('any', key)
            self._key_emitter.emit(key.name, key)

    # - - - - - - - - - - - - - - - -LOOPING- - - - - - - - - - - - - - - - #

    def _on_start(self):
        self._set_term_defaults(True)
        atexit.register(self._exit_finalise)
        self._emitter.emit(EVENT_APP_START)

    def _on_loop_event(self):
        self._do_size_polling()
        self._do_character_polling()

    def _on_loop_render(self, delta):
        self._emitter.emit(EVENT_RENDER, delta)
        self._term_output.flush()

    def _on_end(self):
        atexit.unregister(self._exit_finalise)
        self._finalise()
        self._emitter.emit(EVENT_APP_END)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
