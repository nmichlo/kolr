#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#
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
#
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #


from typing import Dict, Tuple, List
import os
import re

from jinja2 import Template
from unidecode import unidecode
from copy import deepcopy, copy
from kolr.color import Color
from kolr.util import util


# ========================================================================= #
# Types                                                                     #
# ========================================================================= #

_ColorHex = str
_ColorRgb = Tuple[int, int, int]

_ListRgb = List[_ColorRgb]
_ListNames = List[str]

_NamedColorHex = Tuple[str, _ColorHex]
_NamedColorRgb = Tuple[str, _ColorRgb]

_NamedColorHexList = List[_NamedColorHex]
_NamedColorRgbList = List[_NamedColorRgb]

_NameToColorHexDict = Dict[str, _ColorHex]
_NameToColorRgbDict = Dict[str, _ColorRgb]

_ColorHexDict = Dict[str, _ColorHex]
_ColorRgbDict = Dict[str, _ColorRgb]


# ========================================================================= #
# Parent ColorPalettes                                                      #
# ========================================================================= #


_STR_TEMPLATE_SEPARATOR = "\n# {{'='*73}} #\n# {{name}}{{' '*(73-(name|length))}} #\n# {{'='*73}} #\n"
_STR_TEMPLATE_STRING_FIELDS = "{% for (field, value) in fields %}{{field}} = '{{value}}'\n{% endfor %}"
_STR_TEMPLATE_VAR_FIELDS = "{% for (field, value) in fields %}{{field}} = {{value}}\n{% endfor %}"
_STR_TEMPLATE_INIT_FILE = "{% for name in names %}import {{package}}.{{name}}\n{% endfor %}"


class BaseColorPalette(object):
    NAME = None

    def __init__(self, name_color_tuples, unique_colors=False):
        assert type(self.NAME) == str, 'Specify the name of the color palette'
        assert self.NAME == BaseColorPalette.standardised_name(self.NAME), 'Name must follow rules of python field'
        assert util.is_iterable(name_color_tuples), TypeError(f'Non-Iterable names: {type(name_color_tuples)}')
        # names
        _names_orig = [name for name, _ in name_color_tuples]
        self._names, _conflicts = BaseColorPalette.generate_unique_names(_names_orig)
        # colors
        self._colors = [Color(color) for _, color in name_color_tuples]
        # sorted
        self._argsorted  = sorted(range(len(self._names)), key=self._names.__getitem__)
        self._name2index = {name: i for i, name in enumerate(self._names)}
        # validate
        BaseColorPalette._assert_names_unique_colors_unique(self._names, self._colors, ignore_colors=not unique_colors)

    def __len__(self):
        return len(self._names)

    def __getitem__(self, item):
        # TODO global default get type
        if type(item) == int:
            return self._names[self._argsorted[item]]
        elif type(item) == str:
            return self._colors[self._name2index[item]]
        else:
            raise TypeError('Invalid getter type')

    @staticmethod
    def standardised_name(name: str):
        if not name:
            return name
        standardised = unidecode(name)
        standardised = standardised.lower()
        standardised = re.sub('[-\']', '', standardised)
        standardised = re.sub('[/\\\\]', '_or_', standardised)
        standardised = re.sub('[^a-zA-Z0-9]+', '_', standardised)
        standardised = standardised.rstrip('_')
        if standardised[0].isdigit():
            standardised = f'_{standardised}'
        return standardised

    @staticmethod
    def generate_unique_names(orig_names: _ListNames) -> Tuple[_ListNames, Dict[str, Tuple[str, str, int]]]:
        names = [BaseUrlColorPalette.standardised_name(orig) for orig in orig_names]
        indices = sorted(range(len(names)), key=lambda i: f'{names[i]}={orig_names[i]}={i}')  # argsort
        # find conflicts & repetitions
        unique, conflicts, stack = [None] * len(orig_names), {}, [(None, None)]
        for i in indices:
            i, orig, name, first = i, orig_names[i], names[i], stack[0][1]
            if name != first:
                stack = []  # define new stack so conflicts aren't cleared
            else:
                conflicts[first], name = stack, f'{first}{len(stack)}'
            stack.append((orig, name, i))
            unique[i] = name  # unsort unique
        # return
        return unique, conflicts

    @staticmethod
    def _assert_names_unique_colors_unique(name_list: _ListNames, color_list: List, ignore_colors=True):
        assert len(name_list), len(color_list)
        colors, names = {}, {}
        for name, color in zip(name_list, color_list):
            if name in names:
                raise KeyError(f'Names not unique for: "{name}" -> {color} / {names[name]}')
            names[name] = color
            if not ignore_colors and color in colors:
                raise KeyError(f'Colors not unique for: {color} -> "{name}" / {colors[color]}')
            colors[color] = name

    def nearest_color(self, color):
        # import numpy as np
        # i = np.argmin(np.sum((np.array([c.rgb for c in self._colors]) - np.array(color.rgb)) ** 2, axis=1))
        # return self._colors[i]
        rgb = color.rgb
        closest, dist = None, float('inf')
        for c in self._colors:
            r = c.rgb
            d = ((rgb[0] - r[0]) ** 2 + (rgb[1] - r[1]) ** 2 + (rgb[2] - r[2]) ** 2) ** 0.5
            if d <= dist:
                closest, dist = c, d
            if d == 0:
                break
        return Color(closest)

    def as_palette(self, palette) -> 'BaseColorPalette':
        assert isinstance(palette, BaseColorPalette), 'not a pallette'
        new_colors = [palette.nearest_color(color) for color in self._colors]
        new_palette = copy(self)
        new_palette._colors = new_colors
        return new_palette

    def generate_python(self, color_type='rgb'):
        return Template(f'{_STR_TEMPLATE_SEPARATOR}\n\n{_STR_TEMPLATE_STRING_FIELDS if color_type == "hex" else _STR_TEMPLATE_VAR_FIELDS}').render(
            fields=zip(self, (getattr(self[name], color_type) for name in self)),
            name=f'{self.NAME}: {color_type}'
        )

    def save_python(self, color_type='rgb'):
        os.makedirs(f'gen/{color_type}', exist_ok=True)
        util.overwrite_file(f'gen/rgb/{self.NAME}.py', self.generate_python(color_type=color_type))

    def print(self):
        for name, (r, g, b) in ((self._names[i], self._colors[i].rgb) for i in self._argsorted):
            print(f'\033[38;2;{r};{g};{b}m{name}\033[0m')
        print()


