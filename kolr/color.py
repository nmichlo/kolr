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


# ========================================================================= #
# COLOR                                                                     #
# ========================================================================= #


class Color(object):
    """
    Basic color object that supports conversion between rgb and hex values.
    Computed values are cached.
    """

    def __init__(self, color):
        self._rgb = None

        # Convert color to correct type
        t = type(color)
        if t == Color:
            self._rgb = color._rgb
        elif t == tuple:
            assert len(color) == 3 and all(0 <= v <= 255 and type(v) == int for v in color)
            self._rgb = color
        elif t == str:
            assert len(color) == 7 and color[0] == '#'
            self._rgb = Color.hex_to_rgb(color)
        else:
            raise TypeError(f'Unsupported Type: {t}')

    def __hash__(self):
        return self.rgb.__hash__()

    def __eq__(self, other):
        if type(other) == Color:
            return self.rgb == other.rgb
        return False

    def __str__(self):
        return self.hex

    def __repr__(self):
        return str(self)

    @property
    def hex(self):
        return '#%02x%02x%02x' % self._rgb

    @property
    def rgb(self):
        return self._rgb

    @staticmethod
    def hex_to_rgb(hex):
        hex = hex.lstrip('#')
        assert len(hex) == 6
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb):
        assert len(rgb) == 3 and all(0 <= v <= 255 for v in rgb)
        return '#%02x%02x%02x' % rgb



# ========================================================================= #
# END                                                                       #
# ========================================================================= #
