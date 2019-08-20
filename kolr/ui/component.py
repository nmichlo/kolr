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


import abc
from abc import ABCMeta
import sys
from curses import wrapper
from typing import Optional, List
import stretched
import atexit
import time
import threading
import curses

class TerminalSession(object):

    def __init__(self, frame_rate=10, key_callback=None, mouse_callback=None, resize_callback=None, render_callback=None):
        self._stdscr = None
        self._running = False
        self._frame_rate = frame_rate
        # callbacks TODO: replace with event manager
        self._key_callback = key_callback
        self._mouse_callback = mouse_callback
        self._resize_callback = resize_callback
        self._render_callback = render_callback
        # _event_thread
        self._event_thread = None

    def start(self):
        # launch event loop in other thread
        self._initialise()
        atexit.register(self._finalise)
        # launch main loop
        self._render_loop()
        return self

    def stop(self):
        atexit.unregister(self._finalise)
        self._finalise()
        # print error
        # if exc_type is not None:
        #     print('TerminalSession closed due to an uncaught error', file=sys.stderr)
        #     print(exc_traceback, file=sys.stderr)
        #     print(exc_val, file=sys.stderr)
        # ignore exceptions
        return True

    def _initialise(self):
        if self._stdscr is not None:
            raise RuntimeError('TerminalSession already begun.')
        self._stdscr = curses.initscr()
        # try - same as curses.wrapper
        curses.noecho()
        curses.cbreak()
        self._stdscr.keypad(True)
        try:
            curses.start_color()
        except:
            print('Color initialisation failed')
        # launch event loop
        self._event_thread = threading.Thread(target=self._event_loop)
        self._event_thread.daemon = True
        self._event_thread.start()

    def _finalise(self):
        if self._stdscr is None:
            raise RuntimeError('TerminalSession already ended.')
        self._running = False
        # finally - same as curses.wrapper
        self._stdscr.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        # delete var
        self._stdscr = None

    def _event_loop(self):
        self._running = True
        while self._running:
            key = self._stdscr.getch()
            if key == -1:
                continue
            elif key == curses.KEY_RESIZE:
                h, w = self._stdscr.getmaxyx()
                if curses.LINES != h or curses.COLS != w:
                    curses.resizeterm(h, w)
                    self._on_resize(w, h)
            elif key == curses.KEY_MOUSE:
                self._on_mouse(curses.getmouse())
            else:
                self._on_key(key)

    def _render_loop(self):
        self._running = True
        last_t = time.time_ns()
        while self._running:
            # update time
            t = time.time_ns()
            delta = (t - last_t) / 1_000_000_000
            last_t = t
            # callback
            self._on_render(delta)
            # sleep
            sleep = 1 / self._frame_rate - delta
            if sleep > 0:
                time.sleep(sleep)

    def _on_key(self, key):
        if callable(self._key_callback):
            self._key_callback(key)

    def _on_mouse(self, mouse):
        if callable(self._mouse_callback):
            self._mouse_callback(mouse)

    def _on_resize(self, w, h):
        if callable(self._resize_callback):
            self._resize_callback(w, h)

    def _on_render(self, delta):
        if callable(self._render_callback):
            self._render_callback(self, delta)

    def clear(self):
        self._stdscr.clear()

    def write_str(self, string, x=0, y=0):
        self._stdscr.addstr(y, x, string)

    def write_char(self, char, x=0, y=0):
        assert len(char) == 1
        self._stdscr.addstr(y, x, char)

    def flush(self):
        self._stdscr.refresh()


if __name__ == '__main__':

    def main():
        k = None

        def key_callback(key):
            nonlocal k
            if key == 27:
                screen.stop()
            k = key

        def render_callback(screen, delta):
            nonlocal k
            screen.clear()
            screen.write_str(f'ASDF {k} {delta}')
            screen.flush()

        screen = TerminalSession(
            render_callback=render_callback,
            key_callback=key_callback
        )

        screen.start()

    main()






