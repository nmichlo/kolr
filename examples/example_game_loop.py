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
import matplotlib.pyplot as plt
from kolr.util.loop import RenderLoop


class Loop(RenderLoop):
    def __init__(self, runtime_ms=5000, *args, **kwargs):
        from collections import defaultdict
        super().__init__(*args, **kwargs)
        self._runtime_ms = runtime_ms
        self.update_count = 0
        self.render_count = 0
        self.start_time = None
        self.xs = defaultdict(list)
        self.ys = defaultdict(list)
        self.ys_id = {}

    def append(self, key):
        t = time.time() - self.start_time
        self.xs[key].append(t)
        # self.ys[key].append(self.ys_id.setdefault(key, len(self.ys_id)+1))
        self.ys[key].append(1)
        return t

    def _on_loop_start(self):
        self.start_time = time.time()
        self.append('start')

    def _on_loop_event(self) -> bool:
        t = self.append('event')
        if t*1000 > self._runtime_ms:
            return False
        return True

    def _on_loop_update(self):
        import random
        self.update_count += 1
        self.append('update')
        time.sleep(random.random() * 1/50)
        print(f'[U] fps: {self.render_count / (time.time() - self.start_time):.2f} tps: {self.update_count / (time.time() - self.start_time):.2f}')

    def _on_loop_render(self, delta):
        import random
        self.render_count += 1
        time.sleep(random.random() * 1/50)
        print(f'[R] fps: {self.render_count / (time.time() - self.start_time):.2f} tps: {self.update_count / (time.time() - self.start_time):.2f}')
        self.append('render')

    def _on_loop_end(self):
        self.append('end')

    def plot(self):
        p = lambda key, c: plt.scatter(self.xs[key], self.ys[key], c=c, label=key)
        p('event', '#3333ff')   # blue
        p('update', '#ee22ff')  # purple
        p('render', '#22bbee')  # cyan
        p('start', '#00ff00')   # green
        p('end', '#ff0000')     # red
        plt.legend()
        plt.show()


if __name__ == '__main__':
    Loop(runtime_ms=3000, frame_rate=3, tick_rate=2, max_frame_skip=-1).start().plot()

