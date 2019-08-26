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


from kolr.term.controller import TerminalController, EVENT_RESIZE, EVENT_KEY, EVENT_RENDER, EVENT_MOUSE


if __name__ == '__main__':

    p, k, (w, h), (x, y) = None, None, (None, None), (None, None)

    screen = TerminalController(frame_rate=10)

    @screen.on(EVENT_KEY)
    def key_callback(key):
        global k
        if key == 27:
            screen.stop()
        k = key

    @screen.on(EVENT_RESIZE)
    def render_callback(_w, _h):
        global w, h
        w = _w
        h = _h

    @screen.on(EVENT_MOUSE)
    def render_callback(event):
        global x, y
        x = event

    @screen.on(EVENT_RENDER)
    def render_callback(delta):
        screen.clear()
        screen.write_str(f'key: {k}', y=0)
        screen.write_str(f'x: {x} y: {y}', y=1)
        screen.write_str(f'w: {w} h: {h}', y=2)
        screen.write_str(f'delta: {delta}', y=3)
        if p:
            screen.write_str(f'pressed: {p}', y=5)
        screen.flush()

    @screen.kb('<any>')
    def _(event):
        global p
        p = event

    @screen.kb('c-c')
    def _(event):
        screen.stop()

    screen.start()
