
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


import atexit
import curses
import os
import time
from kolr.util.events import Emitter
from kolr.term import escape_codes as ec
from sys import stdout, stdin, stderr
import readchar
from kolr.util.loop import RenderLoop


# ========================================================================= #
# GET CHAR                                                                  #
# ========================================================================= #

"""
Originally used: http://code.activestate.com/recipes/134892
But does not support unicode properly.
Now using 'readchar' library or curses instead.

TODO: goal is to only use the standard library
"""


# ========================================================================= #
# TERMINAL SESSION                                                          #
# ========================================================================= #


EVENT_RESIZE = 'resize'
EVENT_MOUSE = 'mouse'
EVENT_KEY = 'key'
EVENT_RENDER = 'render'


class TerminalController(RenderLoop):

    def __init__(self, frame_rate=10):
        super().__init__(frame_rate)
        # curses
        self._stdscr = None
        # callbacks TODO: replace with event manager
        self._emitter = Emitter([EVENT_RESIZE, EVENT_MOUSE, EVENT_KEY, EVENT_RENDER])

    # - - - - - - - - - - - - - - - - EVENT - - - - - - - - - - - - - - - - #

    def on(self, key, observer=None):
        return self._emitter.on(key, observer)

    def off(self, key, observer):
        return self._emitter.off(key, observer)

    # - - - - - - - - - - - - - - - -NCURSES- - - - - - - - - - - - - - - - #

    def _initialise(self):
        # similar to curses.wrapper
        if self._stdscr is not None:
            raise RuntimeError('TerminalController already begun.')
        self._stdscr = curses.initscr()
        # try - same as curses.wrapper
        curses.noecho()
        curses.cbreak()
        self._stdscr.keypad(True)
        try:
            curses.start_color()
        except:
            print('Color initialisation failed')

    def _finalise(self):
        # similar to curses.wrapper
        if self._stdscr is not None:
            self._stdscr.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        # delete var
        self._stdscr = None

    def _exit_finalise(self):
        self._finalise()
        print("Encountered Unknown Error")

    # - - - - - - - - - - - - - - - -LOOPING- - - - - - - - - - - - - - - - #

    def _pre_loop(self):
        self._initialise()
        atexit.register(self._exit_finalise)

    def _on_loop(self, delta) -> bool:
        # KEYS
        while True:
            self._stdscr.nodelay(True)
            key = self._stdscr.getch()
            if key == -1:
                break
            elif key == curses.KEY_RESIZE:
                h, w = self._stdscr.getmaxyx()
                if curses.LINES != h or curses.COLS != w:
                    curses.resizeterm(h, w)
                    self._emitter.emit(EVENT_RESIZE, w, h)
                pass
            elif key == curses.KEY_MOUSE:
                self._emitter.emit(EVENT_MOUSE, curses.getmouse())
            else:
                self._emitter.emit(EVENT_KEY, key)
        # RENDER
        self._emitter.emit(EVENT_RENDER, delta)

    def _post_loop(self):
        atexit.unregister(self._exit_finalise)
        self._finalise()

    # - - - - - - - - - - - - - - - INTERFACE - - - - - - - - - - - - - - - #

    def clear(self):
        self._stdscr.clear()

    def write_str(self, string, x=0, y=0):
        self._stdscr.addstr(y, x, string)

    def write_char(self, char, x=0, y=0):
        assert len(char) == 1
        self._stdscr.addstr(y, x, char)

    def flush(self):
        self._stdscr.refresh()

    # def launch_thread():
    #     self._event_thread = threading.Thread(target=self._event_loop)
    #     self._event_thread.start()
    #
    # def _event_loop(self):
    #     self._running = True
    #     while self._running:
    #         key = self._stdscr.getch()
    #         if key == -1:
    #             continue
    #         elif key == curses.KEY_RESIZE:
    #             h, w = self._stdscr.getmaxyx()
    #             if curses.LINES != h or curses.COLS != w:
    #                 curses.resizeterm(h, w)
    #                 self._emitter.emit(EVENT_RESIZE, w, h)
    #         elif key == curses.KEY_MOUSE:
    #             self._emitter.emit(EVENT_MOUSE, curses.getmouse())
    #         else:
    #             self._emitter.emit(EVENT_KEY, key)
    #
    # def _render_loop(self):
    #     self._running = True
    #     last_t = time.time_ns()
    #     while self._running:
    #         # update time
    #         t = time.time_ns()
    #         delta = (t - last_t) / 1_000_000_000
    #         last_t = t
    #         # callback
    #         self._emitter.emit(EVENT_RENDER, delta)
    #         # sleep
    #         sleep = 1 / self._frame_rate - delta
    #         if sleep > 0:
    #             time.sleep(sleep)


if __name__ == '__main__':

    def main():
        k, w, h = None, None, None

        # screen = TerminalSessionThreaded()
        screen = TerminalController()

        @screen.on(EVENT_KEY)
        def key_callback(key):
            nonlocal k
            if key == 27:
                screen.stop()
            k = key

        @screen.on(EVENT_RENDER)
        def render_callback(delta):
            nonlocal k
            screen.clear()
            screen.write_str(f'ASDF {k} {w} {h} {delta}')
            screen.flush()

        @screen.on(EVENT_RESIZE)
        def render_callback(_w, _h):
            nonlocal w, h
            w = _w
            h = _h

        screen.start()

    try:
        main()
    except Exception as e:
        try:
            TerminalController()._finalise()
        except:
            pass
        time.sleep(0.1)
        print(e)


