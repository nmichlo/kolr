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


# ========================================================================= #
# Buffer                                                                    #
# ========================================================================= #


class Buffer(object):
    def __init__(self, width, height, fill=' '):
        self._width = width
        self._height = height
        # buffer
        self._buffer = None
        # initialise
        self.clear(fill)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return self._width, self._height

    def get(self, x, y):
        """
        Get a value from the hidden buffer.
        :param x: x position
        :param y: y position
        :return: the value at the location
        """
        return self._buffer[y][x]

    def set(self, x, y, value):
        """
        Set a value for the hidden buffer
        :param x: x position
        :param y: y position
        :param value: the value to set at the location
        """
        self._buffer[y][x] = value

    def set_from(self, src_buf: 'Buffer', from_x=0, from_y=0, from_w=None, from_h=None, to_x=0, to_y=0):
        """
        Copy a region from another buffer into the specified location of this buffer.
        Trims the regions if the positions are negative or there are size mismatches.
        :param src_buf: The source buffer
        :param from_x: source buffer rectangular (src_buf) region's top left corner x pos.
        :param from_y: source buffer rectangular (src_buf) region's top left corner y pos.
        :param from_w: source buffer rectangular (src_buf) region's width.
        :param from_h: source buffer rectangular (src_buf) region's height.
        :param to_x: target buffer (self) region's top left corner x pos.
        :param to_y: target buffer (self) region's top left corner y pos.
        """
        # defaults
        if from_w is None: from_w = src_buf.width
        if from_h is None: from_h = src_buf.height
        # bounds
        r_ox = max(0, -to_x, -from_x)
        r_oy = max(0, -to_y, -from_y)
        r_w = min(from_w, src_buf.width - from_x, self.width - to_x) - r_ox
        r_h = min(from_h, src_buf.height - from_y, self.height - to_y) - r_oy
        # checks
        if (r_w <= 0) or (r_h <= 0):
            return
        # copy
        for y in range(r_oy, r_oy+r_h):
            self._buffer[to_y + y][to_x + r_ox:to_x + r_ox + r_w] = src_buf._buffer[from_y + y][from_x + r_ox:from_x + r_ox + r_w]

    def clear(self, fill=' '):
        """
        :param fill: The immutable value to fill the entire buffer
        """
        self._buffer = Buffer._make_2d_array(self._width, self._height, fill)

    @staticmethod
    def _make_2d_array(w, h, fill):
        row = [fill for x in range(w)]
        return [row[:] for y in range(h)]  # shallow copy the rows

    @staticmethod
    def _shallow_copy_2d(array):
        return [row[:] for row in array]



# ========================================================================= #
# Double Buffer                                                             #
# ========================================================================= #


class DoubleBuffer(Buffer):
    def __init__(self, width, height):
        super().__init__(width, height)
        # buffers
        self._buffer_visible = None
        # initialise
        self.flush()

    def get(self, x, y):
        """
        Get a value from the visible buffer.
        :param x: x position
        :param y: y position
        :return: the value at the location
        """
        return self._buffer_visible[y][x]

    def swap(self):
        """
        swap the hidden buffer to the visible buffer
        """
        self._buffer, self._buffer_visible = self._buffer_visible, self._buffer

    def flush(self):
        self._buffer_visible = DoubleBuffer._shallow_copy_2d(self._buffer)

    def diffs(self):
        """
        Yield the different indices between the hidden buffer and the visible buffer
        """
        for y in range(self._height):
            visible_row, hidden_row = self._buffer_visible[y], self._buffer[y]
            for x in range(self._width):
                if visible_row[x] != hidden_row[y]:
                    yield x, y


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