class BaseUrlColorPalette(BaseColorPalette):
    URL = None

    def __init__(self):
        assert type(self.URL) == str, 'Specify the url of the color dataset'
        super().__init__(self._get_colors_from_data(util.fetch_url(self.URL)))

    def _get_colors_from_data(self, data: str) -> _NamedColorRgbList:
        raise NotImplementedError('Override Me!')


# ========================================================================= #
# Color Palettes                                                            #
# ========================================================================= #


class ColorPaletteXkcd(BaseUrlColorPalette):
    URL = 'https://xkcd.com/color/rgb.txt'
    NAME = 'xkcd'

    def _get_colors_from_data(self, data: str) -> _NamedColorHexList:
        import re
        pattern = re.compile('^(.+)\t(#[0-9abcdef]{6})')
        return [match for line in data.split('\n') for match in pattern.findall(line)]


class ColorPaletteMeodai(BaseUrlColorPalette):
    URL ='https://raw.githubusercontent.com/meodai/color-names/master/src/colornames.csv'
    NAME = 'meodai'

    def _get_colors_from_data(self, data: str) -> _NamedColorHexList:
        import csv
        return [item for item in csv.reader(data.split('\n'))][1:]


class ColorPalette3Bit(BaseColorPalette):
    NAME = 'colors_3_bit'

    def __init__(self):
        from kolr.term.colors import COLORS_3_BIT
        super().__init__(COLORS_3_BIT)


class ColorPalette4Bit(BaseColorPalette):
    NAME = 'colors_4_bit'

    def __init__(self):
        from kolr.term.colors import COLORS_4_BIT
        super().__init__(COLORS_4_BIT)


class ColorPalette8Bit(BaseColorPalette):
    NAME = 'colors_8_bit'

    def __init__(self):
        from kolr.term.colors import COLORS_8_BIT
        super().__init__(COLORS_8_BIT, unique_colors=False)


class ColorPalette8BitWikipedia(BaseColorPalette):
    NAME = 'colors_8_bit_wikipedia'

    def __init__(self):
        from kolr.term.colors import COLORS_8_BIT_WIKIPEDIA
        super().__init__(COLORS_8_BIT_WIKIPEDIA, unique_colors=False)


# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    _COLORS_3_BIT = ColorPalette3Bit()
    _COLORS_4_BIT = ColorPalette4Bit()
    _COLORS_8_BIT = ColorPalette8Bit()
    _COLORS_8_BIT_WIKIPEDIA = ColorPalette8BitWikipedia()
    _COLORS_XKCD = ColorPaletteXkcd()
    _COLOR_MEODIA = ColorPaletteMeodai()

    _COLORS_4_BIT.print()
    print()
    _COLORS_4_BIT.as_palette(_COLORS_3_BIT).print()
    print()
    _COLORS_4_BIT.as_palette(_COLORS_3_BIT).print()
    print()
    _COLORS_8_BIT.as_palette(_COLORS_4_BIT).print()

    _COLORS_8_BIT.generate_python('rgb')
    _COLORS_8_BIT_WIKIPEDIA.generate_python('hex')


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
