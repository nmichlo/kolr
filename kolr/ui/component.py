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
from typing import Optional, List
import stretched


# ========================================================================= #
# Buffer                                                                    #
# ========================================================================= #


class DoubleBuffer(object, metaclass=ABCMeta):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # buffers
        self._buffer_visible = None
        self._buffer_hidden = None
        # initialise
        self.clear()
        self.flush()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get(self, x, y):
        """
        Get a value from the visible buffer
        """
        return self._buffer_visible[y][x]

    def set(self, x, y, value):
        """
        Set a value for the hidden buffer
        """
        self._buffer_hidden[y][x] = value

    def set_from(self, buffer: 'DoubleBuffer', to_x=0, to_y=0, from_x=0, from_y=0, from_w=None, from_h=None):
        """
        Copy a region from another buffer into the specified location of this buffer.
        Trims the regions if the positions are negative or there are size mismatches.
        """
        # defaults
        if from_w is None: from_w = buffer.width
        if from_h is None: from_h = buffer.height
        # bounds
        r_ox = max(0, -to_x, -from_x)
        r_oy = max(0, -to_y, -from_y)
        r_w = min(from_w, buffer.width - from_x, self.width - to_x) - r_ox
        r_h = min(from_h, buffer.height - from_y, self.height - to_y) - r_oy
        # checks
        if (r_w <= 0) or (r_h <= 0):
            return
        # copy
        for y in range(r_oy, r_oy+r_h):
            self._buffer_hidden[to_y+y][to_x+r_ox:to_x+r_ox+r_w] = buffer._buffer_hidden[from_y+y][from_x+r_ox:from_x+r_ox+r_w]

    def diffs(self):
        """
        Yield the different indices between the hidden buffer and the visible buffer
        """
        for y in range(self._height):
            visible_row, hidden_row = self._buffer_visible[y], self._buffer_hidden[y]
            for x in range(self._width):
                if visible_row[x] != hidden_row[y]:
                    yield x, y

    def clear(self, char=' ', style=''):
        """
        Accepts a tuple of type: (char, style)
        """
        hidden_row = [(char, style) for x in range(self._width)]
        # shallow copy the rows
        self._buffer_hidden = [hidden_row[:] for y in range(self._height)]

    def flush(self):
        """
        flush the hidden buffer to the visible buffer
        """
        # Shallow copy as contents is immutable
        self._buffer_visible = [row[:] for row in self._buffer_hidden]


# ========================================================================= #
# Node                                                                      #
# ========================================================================= #


def nondirty(func):
    def inner(self, *args, **kwargs):
        if self.dirty:
            self.recompute()
        return func(*args, **kwargs)
    return inner


def dirties(func):
    return func


class Node:

    def __init__(self, width=None, height=None):
        assert width is None or (type(width) == int and width > 0)
        assert height is None or (type(height) == int and height > 0)
        # node
        self._children = []
        self._parent = None
        # layout
        self._x = None
        self._y = None
        self._w = None
        self._h = None
        # paint
        self._buffer = None
        # component
        self._event_listener = None
        # stretch
        self._node = stretched.Node(stretched.Style(
            size=stretched.Size(
                width=stretched.Dimension.new_points(width) if width else stretched.Dimension.AUTO,
                height=stretched.Dimension.new_points(height) if height else stretched.Dimension.AUTO,
            )
        ))

    # - - - - - - - - - - - - - - - -LAYOUTS- - - - - - - - - - - - - - - - #

    @property
    def dirty(self) -> bool:
        return self._node.dirty

    def compute_layout(self):
        print('WARNING: compute_layout is not implemented')
        # self._buffer = DoubleBuffer(None, None)
        pass

    # - - - - - - - - - - - - - - - RECTANGLE - - - - - - - - - - - - - - - #

    @property
    @nondirty
    def x(self) -> int: return self._x
    @property
    @nondirty
    def y(self) -> int: return self._y

    @property
    @nondirty
    def w(self) -> int: return self._w
    @property
    @nondirty
    def h(self) -> int: return self._h

    @property
    @nondirty
    def pos(self): return (self._x, self._y)
    @property
    @nondirty
    def size(self): return (self._w, self._h)
    @property
    @nondirty
    def rect(self): return (self._x, self._y, self._w, self._h)

    @nondirty
    def contains_coord(self, x, y):
        return (self._x <= x < self._x + self._w) and (self._y <= y < self._y + self._y)

    @nondirty
    def is_overlap(self, node: 'Node'):
        ox, oy, ow, oh = node.rect
        return not (
                (self._y + self._h < oy) or (self._y > oy + oh) or
                (self._x + self._w < ox) or (self._x > ox + ow)
        )

    # - - - - - - - - - - - - - - - - NODES - - - - - - - - - - - - - - - - #

    @dirties
    def add_child(self, node: 'Node'):
        assert isinstance(node, Node)
        assert not node.is_root
        assert not self.is_leaf
        assert not node.has_parent
        assert not self.contains_child(node)
        self._children.append(node)
        self._node.add_child(node._node)
        node._parent = self

    @dirties
    def remove_child(self, node: 'Node'):
        assert isinstance(node, Node)
        assert node.parent is self
        assert self.contains_child(node)
        self._children.remove(node)
        self._node.remove_child(node._node)
        node._parent = None

    @property
    def has_parent(self) -> bool: return self._parent is not None
    @property
    def has_children(self) -> bool: return len(self._children) > 0

    @property
    def children(self) -> List['Node']: return self._children[:]
    @property
    def parent(self) -> Optional['Node']: return self._parent

    def contains_child(self, node: 'Node'):
        assert isinstance(node, Node)
        return node in self._children

    def get_child_from_coord_recursive(self, x, y):
        """
        Assumes child nodes are contained within their parent nodes.
        """
        if self.contains_coord(x, y):
            for child in self._children:
                contains = child.get_child_from_coord_recursive(self)
                if contains:
                    return contains
            return self
        return None

    # - - - - - - - - - - - - - - - - EVENT - - - - - - - - - - - - - - - - #

    @property
    def has_event_listener(self):
        return callable(self._event_listener)

    def set_event_listener(self, func):
        assert not self.has_event_listener
        assert callable(func)
        self._event_listener = func

    def remove_event_listener(self):
        assert self.has_event_listener
        self._event_listener = None

    # def handle_mouse_click(self, x, y):
    #     if self.contains_coord(x, y):
    #         component = self.get_child_from_coord(x, y)
    #         if component is not None:
    #             component.handle_mouse_click(x, y)
    #         elif self.has_event_listener:
    #             self._event_listener.mouseClicked(x, y)

    # - - - - - - - - - - - - - - - - PAINT - - - - - - - - - - - - - - - - #

    def repaint(self):
        self.paint(self._buffer)
        for child in self._children:
            child.repaint()
            (cx, cy), (sx, sy) = child.pos, self.pos
            self._buffer.set_from(child._buffer, cx - sx, cy - sy)
        self._buffer.flush()

    def paint(self, buffer):
        pass

    # - - - - - - - - - - - - - -IS OVERRIDEABLE- - - - - - - - - - - - - - #

    @property
    def is_leaf(self): return False

    @property
    def is_root(self): return False

# ========================================================================= #
# Window                                                                    #
# ========================================================================= #


# class Window(Component):
#
#     def __init__(self, w, h):
#         super().__init__(0, 0, w, h)
#         self._buffer = DoubleBuffer(w, h)
#
#     def render(self):
#         self.paint(self._buffer)


# ========================================================================= #
# END                                                                    #
# ========================================================================= #
