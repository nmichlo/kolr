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


import stretched

from kolr.term.escape_codes.esc import ESC
from kolr.term.io.manager import TermManager, EVENT_RESIZE, EVENT_RENDER
from kolr.ui.buffer import DoubleBuffer
from kolr.ui.component import Component


# ========================================================================= #
# Window                                                                    #
# ========================================================================= #


class Window(Component):
    def __init__(self, frame_rate=10, tick_rate=5):
        super().__init__()
        # initialise
        self._manager = TermManager(frame_rate=frame_rate, tick_rate=tick_rate)

        # EXTENDS: TermManager
        self.on_key = self._manager.on_key
        self.off_key = self._manager.off_key

        # IMPLEMENTS: TermManager
        @self._manager.on(EVENT_RESIZE)
        def _recompute_on_resize_terminal(w, h):
            self.compute_layout(w, h)

        @self._manager.on(EVENT_RENDER)
        def _write_buffer_to_screen_on_resize(delta):
            self._manager.clear()
            self.repaint()
            for x, y in self._buffer.diffs():
                self._manager.write(self._buffer.get(x, y), x=x, y=y, unsafe=True)

    def start(self):
        self._manager.start()
        return self

    def stop(self):
        self._manager.stop()
        return self

    @property
    def is_root(self): return True


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
