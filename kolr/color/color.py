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


from kolr.term.detect_color import CODE_24_BIT, CODE_3_BIT, CODE_4_BIT, CODE_8_BIT, DETECTED_CODE, CODE_MONO
from kolr.term.escape_codes import sgr, clr
from kolr.util.util import cached_property


# ========================================================================= #
# COLOR                                                                     #
# ========================================================================= #


class Color(object):
    """
    Basic color object that supports conversion between rgb and hex values.
    Computed values are cached.

    TODO: instead of cache_property, this should use flywheel pattern and color dictionaries
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
    def rgb(self):
        return self._rgb

    @cached_property
    def hex(self):
        return '#%02x%02x%02x' % self._rgb

    @staticmethod
    def hex_to_rgb(hex):
        hex = hex.lstrip('#')
        assert len(hex) == 6
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb):
        assert len(rgb) == 3 and all(0 <= v <= 255 for v in rgb)
        return '#%02x%02x%02x' % rgb

    def escape_code(self, colors=DETECTED_CODE, bg=False):
        if colors == CODE_MONO:
            return ''
        elif colors == CODE_3_BIT:
            from kolr.palette import COLOR_PALETTE_3_BIT
            idx = COLOR_PALETTE_3_BIT.nearest_index(self)
            return clr.bg3(idx) if bg else clr.fg3(idx)
        elif colors == CODE_4_BIT:
            from kolr.palette import COLOR_PALETTE_4_BIT
            idx = COLOR_PALETTE_4_BIT.nearest_index(self)
            return clr.bg4(idx) if bg else clr.fg4(idx)
        elif colors == CODE_8_BIT:
            from kolr.palette import COLOR_PALETTE_8_BIT
            idx = COLOR_PALETTE_8_BIT.nearest_index(self)
            return clr.bg8(idx) if bg else clr.fg8(idx)
        elif colors == CODE_24_BIT:
            return sgr.bg_select(self.rgb) if bg else sgr.fg_select(self.rgb)
        else:
            raise KeyError('Invalid Terminal Colors')

    @cached_property
    def fg(self):
        return self.escape_code(DETECTED_CODE, bg=False)

    @cached_property
    def bg(self):
        return self.escape_code(DETECTED_CODE, bg=True)

    @cached_property
    def fg3(self):
        return self.escape_code(CODE_3_BIT, bg=False)

    @cached_property
    def bg3(self):
        return self.escape_code(CODE_3_BIT, bg=True)

    @cached_property
    def fg4(self):
        return self.escape_code(CODE_4_BIT, bg=False)

    @cached_property
    def bg4(self):
        return self.escape_code(CODE_4_BIT, bg=True)

    @cached_property
    def fg8(self):
        return self.escape_code(CODE_8_BIT, bg=False)

    @cached_property
    def bg8(self):
        return self.escape_code(CODE_8_BIT, bg=True)

    @cached_property
    def fg24(self):
        return self.escape_code(CODE_24_BIT, bg=False)

    @cached_property
    def bg24(self):
        return self.escape_code(CODE_24_BIT, bg=True)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
