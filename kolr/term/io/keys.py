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


from typing import NamedTuple, Tuple, Any
import unicodedata


# ========================================================================= #
# KEYS                                                                      #
# ========================================================================= #


class AnyKey(object):
    def __init__(self, name: str, data: Any):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    def __str__(self):
        return str((self.name, self.data))

    def __repr__(self):
        return f'{self.__class__.__name__}{(self.name, self.data)}'


class Key(AnyKey):
    def __init__(self, name: str, data: str):
        super().__init__(name, data)

    @property
    def long_name(self):
        return Key.char2name(self.data)

    @staticmethod
    def char2name(char):
        try:
            name = unicodedata.name(char)
            return name.lower().replace(' ', '_')  # some names contain hyphens in weird places
        except:
            return None

    @staticmethod
    def name2char(name):
        try:
            name = name.upper().replace('_', ' ')
            return unicodedata.lookup(name)
        except:
            return None


class MouseKey(AnyKey):
    def __init__(self, name: str, data: Tuple[int, int]):
        super().__init__(name, data)

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @property
    def pos(self):
        return self.data


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