# class DoubleBuffer(object, metaclass=ABCMeta):
#
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#         # buffers
#         self._buffer_visible = None
#         self._buffer_hidden = None
#         # initialise
#         self.clear()
#         self.flush()
#
#     @property
#     def width(self):
#         return self._width
#
#     @property
#     def height(self):
#         return self._height
#
#     def get(self, x, y):
#         """
#         Get a value from the visible buffer
#         """
#         return self._buffer_visible[y][x]
#
#     def set(self, x, y, value):
#         """
#         Set a value for the hidden buffer
#         """
#         self._buffer_hidden[y][x] = value
#
#     def set_from(self, buffer: 'DoubleBuffer', to_x=0, to_y=0, from_x=0, from_y=0, from_w=None, from_h=None):
#         """
#         Copy a region from another buffer into the specified location of this buffer.
#         Trims the regions if the positions are negative or there are size mismatches.
#         """
#         # defaults
#         if from_w is None: from_w = buffer.width
#         if from_h is None: from_h = buffer.height
#         # bounds
#         r_ox = max(0, -to_x, -from_x)
#         r_oy = max(0, -to_y, -from_y)
#         r_w = min(from_w, buffer.width - from_x, self.width - to_x) - r_ox
#         r_h = min(from_h, buffer.height - from_y, self.height - to_y) - r_oy
#         # checks
#         if (r_w <= 0) or (r_h <= 0):
#             return
#         # copy
#         for y in range(r_oy, r_oy+r_h):
#             self._buffer_hidden[to_y+y][to_x+r_ox:to_x+r_ox+r_w] = buffer._buffer_hidden[from_y+y][from_x+r_ox:from_x+r_ox+r_w]
#
#     def diffs(self):
#         """
#         Yield the different indices between the hidden buffer and the visible buffer
#         """
#         for y in range(self._height):
#             visible_row, hidden_row = self._buffer_visible[y], self._buffer_hidden[y]
#             for x in range(self._width):
#                 if visible_row[x] != hidden_row[y]:
#                     yield x, y
#
#     def clear(self, char=' ', style=''):
#         """
#         Accepts a tuple of type: (char, style)
#         """
#         hidden_row = [(char, style) for x in range(self._width)]
#         # shallow copy the rows
#         self._buffer_hidden = [hidden_row[:] for y in range(self._height)]
#
#     def flush(self):
#         """
#         flush the hidden buffer to the visible buffer
#         """
#         # Shallow copy as contents is immutable
#         self._buffer_visible = [row[:] for row in self._buffer_hidden]
#
#
# def nondirty(func):
#     def inner(self, *args, **kwargs):
#         if self.dirty:
#             self.recompute()
#         return func(*args, **kwargs)
#     return inner
#
#
# def dirties(func):
#     return func
#
#
# class Node:
#
#     def __init__(self, width=None, height=None):
#         assert width is None or (type(width) == int and width > 0)
#         assert height is None or (type(height) == int and height > 0)
#         # node
#         self._children = []
#         self._parent = None
#         # layout
#         self._x = None
#         self._y = None
#         self._w = None
#         self._h = None
#         # paint
#         self._buffer = None
#         # component
#         self._event_listener = None
#         # stretch
#         self._node = stretched.Node(stretched.Style(
#             size=stretched.Size(
#                 width=stretched.Dimension.new_points(width) if width else stretched.Dimension.AUTO,
#                 height=stretched.Dimension.new_points(height) if height else stretched.Dimension.AUTO,
#             )
#         ))
#
#     # - - - - - - - - - - - - - - - -LAYOUTS- - - - - - - - - - - - - - - - #
#
#     @property
#     def dirty(self) -> bool:
#         return self._node.dirty
#
#     def compute_layout(self):
#         print('WARNING: compute_layout is not implemented')
#         # self._buffer = DoubleBuffer(None, None)
#         pass
#
#     # - - - - - - - - - - - - - - - RECTANGLE - - - - - - - - - - - - - - - #
#
#     @property
#     @nondirty
#     def x(self) -> int: return self._x
#     @property
#     @nondirty
#     def y(self) -> int: return self._y
#
#     @property
#     @nondirty
#     def w(self) -> int: return self._w
#     @property
#     @nondirty
#     def h(self) -> int: return self._h
#
#     @property
#     @nondirty
#     def pos(self): return (self._x, self._y)
#     @property
#     @nondirty
#     def size(self): return (self._w, self._h)
#     @property
#     @nondirty
#     def rect(self): return (self._x, self._y, self._w, self._h)
#
#     @nondirty
#     def contains_coord(self, x, y):
#         return (self._x <= x < self._x + self._w) and (self._y <= y < self._y + self._y)
#
#     @nondirty
#     def is_overlap(self, node: 'Node'):
#         ox, oy, ow, oh = node.rect
#         return not (
#                 (self._y + self._h < oy) or (self._y > oy + oh) or
#                 (self._x + self._w < ox) or (self._x > ox + ow)
#         )
#
#     # - - - - - - - - - - - - - - - - NODES - - - - - - - - - - - - - - - - #
#
#     @dirties
#     def add_child(self, node: 'Node'):
#         assert isinstance(node, Node)
#         assert not node.is_root
#         assert not self.is_leaf
#         assert not node.has_parent
#         assert not self.contains_child(node)
#         self._children.append(node)
#         self._node.add_child(node._node)
#         node._parent = self
#
#     @dirties
#     def remove_child(self, node: 'Node'):
#         assert isinstance(node, Node)
#         assert node.parent is self
#         assert self.contains_child(node)
#         self._children.remove(node)
#         self._node.remove_child(node._node)
#         node._parent = None
#
#     @property
#     def has_parent(self) -> bool: return self._parent is not None
#     @property
#     def has_children(self) -> bool: return len(self._children) > 0
#
#     @property
#     def children(self) -> List['Node']: return self._children[:]
#     @property
#     def parent(self) -> Optional['Node']: return self._parent
#
#     def contains_child(self, node: 'Node'):
#         assert isinstance(node, Node)
#         return node in self._children
#
#     def get_child_from_coord_recursive(self, x, y):
#         """
#         Assumes child nodes are contained within their parent nodes.
#         """
#         if self.contains_coord(x, y):
#             for child in self._children:
#                 contains = child.get_child_from_coord_recursive(self)
#                 if contains:
#                     return contains
#             return self
#         return None
#
#     # - - - - - - - - - - - - - - - - EVENT - - - - - - - - - - - - - - - - #
#
#     @property
#     def has_event_listener(self):
#         return callable(self._event_listener)
#
#     def set_event_listener(self, func):
#         assert not self.has_event_listener
#         assert callable(func)
#         self._event_listener = func
#
#     def remove_event_listener(self):
#         assert self.has_event_listener
#         self._event_listener = None
#
#     # def handle_mouse_click(self, x, y):
#     #     if self.contains_coord(x, y):
#     #         component = self.get_child_from_coord(x, y)
#     #         if component is not None:
#     #             component.handle_mouse_click(x, y)
#     #         elif self.has_event_listener:
#     #             self._event_listener.mouseClicked(x, y)
#
#     # - - - - - - - - - - - - - - - - PAINT - - - - - - - - - - - - - - - - #
#
#     def repaint(self):
#         self.paint(self._buffer)
#         for child in self._children:
#             child.repaint()
#             (cx, cy), (sx, sy) = child.pos, self.pos
#             self._buffer.set_from(child._buffer, cx - sx, cy - sy)
#         self._buffer.flush()
#
#     def paint(self, buffer):
#         pass
#
#     # - - - - - - - - - - - - - -IS OVERRIDEABLE- - - - - - - - - - - - - - #
#
#     @property
#     def is_leaf(self): return False
#
#     @property
#     def is_root(self): return False
















#
#
#
#
#
# class Window(Component):
#
#     def __init__(self, w, h):
#         super().__init__(0, 0, w, h)
#         self._buffer = DoubleBuffer(w, h)
#
#     def render(self):
#         self.paint(self._buffer)
#
#
#
# class TerminalInterface(object):
#     pass
#
#
# class Renderer(object):
#     pass




