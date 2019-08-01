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


from kolr.term.escape_codes.csi import sgr


# ========================================================================= #
# SGR COLORS - 3/4 BIT                                                      #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit                  #
# ========================================================================= #


_FG_CODES = [sgr(i) for i in range(30, 38)] + [sgr(i) for i in range(90, 98)]
_BG_CODES = [sgr(i) for i in range(40, 48)] + [sgr(i) for i in range(100, 108)]


def fg(n):
    return _FG_CODES[n]


def bg(n):
    return _FG_CODES[n]


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


# C3_black   = COLORS_3_BIT + Color3Or4Bit(name='Black',          fg_code=30, bg_code=40,  colors=TermColors(vga=(0, 0, 0),       windows_console=(0, 0, 0),       windows_powershell=(0, 0, 0),       windows_10_consolepowershell_6=(12, 12, 12),    terminal_app=(0, 0, 0),       putty=(0, 0, 0),       mirc=(0, 0, 0),       xterm=(0, 0, 0),       x=(0, 0, 0),       ubuntu=(1, 1, 1)      ))
# C3_red     = COLORS_3_BIT + Color3Or4Bit(name='Red',            fg_code=31, bg_code=41,  colors=TermColors(vga=(170, 0, 0),     windows_console=(128, 0, 0),     windows_powershell=(128, 0, 0),     windows_10_consolepowershell_6=(197, 15, 31),   terminal_app=(194, 54, 33),   putty=(187, 0, 0),     mirc=(127, 0, 0),     xterm=(205, 0, 0),     x=(255, 0, 0),     ubuntu=(222, 56, 43)  ))
# C3_green   = COLORS_3_BIT + Color3Or4Bit(name='Green',          fg_code=32, bg_code=42,  colors=TermColors(vga=(0, 170, 0),     windows_console=(0, 128, 0),     windows_powershell=(0, 128, 0),     windows_10_consolepowershell_6=(19, 161, 14),   terminal_app=(37, 188, 36),   putty=(0, 187, 0),     mirc=(0, 147, 0),     xterm=(0, 205, 0),     x=(0, 255, 0),     ubuntu=(57, 181, 74)  ))
# C3_yellow  = COLORS_3_BIT + Color3Or4Bit(name='Yellow',         fg_code=33, bg_code=43,  colors=TermColors(vga=(170, 85, 0),    windows_console=(128, 128, 0),   windows_powershell=(238, 237, 240), windows_10_consolepowershell_6=(193, 156, 0),   terminal_app=(173, 173, 39),  putty=(187, 187, 0),   mirc=(252, 127, 0),   xterm=(205, 205, 0),   x=(255, 255, 0),   ubuntu=(255, 199, 6)  ))
# C3_blue    = COLORS_3_BIT + Color3Or4Bit(name='Blue',           fg_code=34, bg_code=44,  colors=TermColors(vga=(0, 0, 170),     windows_console=(0, 0, 128),     windows_powershell=(0, 0, 128),     windows_10_consolepowershell_6=(0, 55, 218),    terminal_app=(73, 46, 225),   putty=(0, 0, 187),     mirc=(0, 0, 127),     xterm=(0, 0, 238),     x=(0, 0, 255),     ubuntu=(0, 111, 184)  ))
# C3_magenta = COLORS_3_BIT + Color3Or4Bit(name='Magenta',        fg_code=35, bg_code=45,  colors=TermColors(vga=(170, 0, 170),   windows_console=(128, 0, 128),   windows_powershell=(1, 36, 86),     windows_10_consolepowershell_6=(136, 23, 152),  terminal_app=(211, 56, 211),  putty=(187, 0, 187),   mirc=(156, 0, 156),   xterm=(205, 0, 205),   x=(255, 0, 255),   ubuntu=(118, 38, 113) ))
# C3_cyan    = COLORS_3_BIT + Color3Or4Bit(name='Cyan',           fg_code=36, bg_code=46,  colors=TermColors(vga=(0, 170, 170),   windows_console=(0, 128, 128),   windows_powershell=(0, 128, 128),   windows_10_consolepowershell_6=(58, 150, 221),  terminal_app=(51, 187, 200),  putty=(0, 187, 187),   mirc=(0, 147, 147),   xterm=(0, 205, 205),   x=(0, 255, 255),   ubuntu=(44, 181, 233) ))
# C3_white   = COLORS_3_BIT + Color3Or4Bit(name='White',          fg_code=37, bg_code=47,  colors=TermColors(vga=(170, 170, 170), windows_console=(192, 192, 192), windows_powershell=(192, 192, 192), windows_10_consolepowershell_6=(204, 204, 204), terminal_app=(203, 204, 205), putty=(187, 187, 187), mirc=(210, 210, 210), xterm=(229, 229, 229), x=(255, 255, 255), ubuntu=(204, 204, 204)))

