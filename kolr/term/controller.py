
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
import traceback


from kolr.term.interface import TermInput, TermOutput
from kolr.util.events import Emitter
from kolr.util.loop import RenderLoop
import atexit

# TODO: REMOVE prompt_toolkit DEPENDENCY
import prompt_toolkit.key_binding
import prompt_toolkit.key_binding.key_processor
from prompt_toolkit.keys import Keys


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


class TerminalController(object):

    def __init__(self, frame_rate=5, tick_rate=2):
        super().__init__()

        # INIT: event manager
        self._emitter = Emitter([EVENT_APP_START, EVENT_APP_END, EVENT_RESIZE, EVENT_MOUSE, EVENT_KEY, EVENT_RENDER, EVENT_UPDATE])

        # INIT: terminal interface
        self._term_size = (None, None)
        self._term_input = TermInput()
        self._term_output = TermOutput()

        # INIT: game loop
        self._loop = RenderLoop(
            frame_rate=frame_rate,
            tick_rate=tick_rate,
            max_frame_skip=-1,
            on_loop_start=self._on_loop_start,
            on_loop_event=self._on_loop_event,
            on_loop_update=self._emitter.emit_func(EVENT_UPDATE),
            on_loop_render=self._emitter.emit_func(EVENT_RENDER),
            on_loop_end=self._on_loop_end,
        )

        # EXTEND: RenderLoop
        self.start = self._loop.start
        self.stop = self._loop.stop

        # EXTEND: Emitter
        self.on = self._emitter.on
        self.off = self._emitter.off

        # EXTEND: TerminalInterface
        self.clear = self._term_output.clear
        self.cursor_goto = self._term_output.cursor_goto
        self.flush = self._term_output.flush

        # TODO: REMOVE prompt_toolkit DEPENDENCY
        self._key_bindings = prompt_toolkit.key_binding.KeyBindings()
        self._key_processor = prompt_toolkit.key_binding.key_processor.KeyProcessor(self._key_bindings)

        # EXTEND: KeyBindings
        self.kb = lambda key, *keys: self._key_bindings.add(key, *keys)
        self.kb_add = lambda key, *keys, func=None: self._key_bindings.add(key, *keys) if func is None else self._key_bindings.add(key, *keys)(func)
        self.kb_del = lambda *func_or_keys: self._key_bindings.remove(*func_or_keys)

    # - - - - - - - - - - - - - - - INTERFACE - - - - - - - - - - - - - - - #

    def write_str(self, string, x=None, y=None):
        if x is not None or y is not None:
            self.cursor_goto(x or 0, y or 0)
        self._term_output.write(string)

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

    # def _handle_key_event(self, char):
    #     if char.key == 'c-c' or char.key == 'escape':
    #         return False
    #     else:
    #         self._emitter.emit(EVENT_KEY, (char.key, char.data))
    #
    # def _handle_mouse_event(self, char):
    #     try:
    #         code, x, y = char.data[3:-1].split(';')
    #         action = None
    #         if code == '0':
    #             action = 'click-press' if (char.data[-1] == 'M') else 'click-release'
    #         elif code == '65':
    #             action = 'scroll-down'
    #         elif code == '64':
    #             action = 'scroll-up'
    #         self._emitter.emit(EVENT_MOUSE, (int(x), int(y), action))
    #     except Exception as e:
    #         traceback.print_exc()
    #         sys.stderr.write('An unexpected error occurred! {}'.format(e))
    #         sys.stderr.flush()

    def _do_character_polling(self):
        # while self._term_input.has_char():
        #     char = self._term_input.get_char()
        #     self._emitter.emit(EVENT_KEY, char)

        while self._term_input.has_char():
            char = self._term_input.get_char()
            self._key_processor.feed(char)
            self._emitter.emit(EVENT_KEY, char.data)
            # if char.key in {Keys.Vt100MouseEvent, Keys.WindowsMouseEvent}:
            #     self._emitter.emit(EVENT_MOUSE, char.data)
            # else:
            #     self._emitter.emit(EVENT_KEY, (char.key, char.data))
        # self._key_processor.process_keys()

    def _do_size_polling(self):
        size = self._term_output.get_size()
        if size != self._term_size:
            self._term_size = size
            self._emitter.emit(EVENT_RESIZE, size[0], size[1])  # w, h

    # - - - - - - - - - - - - - - - -LOOPING- - - - - - - - - - - - - - - - #

    def _on_loop_start(self):
        self._set_term_defaults(True)
        atexit.register(self._exit_finalise)
        self._emitter.emit(EVENT_APP_START)

    def _on_loop_event(self):
        self._do_size_polling()
        self._do_character_polling()

    def _on_loop_end(self):
        atexit.unregister(self._exit_finalise)
        self._finalise()
        self._emitter.emit(EVENT_APP_END)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
