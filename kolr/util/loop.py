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
import time


class RenderLoop(object):

    def __init__(self, frame_rate=30):
        self._frame_time = 1 / frame_rate
        self._running = False

    def start(self):
        if self._running:
            return self
        self._run()
        return self

    def stop(self):
        if not self._running:
            return self
        self._running = False
        return self

    def _run(self):
        assert not self._running
        self._pre_loop()

        self._running, last_t = True, time.time_ns()
        while self._running:
            # update time
            t = time.time_ns()
            last_t, delta = t, (t - last_t) / 1_000_000_000
            # Update
            self._on_loop(delta)
            # update sleep
            sleep = self._frame_time - delta
            if sleep > 0:
                time.sleep(sleep)

        self._post_loop()

    def _pre_loop(self):
        raise NotImplementedError()

    def _on_loop(self, delta) -> bool:
        raise NotImplementedError()

    def _post_loop(self):
        raise NotImplementedError()
