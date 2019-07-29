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


import os
import re
from typing import Dict, Tuple, List
from cachier import cachier
from jinja2 import Template
from unidecode import unidecode


# ========================================================================= #
# Types                                                                     #
# ========================================================================= #
from kolr.color import Color
from kolr.util import util

ColorHex = str
ColorRgb = Tuple[int, int, int]

ListRgb = List[ColorRgb]
ListNames = List[str]

NamedColorHex = Tuple[str, ColorHex]
NamedColorRgb = Tuple[str, ColorRgb]

NamedColorHexList = List[NamedColorHex]
NamedColorRgbList = List[NamedColorRgb]

NameToColorHexDict = Dict[str, ColorHex]
NameToColorRgbDict = Dict[str, ColorRgb]

ColorHexDict = Dict[str, ColorHex]
ColorRgbDict = Dict[str, ColorRgb]


# ========================================================================= #
# Parent ColorPalettes                                                      #
# ========================================================================= #


_STR_TEMPLATE_SEPARATOR = "\n# {{'='*73}} #\n# {{name}}{{' '*(73-(name|length))}} #\n# {{'='*73}} #\n"
_STR_TEMPLATE_STRING_FIELDS = "{% for (field, value) in fields %}{{field}} = '{{value}}'\n{% endfor %}"
_STR_TEMPLATE_VAR_FIELDS = "{% for (field, value) in fields %}{{field}} = {{value}}\n{% endfor %}"
_STR_TEMPLATE_INIT_FILE = "{% for name in names %}import {{package}}.{{name}}\n{% endfor %}"


class ColorPalette(object):
    NAME = None

    def __init__(self, name_color_tuples, unique_colors=True):
        assert type(self.NAME) == str, 'Specify the name of the color palette'
        assert self.NAME == ColorPalette.standardised_name(self.NAME), 'Name must follow rules of python field'
        assert util.is_iterable(name_color_tuples), TypeError(f'Non-Iterable names: {type(name_color_tuples)}')
        # names
        self._names_orig = [name for name, _ in name_color_tuples]
        self._names, self._conflicts = ColorPalette.generate_unique_names(self._names_orig)
        # colors
        self._colors = [Color(color) for _, color in name_color_tuples]
        # sorted
        self._argsorted  = sorted(range(len(self._names)), key=self._names.__getitem__)
        self._name2index = {name: i for i, name in enumerate(self._names)}
        self._name2color = {name: color for name, color in zip(self._names, self._colors)}
        # validate
        ColorPalette._assert_names_unique_colors_unique(self._names, self._colors, ignore_colors=not unique_colors)

    def __len__(self):
        return len(self._names_orig)

    def __getitem__(self, item):
        # TODO global default get type
        if type(item) == int:
            return self._names[self._argsorted[item]]
        elif type(item) == str:
            return self._name2color[item]
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
    def generate_unique_names(orig_names: ListNames) -> Tuple[ListNames, Dict[str, Tuple[str, str, int]]]:
        names = [FileColorPalette.standardised_name(orig) for orig in orig_names]
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
    def _assert_names_unique_colors_unique(name_list: ListNames, color_list: List, ignore_colors=True):
        assert len(name_list), len(color_list)
        colors, names = {}, {}
        for name, color in zip(name_list, color_list):
            if name in names:
                raise KeyError(f'Names not unique for: "{name}" -> {color} / {names[name]}')
            names[name] = color
            if not ignore_colors and color in colors:
                raise KeyError(f'Colors not unique for: {color} -> "{name}" / {colors[color]}')
            colors[color] = name

    def generate_python(self, color_type='rgb'):
        return Template(f'{_STR_TEMPLATE_SEPARATOR}\n\n{_STR_TEMPLATE_STRING_FIELDS if color_type == "hex" else _STR_TEMPLATE_VAR_FIELDS}').render(
            fields=zip(self, (getattr(self[name], color_type) for name in self)),
            name=f'{self.NAME}: {color_type}'
        )

    def save_python(self, color_type='rgb'):
        os.makedirs(f'gen/{color_type}', exist_ok=True)
        util.overwrite_file(f'gen/rgb/{self.NAME}.py', self.generate_python(color_type=color_type))


class FileColorPalette(ColorPalette):
    URL = None

    def __init__(self):
        assert type(self.URL) == str, 'Specify the url of the color dataset'
        super().__init__(self._get_colors_from_data(util.fetch_url(self.URL)))

    def _get_colors_from_data(self, data: str) -> NamedColorRgbList:
        raise NotImplementedError('Override Me!')


# ========================================================================= #
# Color Palettes                                                            #
# ========================================================================= #


class ColorPaletteXkcd(FileColorPalette):
    URL = 'https://xkcd.com/color/rgb.txt'
    NAME = 'xkcd'

    def _get_colors_from_data(self, data: str) -> NamedColorHexList:
        import re
        pattern = re.compile('^(.+)\t(#[0-9abcdef]{6})')
        return [match for line in data.split('\n') for match in pattern.findall(line)]


class ColorPaletteMeodai(FileColorPalette):
    URL ='https://raw.githubusercontent.com/meodai/color-names/master/src/colornames.csv'
    NAME = 'meodai'

    def _get_colors_from_data(self, data: str) -> NamedColorHexList:
        import csv
        return [item for item in csv.reader(data.split('\n'))][1:]


class ColorPalette3Bit(ColorPalette):
    NAME = 'colors_3_bit'

    def __init__(self):
        from kolr.term.color_mapping import COLORS_3_BIT
        super().__init__(COLORS_3_BIT)


class ColorPalette4Bit(ColorPalette):
    NAME = 'colors_4_bit'

    def __init__(self):
        from kolr.term.color_mapping import COLORS_4_BIT
        super().__init__(COLORS_4_BIT)


class ColorPalette8Bit(ColorPalette):
    NAME = 'colors_8_bit'

    def __init__(self):
        from kolr.term.color_mapping import COLORS_8_BIT
        super().__init__(COLORS_8_BIT, unique_colors=False)


class ColorPalette8BitWikipedia(ColorPalette):
    NAME = 'colors_8_bit_wikipedia'

    def __init__(self):
        from kolr.term.color_mapping import COLORS_8_BIT_WIKIPEDIA
        super().__init__(COLORS_8_BIT_WIKIPEDIA, unique_colors=False)



# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    COLORS_3_BIT = ColorPalette3Bit()
    COLORS_4_BIT = ColorPalette4Bit()
    COLORS_8_BIT = ColorPalette8Bit()
    COLORS_8_BIT_WIKIPEDIA = ColorPalette8BitWikipedia()
    COLORS_XKCD = ColorPaletteXkcd()
    COLOR_MEODIA = ColorPaletteMeodai()

    print(COLORS_8_BIT.generate_python('rgb'))
    print(COLORS_8_BIT_WIKIPEDIA.generate_python('hex'))


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
