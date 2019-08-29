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
from kolr.ui.buffer import Buffer, DoubleBuffer


# ========================================================================= #
# Component                                                                      #
# ========================================================================= #


def nondirty(func):
    def inner(self, *args, **kwargs):
        if self.dirty:
            print('Warning: needs recompute')
            # self.recompute()
        return func(self, *args, **kwargs)
    return inner


def dirties(func):
    return func


class Component:

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
        # buffer
        self._buffer: DoubleBuffer = None
        # stretch
        self._node = stretched.Node(stretched.Style(
            size=stretched.Size(
                width=stretched.Dimension.new_points(width) if width else stretched.DimensionValue.AUTO,
                height=stretched.Dimension.new_points(height) if height else stretched.DimensionValue.AUTO,
            ),
            padding=stretched.Rect(
                start=stretched.Dimension.new_points(1),
                end=stretched.Dimension.new_points(1),
                top=stretched.Dimension.new_points(1),
                bottom=stretched.Dimension.new_points(1),
            )
        ))

    # - - - - - - - - - - - - - - - -LAYOUTS- - - - - - - - - - - - - - - - #

    @property
    def dirty(self) -> bool:
        return self._node.dirty

    def compute_layout(self, width, height):
        self._node.compute_layout(stretched.Size(width, height))
        if not self._buffer or self._buffer.size != (width, height):
            self._buffer = DoubleBuffer(width, height)

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
    def is_overlap(self, node: 'Component'):
        ox, oy, ow, oh = node.rect
        return not (
                (self._y + self._h < oy) or (self._y > oy + oh) or
                (self._x + self._w < ox) or (self._x > ox + ow)
        )

    # - - - - - - - - - - - - - - - - NODES - - - - - - - - - - - - - - - - #

    @dirties
    def add_child(self, node: 'Component'):
        assert isinstance(node, Component)
        assert not node.is_root
        assert not self.is_leaf
        assert not node.has_parent
        assert not self.contains_child(node)
        self._children.append(node)
        self._node.add_child(node._node)
        node._parent = self

    @dirties
    def remove_child(self, node: 'Component'):
        assert isinstance(node, Component)
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
    def children(self) -> List['Component']: return self._children[:]
    @property
    def parent(self) -> Optional['Component']: return self._parent

    def contains_child(self, node: 'Component'):
        assert isinstance(node, Component)
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

    # @property
    # def has_event_listener(self):
    #     return callable(self._event_listener)
    #
    # def set_event_listener(self, func):
    #     assert not self.has_event_listener
    #     assert callable(func)
    #     self._event_listener = func
    #
    # def remove_event_listener(self):
    #     assert self.has_event_listener
    #     self._event_listener = None

    # def handle_mouse_click(self, x, y):
    #     if self.contains_coord(x, y):
    #         component = self.get_child_from_coord(x, y)
    #         if component is not None:
    #             component.handle_mouse_click(x, y)
    #         elif self.has_event_listener:
    #             self._event_listener.mouseClicked(x, y)

    # - - - - - - - - - - - - - - - - PAINT - - - - - - - - - - - - - - - - #

    @nondirty
    def repaint(self):
        self.paint(self._buffer)
        for child in self._children:
            child.repaint()
            (cx, cy), (sx, sy) = child.pos, self.pos
            self._buffer.set_from(child._buffer, cx - sx, cy - sy)
        self._buffer.flush()

    def paint(self, buffer):
        # ┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # ┃         ┃   0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F   ┃
        # ┣━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        # ┃ U+250x  ┃   ─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏   ┃
        # ┃ U+251x  ┃   ┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟   ┃
        # ┃ U+252x  ┃   ┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯   ┃
        # ┃ U+253x  ┃   ┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿   ┃
        # ┃ U+254x  ┃   ╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏   ┃
        # ┃ U+255x  ┃   ═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟   ┃
        # ┃ U+256x  ┃   ╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯   ┃
        # ┃ U+257x  ┃   ╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿   ┃
        # ┗━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        # for x in range(1, buffer.width-1):
        #     buffer.set(x, 0, '━')
        #     buffer.set(x, buffer.height-1, '━')
        # for y in range(1, buffer.height-1):
        #     buffer.set(0, y, '┃')
        #     buffer.set(buffer.width-1, y, '┃')
        buffer.set(0, 0, 'R')
        buffer.set(buffer.width-1, 0, '┓')
        buffer.set(0, buffer.height-1, '┗')
        buffer.set(buffer.width-1, buffer.height-1, '┛')

    # - - - - - - - - - - - - - -IS OVERRIDEABLE- - - - - - - - - - - - - - #

    @property
    def is_leaf(self): return False

    @property
    def is_root(self): return False


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
