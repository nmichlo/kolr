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
from abc import ABCMeta, abstractmethod
from typing import Callable, Optional


class UpdateRenderLoop(object):

    def __init__(
            self,
            frame_rate: float = 10,
            tick_rate: float = 5,
            max_frame_skip: int = 0,
            # Callbacks
            on_start: Optional[Callable[[], None]] = None,

            on_loop_event: Optional[Callable[[], None]] = None,
            on_loop_update: Optional[Callable[[], None]] = None,
            on_loop_render: Optional[Callable[[float], None]] = None,

            on_end: Optional[Callable[[None], None]] = None,
    ):
        # params
        max_frame_skip = float('inf') if max_frame_skip < 0 else max_frame_skip
        self._frame_time = 1 / frame_rate if frame_rate > 0 else float('inf')
        self._tick_time = 1 / tick_rate if tick_rate > 0 else float('inf')
        self._max_frame_skip = max_frame_skip
        self._running = False
        # callbacks
        self._on_start = on_start
        self._on_loop_event = on_loop_event
        self._on_loop_update = on_loop_update
        self._on_loop_render = on_loop_render
        self._on_end = on_end

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
        """
        Based on:
          - https://gist.github.com/mariobadr/673bbd5545242fcf9482
          - http://gameprogrammingpatterns.com/game-loop.html
          - https://dewitters.com/dewitters-gameloop/
        TODO: http://bitsquid.blogspot.com/2010/10/time-step-smoothing.html
        TODO: http://gamasutra.com/view/feature/130247/multithreaded_game_engine_.php
        """

        assert not self._running

        if self._on_start:
            self._on_start()

        self._running = True
        ave_time, sleep, lag, last_time = 0, 0, 0, time.time()

        while self._running:
            t = time.time()
            diff, last_time = t - last_time, t
            # EVENTS
            if self._on_loop_event:
                self._on_loop_event()
            # UPDATE
            if self._on_loop_update:
                lag += diff
                skipped_frames = 0
                while lag >= self._tick_time and skipped_frames <= self._max_frame_skip:
                    skipped_frames += 1
                    lag -= self._tick_time
                    self._on_loop_update()
            # RENDER
            if self._on_loop_render:
                self._on_loop_render(lag / self._tick_time)
            # RENDER SLEEP
            ave_time = (ave_time + diff) / 2
            sleep_error, last_proc_time = ave_time - self._frame_time, diff - sleep
            sleep = max((self._frame_time - last_proc_time) - sleep_error, 0)
            if sleep > 0:
                time.sleep(sleep)

        if self._on_end:
            self._on_end()