#
#
#
#
#
#
# from colosseum import CSS
# from colosseum.dimensions import Size, Box
#
# # https://colosseum.readthedocs.io/en/latest/tutorial/tutorial-1.html
#
# class MyDOMNode:
#     def __init__(self, name=None, style=None, children=None):
#         self.name = name if name else 'div'
#         self.parent = None
#         self.children = []
#         if children:
#             for child in children:
#                 self.children.append(child)
#                 child.parent = self
#         self.intrinsic = Size(self)
#         self.layout = Box(self)
#         self.style = style.copy(self) if style else CSS()
#
#     def __repr__(self):
#         return '<{}:{} {}>'.format(self.name, id(self), str(self.layout))
#
#     def add(self, child):
#         self.children.append(child)
#         child.parent = self
#
#
# node = MyDOMNode(style=CSS(width=1000, height=1000))
# node.add(MyDOMNode(style=CSS(width=100, height=200)))
# node.add(MyDOMNode(style=CSS(width=300, height=150)))
# node.style.flex_direction = COLUMN
# node.style.update()
# print(node.layout)
#
# # node.layout.content_width
# # node.layout.content_width
# # node.layout.content_top
# # node.layout.content_left
# # for child in node.children:
# #     print(child.layout)



















# class Screen(with_metaclass(ABCMeta, _AbstractCanvas)):
#     """
#     Class to track basic state of the screen.  This constructs the necessary
#     resources to allow us to do the ASCII animations.
#
#     This is an abstract class that will build the correct concrete class for
#     you when you call :py:meth:`.wrapper`.  If needed, you can use the
#     :py:meth:`~.Screen.open` and :py:meth:`~.Screen.close` methods for finer
#     grained control of the construction and tidy up.
#
#     Note that you need to define the required height for your screen buffer.
#     This is important if you plan on using any Effects that will scroll the
#     screen vertically (e.g. Scroll).  It must be big enough to handle the
#     full scrolling of your selected Effect.
#     """
#
#     # Text attributes for use when printing to the Screen.
#     A_BOLD = constants.A_BOLD
#     A_NORMAL = constants.A_NORMAL
#     A_REVERSE = constants.A_REVERSE
#     A_UNDERLINE = constants.A_UNDERLINE
#
#     # Text colours for use when printing to the Screen.
#     COLOUR_BLACK = constants.COLOUR_BLACK
#     COLOUR_RED = constants.COLOUR_RED
#     COLOUR_GREEN = constants.COLOUR_GREEN
#     COLOUR_YELLOW = constants.COLOUR_YELLOW
#     COLOUR_BLUE = constants.COLOUR_BLUE
#     COLOUR_MAGENTA = constants.COLOUR_MAGENTA
#     COLOUR_CYAN = constants.COLOUR_CYAN
#     COLOUR_WHITE = constants.COLOUR_WHITE
#
#     def __init__(self, height, width, buffer_height, unicode_aware):
#         """
#         Don't call this constructor directly.
#         """
#         super(Screen, self).__init__(
#             height, width, buffer_height, 0, unicode_aware)
#
#         # Initialize base class variables - e.g. those used for drawing.
#         self.height = height
#         self.width = width
#         self._last_start_line = 0
#
#         # Set up internal state for colours - used by children to determine
#         # changes to text colour when refreshing the screen.
#         self._colour = 0
#         self._attr = 0
#         self._bg = 0
#
#         # tracking of current cursor position - used in screen refresh.
#         self._cur_x = 0
#         self._cur_y = 0
#
#         # Control variables for playing out a set of Scenes.
#         self._scenes = []
#         self._scene_index = 0
#         self._frame = 0
#         self._idle_frame_count = 0
#         self._forced_update = False
#         self._unhandled_input = self._unhandled_event_default
#
#     @classmethod
#     def open(cls, height=None, catch_interrupt=False, unicode_aware=None):
#         """
#         Construct a new Screen for any platform.  This will just create the
#         correct Screen object for your environment.  See :py:meth:`.wrapper` for
#         a function to create and tidy up once you've finished with the Screen.
#
#         :param height: The buffer height for this curses_screen (for testing only).
#         :param catch_interrupt: Whether to catch and prevent keyboard
#             interrupts.  Defaults to False to maintain backwards compatibility.
#         :param unicode_aware: Whether the application can use unicode or not.
#             If None, try to detect from the environment if UTF-8 is enabled.
#         """
#         if sys.platform == "win32":
#             # Clone the standard output buffer so that we can do whatever we
#             # need for the application, but restore the buffer at the _finalise.
#             # Note that we need to resize the clone to ensure that it is the
#             # same size as the original in some versions of Windows.
#             old_out = win32console.PyConsoleScreenBufferType(
#                 win32file.CreateFile("CONOUT$",
#                                      win32file.GENERIC_READ | win32file.GENERIC_WRITE,
#                                      win32file.FILE_SHARE_WRITE,
#                                      None,
#                                      win32file.OPEN_ALWAYS,
#                                      0,
#                                      None))
#             try:
#                 info = old_out.GetConsoleScreenBufferInfo()
#             except pywintypes.error:
#                 info = None
#             win_out = win32console.CreateConsoleScreenBuffer()
#             if info:
#                 win_out.SetConsoleScreenBufferSize(info['Size'])
#             else:
#                 win_out.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
#             win_out.SetConsoleActiveScreenBuffer()
#
#             # Get the standard input buffer.
#             win_in = win32console.PyConsoleScreenBufferType(
#                 win32file.CreateFile("CONIN$",
#                                      win32file.GENERIC_READ | win32file.GENERIC_WRITE,
#                                      win32file.FILE_SHARE_READ,
#                                      None,
#                                      win32file.OPEN_ALWAYS,
#                                      0,
#                                      None))
#             win_in.SetStdHandle(win32console.STD_INPUT_HANDLE)
#
#             # Hide the cursor.
#             win_out.SetConsoleCursorInfo(1, 0)
#
#             # Disable scrolling
#             out_mode = win_out.GetConsoleMode()
#             win_out.SetConsoleMode(
#                 out_mode & ~ win32console.ENABLE_WRAP_AT_EOL_OUTPUT)
#
#             # Enable mouse input, disable quick-edit mode and disable ctrl-c
#             # if needed.
#             in_mode = win_in.GetConsoleMode()
#             new_mode = (in_mode | win32console.ENABLE_MOUSE_INPUT |
#                         ENABLE_EXTENDED_FLAGS)
#             new_mode &= ~ENABLE_QUICK_EDIT_MODE
#             if catch_interrupt:
#                 # Ignore ctrl-c handlers if specified.
#                 new_mode &= ~win32console.ENABLE_PROCESSED_INPUT
#             win_in.SetConsoleMode(new_mode)
#
#             screen = _WindowsScreen(win_out, win_in, height, old_out, in_mode,
#                                     unicode_aware=unicode_aware)
#         else:
#             # Reproduce curses.wrapper()
#             stdscr = curses.initscr()
#             curses.noecho()
#             curses.cbreak()
#             stdscr.keypad(1)
#
#             # Fed up with linters complaining about original curses code - trying to be a bit better...
#             # noinspection PyBroadException
#             # pylint: disable=broad-except
#             try:
#                 curses.start_color()
#             except Exception as e:
#                 logger.debug(e)
#             screen = _CursesScreen(stdscr, height,
#                                    catch_interrupt=catch_interrupt,
#                                    unicode_aware=unicode_aware)
#
#         return screen
#
#     @abstractmethod
#     def close(self, restore=True):
#         """
#         Close down this Screen and tidy up the environment as required.
#
#         :param restore: whether to restore the environment or not.
#         """
#
#     @classmethod
#     def wrapper(cls, func, height=None, catch_interrupt=False, arguments=None,
#                 unicode_aware=None):
#         """
#         Construct a new Screen for any platform.  This will initialize the
#         Screen, call the specified function and then tidy up the system as
#         required when the function exits.
#
#         :param func: The function to call once the Screen has been created.
#         :param height: The buffer height for this Screen (only for test purposes).
#         :param catch_interrupt: Whether to catch and prevent keyboard
#             interrupts.  Defaults to False to maintain backwards compatibility.
#         :param arguments: Optional arguments list to pass to func (after the
#             Screen object).
#         :param unicode_aware: Whether the application can use unicode or not.
#             If None, try to detect from the environment if UTF-8 is enabled.
#         """
#         screen = Screen.open(height,
#                              catch_interrupt=catch_interrupt,
#                              unicode_aware=unicode_aware)
#         restore = True
#         try:
#             try:
#                 if arguments:
#                     return func(screen, *arguments)
#                 else:
#                     return func(screen)
#             except ResizeScreenError:
#                 restore = False
#                 raise
#         finally:
#             screen.close(restore)
#
#     def _reset(self):
#         """
#         Reset the Screen.
#         """
#         self._last_start_line = 0
#         self._colour = None
#         self._attr = None
#         self._bg = None
#         self._cur_x = None
#         self._cur_y = None
#
#     def refresh(self):
#         """
#         Refresh the screen.
#         """
#         # Scroll the screen now - we've already sorted the double-buffer to reflect this change.
#         if self._last_start_line != self._start_line:
#             self._scroll(self._start_line - self._last_start_line)
#             self._last_start_line = self._start_line
#
#         # Now draw any deltas to the scrolled screen.  Note that CJK character sets sometimes
#         # use double-width characters, so don't try to draw the next 2nd char (of 0 width).
#         for y, x in self._buffer.deltas(0, self.height):
#             new_cell = self._buffer.get(x, y)
#             if new_cell[4] > 0:
#                 self._change_colours(new_cell[1], new_cell[2], new_cell[3])
#                 self._print_at(chr(new_cell[0]), x, y, new_cell[4])
#
#         # Resynch for next refresh.
#         self._buffer.sync()
#
#     def clear(self):
#         """
#         Clear the Screen of all content.
#
#         Note that this will instantly clear the Screen and reset all buffers to the default state,
#         without waiting for you to call :py:meth:`~.Screen.refresh`.
#         """
#         # Clear the actual terminal
#         self.reset()
#         self._change_colours(Screen.COLOUR_WHITE, 0, 0)
#         self._clear()
#
#     def get_key(self):
#         """
#         Check for a key without waiting.  This method is deprecated.  Use
#         :py:meth:`.get_event` instead.
#         """
#         event = self.get_event()
#         if event and isinstance(event, KeyboardEvent):
#             return event.key_code
#         return None
#
#     @abstractmethod
#     def get_event(self):
#         """
#         Check for any events (e.g. key-press or mouse movement) without waiting.
#
#         :returns: A :py:obj:`.Event` object if anything was detected, otherwise
#                   it returns None.
#         """
#
#     @staticmethod
#     def ctrl(char):
#         """
#         Calculate the control code for a given key.  For example, this converts
#         "a" to 1 (which is the code for ctrl-a).
#
#         :param char: The key to convert to a control code.
#         :return: The control code as an integer or None if unknown.
#         """
#         # Convert string to int... assuming any non-integer is a string.
#         # TODO: Consider asserting a more rigorous test without falling back to past basestring.
#         if not isinstance(char, int):
#             char = ord(char.upper())
#
#         # Only deal with the characters between '@' and '_'
#         return char & 0x1f if 64 <= char <= 95 else None
#
#     @abstractmethod
#     def has_resized(self):
#         """
#         Check whether the screen has been re-sized.
#
#         :returns: True when the screen has been re-sized since the last check.
#         """
#
#     def getch(self, x, y):
#         """
#         Get the character at a specified location.  This method is deprecated.
#         Use :py:meth:`.get_from` instead.
#
#         :param x: The x coordinate.
#         :param y: The y coordinate.
#         """
#         return self.get_from(x, y)
#
#     def putch(self, text, x, y, colour=7, attr=0, bg=0, transparent=False):
#         """
#         Print text at the specified location.  This method is deprecated.  Use
#         :py:meth:`.print_at` instead.
#
#         :param text: The (single line) text to be printed.
#         :param x: The column (x coord) for the _initialise of the text.
#         :param y: The line (y coord) for the _initialise of the text.
#         :param colour: The colour of the text to be displayed.
#         :param attr: The cell attribute of the text to be displayed.
#         :param bg: The background colour of the text to be displayed.
#         :param transparent: Whether to print spaces or not, thus giving a
#             transparent effect.
#         """
#         self.print_at(text, x, y, colour, attr, bg, transparent)
#
#     @staticmethod
#     def _unhandled_event_default(event):
#         """
#         Default unhandled event handler for handling simple scene navigation.
#         """
#         if isinstance(event, KeyboardEvent):
#             c = event.key_code
#             if c in (ord("X"), ord("x"), ord("Q"), ord("q")):
#                 raise StopApplication("User terminated app")
#             if c in (ord(" "), ord("\n"), ord("\r")):
#                 raise NextScene()
#
#     def play(self, scenes, stop_on_resize=False, unhandled_input=None,
#              start_scene=None, repeat=True, allow_int=False):
#         """
#         Play a set of scenes.
#
#         This is effectively a helper function to wrap :py:meth:`.set_scenes` and
#         :py:meth:`.draw_next_frame` to simplify animation for most applications.
#
#         :param scenes: a list of :py:obj:`.Scene` objects to play.
#         :param stop_on_resize: Whether to stop when the screen is resized.
#             Default is to carry on regardless - which will typically result
#             in an error. This is largely done for back-compatibility.
#         :param unhandled_input: Function to call for any input not handled
#             by the Scenes/Effects being played.  Defaults to a function that
#             closes the application on "Q" or "X" being pressed.
#         :param start_scene: The old Scene to _initialise from.  This must have name
#             that matches the name of one of the Scenes passed in.
#         :param repeat: Whether to repeat the Scenes once it has reached the _finalise.
#             Defaults to True.
#         :param allow_int: Allow input to interrupt frame rate delay.
#
#         :raises ResizeScreenError: if the screen is resized (and allowed by
#             stop_on_resize).
#
#         The unhandled input function just takes one parameter - the input
#         event that was not handled.
#         """
#         # Initialise the Screen for animation.
#         self.set_scenes(
#             scenes, unhandled_input=unhandled_input, start_scene=start_scene)
#
#         # Mainline loop for animations
#         try:
#             while True:
#                 a = time.time()
#                 self.draw_next_frame(repeat=repeat)
#                 if self.has_resized():
#                     if stop_on_resize:
#                         self._scenes[self._scene_index].exit()
#                         raise ResizeScreenError("Screen resized",
#                                                 self._scenes[self._scene_index])
#                 b = time.time()
#                 if b - a < 0.05:
#                     # Just in case time has jumped (e.g. time change), ensure we only delay for 0.05s
#                     pause = min(0.05, a + 0.05 - b)
#                     if allow_int:
#                         self.wait_for_input(pause)
#                     else:
#                         time.sleep(pause)
#         except StopApplication:
#             # Time to stop  - just exit the function.
#             return
#
#     def set_scenes(self, scenes, unhandled_input=None, start_scene=None):
#         """
#         Remember a set of scenes to be played.  This must be called before
#         using :py:meth:`.draw_next_frame`.
#
#         :param scenes: a list of :py:obj:`.Scene` objects to play.
#         :param unhandled_input: Function to call for any input not handled
#             by the Scenes/Effects being played.  Defaults to a function that
#             closes the application on "Q" or "X" being pressed.
#         :param start_scene: The old Scene to _initialise from.  This must have name
#             that matches the name of one of the Scenes passed in.
#
#         :raises ResizeScreenError: if the screen is resized (and allowed by
#             stop_on_resize).
#
#         The unhandled input function just takes one parameter - the input
#         event that was not handled.
#         """
#         # Save off the scenes now.
#         self._scenes = scenes
#
#         # Set up default unhandled input handler if needed.
#         if unhandled_input is None:
#             # Check that none of the Effects is incompatible with the default
#             # handler.
#             safe = True
#             for scene in self._scenes:
#                 for effect in scene.effects:
#                     safe &= effect.safe_to_default_unhandled_input
#             if safe:
#                 unhandled_input = self._unhandled_event_default
#         self._unhandled_input = unhandled_input
#
#         # Find the starting scene.  Default to first if no match.
#         self._scene_index = 0
#         if start_scene is not None:
#             for i, scene in enumerate(scenes):
#                 if scene.name == start_scene.name:
#                     self._scene_index = i
#                     break
#
#         # Reset the Scene - this allows the original scene to pick up old
#         # values on resizing.
#         self._scenes[self._scene_index].reset(
#             old_scene=start_scene, screen=self)
#
#         # Reset other internal state for the animation
#         self._frame = 0
#         self._idle_frame_count = 0
#         self._forced_update = False
#         self.clear()
#
#     def draw_next_frame(self, repeat=True):
#         """
#         Draw the next frame in the currently configured Scenes. You must call
#         :py:meth:`.set_scenes` before using this for the first time.
#
#         :param repeat: Whether to repeat the Scenes once it has reached the _finalise.
#             Defaults to True.
#
#         :raises StopApplication: if the application should be terminated.
#         """
#         scene = self._scenes[self._scene_index]
#         try:
#             # Check for an event now and remember for refresh reasons.
#             event = self.get_event()
#             got_event = event is not None
#
#             # Now process all the input events
#             while event is not None:
#                 event = scene.process_event(event)
#                 if event is not None and self._unhandled_input is not None:
#                     self._unhandled_input(event)
#                 event = self.get_event()
#
#             # Only bother with a refresh if there was an event to process or
#             # we have to refresh due to the refresh limit required for an
#             # Effect.
#             self._frame += 1
#             self._idle_frame_count -= 1
#             if got_event or self._idle_frame_count <= 0 or self._forced_update:
#                 self._forced_update = False
#                 self._idle_frame_count = 1000000
#                 for effect in scene.effects:
#                     # Update the effect and delete if needed.
#                     effect.update(self._frame)
#                     if effect.delete_count is not None:
#                         effect.delete_count -= 1
#                         if effect.delete_count <= 0:
#                             scene.remove_effect(effect)
#
#                     # Sort out when we next _need_ to do a refresh.
#                     if effect.frame_update_count > 0:
#                         self._idle_frame_count = min(self._idle_frame_count,
#                                                      effect.frame_update_count)
#                 self.refresh()
#
#             if 0 < scene.duration <= self._frame:
#                 raise NextScene()
#         except NextScene as e:
#             # Tidy up the current scene.
#             scene.exit()
#
#             # Find the specified next Scene
#             if e.name is None:
#                 # Just allow next iteration of loop
#                 self._scene_index += 1
#                 if self._scene_index >= len(self._scenes):
#                     if repeat:
#                         self._scene_index = 0
#                     else:
#                         raise StopApplication("Repeat disabled")
#             else:
#                 # Find the required scene.
#                 for i, scene in enumerate(self._scenes):
#                     if scene.name == e.name:
#                         self._scene_index = i
#                         break
#                 else:
#                     raise RuntimeError(
#                         "Could not find Scene: '{}'".format(e.name))
#
#             # Reset the screen if needed.
#             scene = self._scenes[self._scene_index]
#             scene.reset()
#             self._frame = 0
#             self._idle_frame_count = 0
#             if scene.clear:
#                 self.clear()
#
#     @property
#     def current_scene(self):
#         """
#         :return: The scene currently being rendered. To be used in conjunction
#                  with :py:meth:`.draw_next_frame`.
#         """
#         return self._scenes[self._scene_index]
#
#     def force_update(self):
#         """
#         Force the Screen to redraw the current Scene on the next call to
#         draw_next_frame, overriding the frame_update_count value for all the
#         Effects.
#         """
#         self._forced_update = True
#
#     @abstractmethod
#     def _change_colours(self, colour, attr, bg):
#         """
#         Change current colour if required.
#
#         :param colour: New colour to use.
#         :param attr: New attributes to use.
#         :param bg: New background colour to use.
#         """
#
#     @abstractmethod
#     def wait_for_input(self, timeout):
#         """
#         Wait until there is some input or the timeout is hit.
#
#         :param timeout: Time to wait for input in seconds (floating point).
#         """
#
#     @abstractmethod
#     def _print_at(self, text, x, y, width):
#         """
#         Print string at the required location.
#
#         :param text: The text string to print.
#         :param x: The x coordinate
#         :param y: The Y coordinate
#         :param width: The width of the character (for dual-width glyphs in CJK languages).
#         """
#
#     @abstractmethod
#     def _clear(self):
#         """
#         Clear the curses_screen.
#         """
#
#     @abstractmethod
#     def _scroll(self, lines):
#         """
#         Scroll the curses_screen up or down.
#
#         :param lines: Number of lines to scroll.  Negative numbers scroll down.
#         """
#
#     @abstractmethod
#     def set_title(self, title):
#         """
#         Set the title for this terminal/console session.  This will typically
#         change the text displayed in the curses_screen title bar.
#
#         :param title: The title to be set.
#         """
#
#
# class ManagedScreen():
#     """
#     Decorator and class to create a managed Screen. It can be used in
#     two ways. If used as a method decorator it will create and open a new Screen,
#     pass the screen to the method as a keyword argument, and close the
#     screen when the method has completed. If used with the with statement
#     the class will create and open a new Screen, return the screen for
#     using in the block, and close the screen when the statement ends.
#     Note that any arguments are in this class so that you can use it
#     as a decorator or using the with statment. No arguments are required
#     to use.
#     """
#
#     def __init__(self, func=lambda: None):
#         update_wrapper(self, func)
#         self.func = func
#
#     def __get__(self, obj, objtype):
#         """
#         Class decorator method, so we can use the class in a with statement.
#
#         See https://stackoverflow.com/a/3296318/4994021 for details.
#         """
#         return partial(self.__call__, obj)
#
#     def __call__(self, *args, **kwargs):
#         screen = Screen.open()
#         kwargs["screen"] = screen
#         output = self.func(*args, **kwargs)
#         screen.close()
#         return output
#
#     def __enter__(self):
#         """
#         Method used for with statement
#         """
#         self.screen = Screen.open()
#         return self.screen
#
#     def __exit__(self, type, value, traceback):
#         """
#         Method used for with statement
#         """
#         self.screen.close()
#