# class TerminalSessionRaw(object):
#     def __init__(self):
#         self._running = False
#
#     def start(self):
#         # start
#         self._initialise()
#         # exit hooks
#         atexit.register(self._finalise)
#         return self
#
#     def stop(self):
#         # stop
#         self._finalise()
#         # remove exit hooks
#         atexit.unregister(self._finalise)
#         return self
#
#     def _initialise(self):
#         if self._running:
#             raise RuntimeError('Terminal session already begun.')
#         # Control
#         self._running = True
#         # Set Terminal Behavior
#         stdout.write(ec.csi.BPE)  # Bracket Paste - Enable
#         stdout.write(ec.csi.CH)   # Cursor - Hide
#         stdout.write(ec.csi.SBE)  # Screen Buffer - Enable
#         stdout.flush()
#
#     def _finalise(self):
#         if not self._running:
#             raise RuntimeError('Terminal session already ended.')
#         # Control
#         self._running = False
#         # Restore Terminal Behavior
#         stdout.write(ec.csi.SBD)  # Screen Buffer - Disable
#         stdout.write(ec.csi.CH)   # Cursor - Show
#         stdout.write(ec.csi.BPD)  # Bracket Paste - Disable
#         stdout.flush()
#
#
# if __name__ == '__main__':
#     def main():
#         controller = TerminalController()
#         controller.start()
#     main()


# class TerminalSessionThreaded(object):
#
#     def __init__(self, frame_rate=10, key_callback=None, mouse_callback=None, resize_callback=None, render_callback=None):
#         self._stdscr = None
#         self._running = False
#         self._frame_rate = frame_rate
#         # callbacks TODO: replace with event manager
#         self._key_callback = key_callback
#         self._mouse_callback = mouse_callback
#         self._resize_callback = resize_callback
#         self._render_callback = render_callback
#         # _event_thread
#         self._event_thread = None
#
#     def start(self):
#         # launch event loop in other thread
#         self._initialise()
#         atexit.register(self._finalise)
#         # launch main loop
#         self._render_loop()
#         return self
#
#     def stop(self):
#         atexit.unregister(self._finalise)
#         self._finalise()
#         # print error
#         # if exc_type is not None:
#         #     print('TerminalController closed due to an uncaught error', file=sys.stderr)
#         #     print(exc_traceback, file=sys.stderr)
#         #     print(exc_val, file=sys.stderr)
#         # ignore exceptions
#         return True
#
#     def _initialise(self):
#         if self._stdscr is not None:
#             raise RuntimeError('TerminalController already begun.')
#         self._stdscr = curses.initscr()
#         # try - same as curses.wrapper
#         curses.noecho()
#         curses.cbreak()
#         self._stdscr.keypad(True)
#         try:
#             curses.start_color()
#         except:
#             print('Color initialisation failed')
#         # launch event loop
#         self._event_thread = threading.Thread(target=self._event_loop)
#         self._event_thread.daemon = True
#         self._event_thread.start()
#
#     def _finalise(self):
#         if self._stdscr is None:
#             raise RuntimeError('TerminalController already ended.')
#         self._running = False
#         # finally - same as curses.wrapper
#         self._stdscr.keypad(False)
#         curses.echo()
#         curses.nocbreak()
#         curses.endwin()
#         # delete var
#         self._stdscr = None
#
#     def _event_loop(self):
#         self._running = True
#         while self._running:
#             key = self._stdscr.getch()
#             if key == -1:
#                 continue
#             elif key == curses.KEY_RESIZE:
#                 h, w = self._stdscr.getmaxyx()
#                 if curses.LINES != h or curses.COLS != w:
#                     curses.resizeterm(h, w)
#                     self._on_resize(w, h)
#             elif key == curses.KEY_MOUSE:
#                 self._on_mouse(curses.getmouse())
#             else:
#                 self._on_key(key)
#
#     def _render_loop(self):
#         self._running = True
#         last_t = time.time_ns()
#         while self._running:
#             # update time
#             t = time.time_ns()
#             delta = (t - last_t) / 1_000_000_000
#             last_t = t
#             # callback
#             self._on_render(delta)
#             # sleep
#             sleep = 1 / self._frame_rate - delta
#             if sleep > 0:
#                 time.sleep(sleep)
#
#     def _on_key(self, key):
#         if callable(self._key_callback):
#             self._key_callback(key)
#
#     def _on_mouse(self, mouse):
#         if callable(self._mouse_callback):
#             self._mouse_callback(mouse)
#
#     def _on_resize(self, w, h):
#         if callable(self._resize_callback):
#             self._resize_callback(w, h)
#
#     def _on_render(self, delta):
#         if callable(self._render_callback):
#             self._render_callback(self, delta)
#
#     def clear(self):
#         self._stdscr.clear()
#
#     def write_str(self, string, x=0, y=0):
#         self._stdscr.addstr(y, x, string)
#
#     def write_char(self, char, x=0, y=0):
#         assert len(char) == 1
#         self._stdscr.addstr(y, x, char)
#
#     def flush(self):
#         self._stdscr.refresh()
#
#
# if __name__ == '__main__':
#
#     def main():
#         k = None
#
#         def key_callback(key):
#             nonlocal k
#             if key == 27:
#                 screen.stop()
#             k = key
#
#         def render_callback(screen, delta):
#             nonlocal k
#             screen.clear()
#             screen.write_str(f'ASDF {k} {delta}')
#             screen.flush()
#
#         screen = TerminalController(
#             render_callback=render_callback,
#             key_callback=key_callback
#         )
#
#         screen.start()
#
#     main()