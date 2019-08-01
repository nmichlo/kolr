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


# ========================================================================= #
# Kolr Builder                                                              #
# ========================================================================= #
from kolr.palette import COLOR_PALETTE_MEODAI
from kolr.term import detect_color


class Kolr(object):

    def __init__(self, *vals, style=None):
        self._stack = []
        self._style(*vals, style=style)

    def __str__(self) -> str:
        return ''.join((f'{c}{s}\033[0m' if c else s) for c, s in self._stack)
    def __repr__(self) -> str:
        return str(self)

    def __add__(self, val): return self._style(val, is_left=False)
    def __radd__(self, val): return self._style(val, is_left=True)

    def __call__(self, *vals, style=None):
        return self._style(*vals, style=style)

    def _normalise_style(self, style=None):
        clr = ''
        if style:
            if style in COLOR_PALETTE_MEODAI:
                # TODO fix for bg
                clr = COLOR_PALETTE_MEODAI[style].fg24
        return clr

    def _style(self, *vals, style=None, is_left=False):
        if not vals:
            return self  # chainable
        clr = self._normalise_style(style)
        append_stack = []
        for val in vals:
            typ = type(val)
            if typ == str:
                append_stack.append((clr, val))
            elif typ == Kolr:
                if clr:
                    for c, v in val._stack:
                        append_stack.append((clr+c, v))
                else:
                    append_stack = val._stack
            else:
                raise TypeError(f'Invalid Type: {typ}')
        # merge
        self._stack = (append_stack + self._stack) if is_left else (self._stack + append_stack)
        return self  # chainable


# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    print(Kolr('left ' + ' right' + 'fdsa', style='green'))
    print(str(Kolr('left ' + Kolr('inner', style='red')('asdf', style='reset') + ' right', style='green')))

# ========================================================================= #
# END                                                                       #
# ========================================================================= #
