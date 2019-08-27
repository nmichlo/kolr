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


from typing import Union


# ========================================================================= #
# XTerm Control Sequences from invisible-island.net as pythonic code.
# Basic control sequences are string variables.
#   - eg: ESC = '\033'
#         CSI = ESC + '['
# Control sequences that have args can be called to return a string.
#   - eg: sgr = CSI + Ps + 'm'
#         sgr(0) == '\033[0m' == sgr.RESET
# ========================================================================= #


class _Param(object):
    def __init__(self, validator=None, formatter=None):
        assert validator is None or callable(validator)
        assert formatter is None or callable(formatter)
        self._validator = validator
        self._formatter = formatter

    def __call__(self, value):
        if self._validator:
            assert self._validator(value)
        if self._formatter:
            value = self._formatter(value)
        return str(value)

    @staticmethod
    def _allow_wrap(allowed=None, validator=None):
        if not allowed:
            return None if not validator else validator
        else:
            allowed = set(allowed)
            return (lambda x: x in allowed) if not validator else (lambda x: validator(x) and x in allowed)

    def __getitem__(self, item):
        assert isinstance(item, (tuple, list, set))
        return _Param(self._allow_wrap(item, self._validator), self._formatter)

    def __add__(self, other: Union[str, '_Param', '_Builder']):
        return _Builder(self).__add__(other)
    def __radd__(self, other: Union[str, '_Param', '_Builder']):
        return _Builder(self).__radd__(other)

    def __str__(self):
        return f'({self._validator}, {self._formatter})'
    def __repr__(self):
        return str(self)


class _Builder(object):
    def __init__(self, *items):
        assert all(isinstance(item, (str, _Param)) for item in items)
        self._items = list(items)

    def __call__(self, *args):
        i, buf = 0, []
        try:
            pass
            for item in self._items:
                if isinstance(item, _Param):
                    item, i = item(args[i]), i + 1
                buf.append(str(item))
        except IndexError as e:
            raise ValueError(f'Too few args, given: {len(args)}, required: {sum(isinstance(item, _Param) for item in self._items)}')
        if i < len(args):
            raise ValueError(f'Too many args, given: {len(args)}, required: {sum(isinstance(item, _Param) for item in self._items)}')
        return ''.join(buf)

    def _add(self, item, is_right=True):
        assert isinstance(item, (str, _Param, _Builder))
        if isinstance(item, _Builder):
            items = item._items[:]
        else:
            items = [item]
        new = _Builder()
        new._items = (self._items + items) if is_right else (items + self._items)
        return new

    def __add__(self, other):
        # self + other
        return self._add(other, is_right=True)
    def __radd__(self, other):
        # other + self
        return self._add(other, is_right=False)

    def __str__(self):
        return str(self._items)
    def __repr__(self):
        return str(self)


class ParamMeta(type):
    def __new__(cls, *args, **kwargs):
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        return getattr(cls, f'_{cls.__name__}__seq')(*args, **kwargs)


# ========================================================================= #
# Definitions                                                               #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
# Comments are from https://invisible-island.net/xterm/ctlseqs/ctlseqs.html #
# Only non-comment code is from Nathan Michlo                               #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#                         XTerm Control Sequences                           #
#                                                                           #
#                                Edward Moy                                 #
#                    University of California, Berkeley                     #
#                                                                           #
#                                Revised by                                 #
#                                                                           #
#                              Stephen Gildea                               #
#                           X Consortium (1994)                             #
#                                                                           #
#                              Thomas Dickey                                #
#                       XFree86 Project (1996-2006)                         #
#                     invisible-island.net (2006-2019)                      #
#                updated for XTerm Patch #348 (2019/07/11)                  #
# ========================================================================= #


# c    The literal character c.

c = 'c'

# C    A single (required) character.

C = _Param(
    validator=lambda x: type(x) == str and (len(x) == 1 or len(x) == 2),
    formatter=None
)

# Ps   A single (usually optional) numeric parameter, composed of one or more digits.

Ps = _Param(
    validator=lambda x: (x is None) or (int(x) >= 0),
    formatter=lambda x: '' if (x is None) else x
)

# Pm   A multiple numeric parameter composed of any number of single
#      numeric parameters, separated by ;  character(s).  Individual val-
#      ues for the parameters are listed with Ps .

Pm = _Param(
    validator=lambda x: all(Ps._validator(a) for a in x),
    formatter=lambda x: ';'.join(str(a) for a in x)
)

# Pt   A text parameter composed of printable characters.

Pt = _Param(
    validator=lambda x: type(x) == str and all(ord(a) < 128 for a in x),
    formatter=None
)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