# C4_bright_black   = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Black',   fg_code=90, bg_code=100, colors=TermColors(vga=(85, 85, 85),    windows_console=(128, 128, 128), windows_powershell=(128, 128, 128), windows_10_consolepowershell_6=(118, 118, 118), terminal_app=(129, 131, 131), putty=(85, 85, 85),    mirc=(127, 127, 127), xterm=(127, 127, 127), x=None,              ubuntu=(128, 128, 128)))
# C4_bright_red     = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Red',     fg_code=91, bg_code=101, colors=TermColors(vga=(255, 85, 85),   windows_console=(255, 0, 0),     windows_powershell=(255, 0, 0),     windows_10_consolepowershell_6=(231, 72, 86),   terminal_app=(252, 57, 31),   putty=(255, 85, 85),   mirc=(255, 0, 0),     xterm=(255, 0, 0),     x=None,              ubuntu=(255, 0, 0)    ))
# C4_bright_green   = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Green',   fg_code=92, bg_code=102, colors=TermColors(vga=(85, 255, 85),   windows_console=(0, 255, 0),     windows_powershell=(0, 255, 0),     windows_10_consolepowershell_6=(22, 198, 12),   terminal_app=(49, 231, 34),   putty=(85, 255, 85),   mirc=(0, 252, 0),     xterm=(0, 255, 0),     x=(144, 238, 144),   ubuntu=(0, 255, 0)    ))
# C4_bright_yellow  = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Yellow',  fg_code=93, bg_code=103, colors=TermColors(vga=(255, 255, 85),  windows_console=(255, 255, 0),   windows_powershell=(255, 255, 0),   windows_10_consolepowershell_6=(249, 241, 165), terminal_app=(234, 236, 35),  putty=(255, 255, 85),  mirc=(255, 255, 0),   xterm=(255, 255, 0),   x=(255, 255, 224),   ubuntu=(255, 255, 0)  ))
# C4_bright_blue    = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Blue',    fg_code=94, bg_code=104, colors=TermColors(vga=(85, 85, 255),   windows_console=(0, 0, 255),     windows_powershell=(0, 0, 255),     windows_10_consolepowershell_6=(59, 120, 255),  terminal_app=(88, 51, 255),   putty=(85, 85, 255),   mirc=(0, 0, 252),     xterm=(92, 92, 255),   x=(173, 216, 230),   ubuntu=(0, 0, 255)    ))
# C4_bright_magenta = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Magenta', fg_code=95, bg_code=105, colors=TermColors(vga=(255, 85, 255),  windows_console=(255, 0, 255),   windows_powershell=(255, 0, 255),   windows_10_consolepowershell_6=(180, 0, 158),   terminal_app=(249, 53, 248),  putty=(255, 85, 255),  mirc=(255, 0, 255),   xterm=(255, 0, 255),   x=None,              ubuntu=(255, 0, 255)  ))
# C4_bright_cyan    = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright Cyan',    fg_code=96, bg_code=106, colors=TermColors(vga=(85, 255, 255),  windows_console=(0, 255, 255),   windows_powershell=(0, 255, 255),   windows_10_consolepowershell_6=(97, 214, 214),  terminal_app=(20, 240, 240),  putty=(85, 255, 255),  mirc=(0, 255, 255),   xterm=(0, 255, 255),   x=(224, 255, 255),   ubuntu=(0, 255, 255)  ))
# C4_bright_white   = COLORS_4_BIT_EXTENSION + Color3Or4Bit(name='Bright White',   fg_code=97, bg_code=107, colors=TermColors(vga=(255, 255, 255), windows_console=(255, 255, 255), windows_powershell=(255, 255, 255), windows_10_consolepowershell_6=(242, 242, 242), terminal_app=(233, 235, 235), putty=(255, 255, 255), mirc=(255, 255, 255), xterm=(255, 255, 255), x=None,              ubuntu=(255, 255, 255)))
