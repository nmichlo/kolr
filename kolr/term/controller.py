
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
# TERMINAL CONTROLLER                                                       #
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

# ========================================================================= #
# END                                                                       #
# ========================================================================= #
