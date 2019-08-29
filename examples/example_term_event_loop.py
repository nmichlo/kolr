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


from kolr.term.escape_codes import csi
from kolr.term.io.manager import TermManager, EVENT_RESIZE, EVENT_KEY, EVENT_RENDER, EVENT_MOUSE


if __name__ == '__main__':

    p, k, (w, h), (x, y) = None, None, (0, 0), (0, 0)
    presses = set()

    screen = TermManager(frame_rate=10)

    @screen.on(EVENT_KEY)
    def key_callback(key):
        global k
        k = key.data

    @screen.on(EVENT_RESIZE)
    def render_callback(_w, _h):
        global w, h
        w = _w
        h = _h

    @screen.on(EVENT_MOUSE)
    def render_callback(event):
        global x, y
        x = event

    def get_ord(x):
        try:
            return ord(x)
        except:
            return None

    @screen.on(EVENT_RENDER)
    def render_callback(delta):
        screen.clear()
        for pos in presses:
            screen.print(csi.sgr.INVERT, ' ', csi.sgr.RESET, x=pos[0], y=pos[1])
        screen.write(f'key: {str(k)[:w-10]}',  y=0)
        screen.write(f'key ord: {get_ord(k)}', y=1)
        screen.write(f'x: {x} y: {y}',         y=2)
        screen.write(f'w: {w} h: {h}',         y=3)
        screen.write(f'delta: {delta}',        y=4)
        if p:
            screen.write(f'pressed: {p}',      y=5)

    @screen.on_key('escape', 'ctrl-c')
    def _(key):
        screen.stop()

    @screen.on_key('mouse-down')
    def _(key):
        if key.pos in presses:
            presses.remove(key.pos)
        else:
            presses.add(key.pos)

    screen.start()
