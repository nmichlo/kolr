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


from kolr.term.escape_codes.sgr import fg_select, bg_select


# ========================================================================= #
# SGR COLORS - 8 BIT                                                        #
# ∙   0->  7: standard colors (as in ESC [ 30–37 m)                         #
# ∙   8-> 15: high intensity colors (as in ESC [ 90–97 m)                   #
# ∙  16->231: 6×6×6 cube (216 colors): 16 + 36*r + 6*g + b (0<=r, g, b<=5)  #
#             0=0x00, 95=0x5F, 135=0x87, 175=0xAF, 215=0xD7, 255=0xFF       #
# ∙ 232->255: grayscale from black to white in 24 steps (3% to 97%)         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit                    #
# ∙ https://github.com/sindresorhus/xterm-colors                            #
# ∙ https://gist.github.com/jasonm23/2868981                                #
# ========================================================================= #


def fg(n):
    assert type(n) == int
    return fg_select(n)


def bg(n):
    assert type(n) == int
    return bg_select(n)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