#     # UNIX compatible platform - use curses
#     import curses
#     import select
#     import termios
#
#     class _CursesScreen(Screen):
#         """
#         Curses screen implementation.
#         """
#
#         # Virtual key code mapping.
#         _KEY_MAP = {
#             27: Screen.KEY_ESCAPE,
#             curses.KEY_F1: Screen.KEY_F1,
#             curses.KEY_F2: Screen.KEY_F2,
#             curses.KEY_F3: Screen.KEY_F3,
#             curses.KEY_F4: Screen.KEY_F4,
#             curses.KEY_F5: Screen.KEY_F5,
#             curses.KEY_F6: Screen.KEY_F6,
#             curses.KEY_F7: Screen.KEY_F7,
#             curses.KEY_F8: Screen.KEY_F8,
#             curses.KEY_F9: Screen.KEY_F9,
#             curses.KEY_F10: Screen.KEY_F10,
#             curses.KEY_F11: Screen.KEY_F11,
#             curses.KEY_F12: Screen.KEY_F12,
#             curses.KEY_F13: Screen.KEY_F13,
#             curses.KEY_F14: Screen.KEY_F14,
#             curses.KEY_F15: Screen.KEY_F15,
#             curses.KEY_F16: Screen.KEY_F16,
#             curses.KEY_F17: Screen.KEY_F17,
#             curses.KEY_F18: Screen.KEY_F18,
#             curses.KEY_F19: Screen.KEY_F19,
#             curses.KEY_F20: Screen.KEY_F20,
#             curses.KEY_F21: Screen.KEY_F21,
#             curses.KEY_F22: Screen.KEY_F22,
#             curses.KEY_F23: Screen.KEY_F23,
#             curses.KEY_F24: Screen.KEY_F24,
#             curses.KEY_PRINT: Screen.KEY_PRINT_SCREEN,
#             curses.KEY_IC: Screen.KEY_INSERT,
#             curses.KEY_DC: Screen.KEY_DELETE,
#             curses.KEY_HOME: Screen.KEY_HOME,
#             curses.KEY_END: Screen.KEY_END,
#             curses.KEY_LEFT: Screen.KEY_LEFT,
#             curses.KEY_UP: Screen.KEY_UP,
#             curses.KEY_RIGHT: Screen.KEY_RIGHT,
#             curses.KEY_DOWN: Screen.KEY_DOWN,
#             curses.KEY_PPAGE: Screen.KEY_PAGE_UP,
#             curses.KEY_NPAGE: Screen.KEY_PAGE_DOWN,
#             curses.KEY_BACKSPACE: Screen.KEY_BACK,
#             9: Screen.KEY_TAB,
#             curses.KEY_BTAB: Screen.KEY_BACK_TAB
#             # Terminals translate keypad keys, so no need for a special
#             # mapping here.
#
#             # Terminals don't transmit meta keys (like control, shift, etc), so
#             # there's no translation for them either.
#         }
#
#         def __init__(self, win, height=None, catch_interrupt=False,
#                      unicode_aware=False):
#             """
#             :param win: The curses_screen object as returned by the curses wrapper method.
#             :param height: The height of the screen buffer to be used (for teesting only).
#             :param catch_interrupt: Whether to catch SIGINT or not.
#             :param unicode_aware: Whether this Screen can use unicode or not.
#             """
#             # Determine unicode support if needed.
#             if unicode_aware is None:
#                 try:
#                     encoding = getlocale()[1]
#                     if not encoding:
#                         encoding = getdefaultlocale()[1]
#                 except ValueError:
#                     encoding = os.environ.get("LC_CTYPE")
#                 unicode_aware = (encoding is not None and
#                                  encoding.lower() == "utf-8")
#
#             # Save off the screen details.
#             super(_CursesScreen, self).__init__(
#                 win.getmaxyx()[0], win.getmaxyx()[1], height, unicode_aware)
#             self._screen = win
#             self._screen.keypad(1)
#
#             # Set up basic colour schemes.
#             self.colours = curses.COLORS
#
#             # Disable the cursor.
#             curses.curs_set(0)
#
#             # Non-blocking key checks.
#             self._screen.nodelay(1)
#
#             # Store previous handlers for restoration at close
#             self._signal_state = _SignalState()
#
#             # Set up signal handler for screen resizing.
#             self._re_sized = False
#             self._signal_state.set(signal.SIGWINCH, self._resize_handler)
#
#             # Catch SIGINTs and translated them to ctrl-c if needed.
#             if catch_interrupt:
#                 # Ignore SIGINT (ctrl-c) and SIGTSTP (ctrl-z) signals.
#                 self._signal_state.set(signal.SIGINT, self._catch_interrupt)
#                 self._signal_state.set(signal.SIGTSTP, self._catch_interrupt)
#
#             # Enable mouse events
#             curses.mousemask(curses.ALL_MOUSE_EVENTS |
#                              curses.REPORT_MOUSE_POSITION)
#
#             # Lookup the necessary escape codes in the terminfo database.
#             self._move_y_x = curses.tigetstr("cup")
#             self._up_line = curses.tigetstr("ri").decode("utf-8")
#             self._down_line = curses.tigetstr("ind").decode("utf-8")
#             self._fg_color = curses.tigetstr("setaf")
#             self._bg_color = curses.tigetstr("setab")
#             self._clear_line = curses.tigetstr("el").decode("utf-8")
#             if curses.tigetflag("hs"):
#                 self._start_title = curses.tigetstr("tsl").decode("utf-8")
#                 self._end_title = curses.tigetstr("fsl").decode("utf-8")
#             else:
#                 self._start_title = self._end_title = None
#             self._a_normal = curses.tigetstr("sgr0").decode("utf-8")
#             self._a_bold = curses.tigetstr("bold").decode("utf-8")
#             self._a_reverse = curses.tigetstr("rev").decode("utf-8")
#             self._a_underline = curses.tigetstr("smul").decode("utf-8")
#             self._clear_screen = curses.tigetstr("clear").decode("utf-8")
#
#             # Look for a mismatch between the kernel terminal and the terminfo
#             # database for backspace.  Fix up keyboard mappings if needed.
#             kbs = curses.tigetstr("kbs").decode("utf-8")
#             tbs = termios.tcgetattr(sys.stdin)[6][termios.VERASE]
#             if tbs != kbs:
#                 self._KEY_MAP[ord(tbs)] = Screen.KEY_BACK
#
#             # Conversion from Screen attributes to curses equivalents.
#             self._ATTRIBUTES = {
#                 Screen.A_BOLD: self._a_bold,
#                 Screen.A_NORMAL: self._a_normal,
#                 Screen.A_REVERSE: self._a_reverse,
#                 Screen.A_UNDERLINE: self._a_underline
#             }
#
#             # Byte stream processing for unicode input.
#             self._bytes_to_read = 0
#             self._bytes_to_return = b""
#
#             # We'll actually break out into low-level output, so flush any
#             # high level buffers now.
#             self._screen.refresh()
#
#         def close(self, restore=True):
#             """
#             Close down this Screen and tidy up the environment as required.
#
#             :param restore: whether to restore the environment or not.
#             """
#             self._signal_state.restore()
#             if restore:
#                 self._screen.keypad(0)
#                 curses.echo()
#                 curses.nocbreak()
#                 curses.endwin()
#
#         @staticmethod
#         def _safe_write(msg):
#             """
#             Safe write to screen - catches IOErrors on screen resize.
#
#             :param msg: The message to write to the screen.
#             """
#             try:
#                 sys.stdout.write(msg)
#             except IOError:
#                 # Screen resize can throw IOErrors.  These can be safely
#                 # ignored as the screen will be shortly reset anyway.
#                 pass
#
#         def _resize_handler(self, *_):
#             """
#             Window resize signal handler.  We don't care about any of the
#             parameters passed in beyond the object reference.
#             """
#             curses.endwin()
#             curses.initscr()
#             self._re_sized = True
#
#         def _scroll(self, lines):
#             """
#             Scroll the curses_screen up or down.
#
#             :param lines: Number of lines to scroll.  Negative numbers scroll
#                 down.
#             """
#             if lines < 0:
#                 self._safe_write("{}{}".format(
#                     curses.tparm(self._move_y_x, 0, 0).decode("utf-8"),
#                     (self._up_line + self._clear_line) * -lines))
#             else:
#                 self._safe_write("{}{}".format(curses.tparm(
#                     self._move_y_x, self.height, 0).decode("utf-8"),
#                     (self._down_line + self._clear_line) * lines))
#
#         def _clear(self):
#             """
#             Clear the Screen of all content.
#             """
#             self._safe_write(self._clear_screen)
#             sys.stdout.flush()
#
#         def refresh(self):
#             """
#             Refresh the screen.
#             """
#             super(_CursesScreen, self).refresh()
#             try:
#                 sys.stdout.flush()
#             except IOError:
#                 pass
#
#         @staticmethod
#         def _catch_interrupt(signal_no, frame):
#             """
#             SIGINT handler.  We ignore the signal and frame info passed in.
#             """
#             # Stop pep-8 shouting at me for unused params I can't control.
#             del frame
#
#             # The OS already caught the ctrl-c, so inject it now for the next
#             # input.
#             if signal_no == signal.SIGINT:
#                 curses.ungetch(3)
#             elif signal_no == signal.SIGTSTP:
#                 curses.ungetch(26)
#             return
#
#         def get_event(self):
#             """
#             Check for an event without waiting.
#             """
#             # Spin through notifications until we find something we want.
#             key = 0
#             while key != -1:
#                 # Get the next key
#                 key = self._screen.getch()
#
#                 if key == curses.KEY_RESIZE:
#                     # Handle screen resize
#                     self._re_sized = True
#                 elif key == curses.KEY_MOUSE:
#                     # Handle a mouse event
#                     _, x, y, _, bstate = curses.getmouse()
#                     buttons = 0
#                     # Some Linux modes only report clicks, so check for any
#                     # button down or click events.
#                     if (bstate & curses.BUTTON1_PRESSED != 0 or
#                             bstate & curses.BUTTON1_CLICKED != 0):
#                         buttons |= MouseEvent.LEFT_CLICK
#                     if (bstate & curses.BUTTON3_PRESSED != 0 or
#                             bstate & curses.BUTTON3_CLICKED != 0):
#                         buttons |= MouseEvent.RIGHT_CLICK
#                     if bstate & curses.BUTTON1_DOUBLE_CLICKED != 0:
#                         buttons |= MouseEvent.DOUBLE_CLICK
#                     return MouseEvent(x, y, buttons)
#                 elif key != -1:
#                     # Handle any byte streams first
#                     logger.debug("Processing key: %x", key)
#                     if self._unicode_aware and key > 0:
#                         if key & 0xC0 == 0xC0:
#                             self._bytes_to_return = struct.pack(b"B", key)
#                             self._bytes_to_read = bin(key)[2:].index("0") - 1
#                             logger.debug("Byte stream: %d bytes left",
#                                          self._bytes_to_read)
#                             continue
#                         elif self._bytes_to_read > 0:
#                             self._bytes_to_return += struct.pack(b"B", key)
#                             self._bytes_to_read -= 1
#                             if self._bytes_to_read > 0:
#                                 continue
#                             else:
#                                 key = ord(self._bytes_to_return.decode("utf-8"))
#
#                     # Handle a genuine key press.
#                     logger.debug("Returning key: %x", key)
#                     if key in self._KEY_MAP:
#                         return KeyboardEvent(self._KEY_MAP[key])
#                     elif key != -1:
#                         return KeyboardEvent(key)
#
#             return None
#
#         def has_resized(self):
#             """
#             Check whether the screen has been re-sized.
#             """
#             re_sized = self._re_sized
#             self._re_sized = False
#             return re_sized
#
#         def _change_colours(self, colour, attr, bg):
#             """
#             Change current colour if required.
#
#             :param colour: New colour to use.
#             :param attr: New attributes to use.
#             :param bg: New background colour to use.
#             """
#             # Change attribute first as this will reset colours when swapping
#             # modes.
#             if attr != self._attr:
#                 self._safe_write(self._a_normal)
#                 if attr != 0:
#                     self._safe_write(self._ATTRIBUTES[attr])
#                 self._attr = attr
#                 self._colour = None
#                 self._bg = None
#
#             # Now swap colours if required.
#             if colour != self._colour:
#                 self._safe_write(curses.tparm(
#                     self._fg_color, colour).decode("utf-8"))
#                 self._colour = colour
#             if bg != self._bg:
#                 self._safe_write(curses.tparm(
#                     self._bg_color, bg).decode("utf-8"))
#                 self._bg = bg
#
#         def _print_at(self, text, x, y, width):
#             """
#             Print string at the required location.
#
#             :param text: The text string to print.
#             :param x: The x coordinate
#             :param y: The Y coordinate
#             :param width: The width of the character (for dual-width glyphs in CJK languages).
#             """
#             # Move the cursor if necessary
#             cursor = u""
#             if x != self._cur_x or y != self._cur_y:
#                 cursor = curses.tparm(self._move_y_x, y, x).decode("utf-8")
#
#             # Print the text at the required location and update the current
#             # position.
#             try:
#                 self._safe_write(cursor + text)
#             except UnicodeEncodeError:
#                 # This is probably a sign that the user has the wrong locale.
#                 # Try to soldier on anyway.
#                 self._safe_write(cursor + "?" * len(text))
#
#             # Update cursor position for next time...
#             self._cur_x = x + width
#             self._cur_y = y
#
#         def wait_for_input(self, timeout):
#             """
#             Wait until there is some input or the timeout is hit.
#
#             :param timeout: Time to wait for input in seconds (floating point).
#             """
#             try:
#                 select.select([sys.stdin], [], [], timeout)
#             except select.error:
#                 # Any error will almost certainly result in a a Screen.  Ignore.
#                 pass
#
#         def set_title(self, title):
#             """
#             Set the title for this terminal/console session.  This will
#             typically change the text displayed in the curses_screen title bar.
#
#             :param title: The title to be set.
#             """
#             if self._start_line is not None:
#                 self._safe_write("{}{}{}".format(self._start_title, title,
#                                                  self._end_title))
#
#     class _SignalState(object):
#         """
#         Save previous user signal state while setting signals.
#
#         Used for signal restoration when asciimatics no longer has control
#         of the user program.
#         """
#
#         def __init__(self):
#             self._old_signal_states = []
#
#         def set(self, signalnum, handler):
#             """
#             Set signal handler and record their previous values.
#
#             :param signalnum: The const/enum matching to the signal to be set.
#             :param handler: The function/const to set the signal to
#             """
#             old_handler = signal.getsignal(signalnum)
#             # Some environments may install a non-Python handler (which returns None at this point).
#             # We can't reinstate these, so just reset the default handler in such cases.
#             if old_handler is None:
#                 old_handler = signal.SIG_DFL
#             self._old_signal_states.append((signalnum, old_handler))
#             signal.signal(signalnum, handler)
#
#         def restore(self):
#             """
#             Restore saved signals to their previous handles.
#             """
#             for signalnum, handler in self._old_signal_states:
#                 signal.signal(signalnum, handler)
#             self._old_signal_states = []
#
