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


from typing import Tuple, NamedTuple
from collections import namedtuple


# ========================================================================= #
# Escape Character                                                          #
# ∙ octal=\033 ∙ hex=\x1B ∙ decimal=27 ∙ keyboard=^[                        #
# ========================================================================= #

# C1 (8-Bit) Control Characters
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
_CtrlChar = namedtuple('ControlCharacter', ('bits7', 'bits8', 'name', 'lname', 'note'))
IND   = _CtrlChar(bits7=ESC + 'D',  bits8='\x84', name='IND',   lname='Index',                                          note="")
NEL   = _CtrlChar(bits7=ESC + 'E',  bits8='\x85', name='NEL',   lname='Next Line',                                      note="")
HTS   = _CtrlChar(bits7=ESC + 'H',  bits8='\x88', name='HTS',   lname='Tab Set',                                        note="")
RI    = _CtrlChar(bits7=ESC + 'M',  bits8='\x8d', name='RI',    lname='Reverse Index',                                  note="")
SS2   = _CtrlChar(bits7=ESC + 'N',  bits8='\x8e', name='SS2',   lname='Single Shift Select of G2 Character Set, VT220', note="This affects next character only.")
SS3   = _CtrlChar(bits7=ESC + 'O',  bits8='\x8f', name='SS3',   lname='Single Shift Select of G3 Character Set, VT220', note="This affects next character only.")
DCS   = _CtrlChar(bits7=ESC + 'P',  bits8='\x90', name='DCS',   lname='Device Control String',                          note="")
SPA   = _CtrlChar(bits7=ESC + 'V',  bits8='\x96', name='SPA',   lname='Start of Guarded Area',                          note="")
EPA   = _CtrlChar(bits7=ESC + 'W',  bits8='\x97', name='EPA',   lname='End of Guarded Area',                            note="")
SOS   = _CtrlChar(bits7=ESC + 'X',  bits8='\x98', name='SOS',   lname='Start of String',                                note="")
DECID = _CtrlChar(bits7=ESC + 'Z',  bits8='\x9a', name='DECID', lname='Return Terminal ID',                             note="Obsolete form of CSI c (DA).")
CSI   = _CtrlChar(bits7=ESC + '[',  bits8='\x9b', name='CSI',   lname='Control Sequence Introducer',                    note="")
ST    = _CtrlChar(bits7=ESC + '\\', bits8='\x9c', name='ST',    lname='String Terminator',                              note="")
OSC   = _CtrlChar(bits7=ESC + ']',  bits8='\x9d', name='OSC',   lname='Operating System Command',                       note="")
PM    = _CtrlChar(bits7=ESC + '^',  bits8='\x9e', name='PM',    lname='Privacy Message',                                note="")
APC   = _CtrlChar(bits7=ESC + '_',  bits8='\x9f', name='APC',   lname='Application Program Command',                    note="")

ESC = '\033'
# # https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Single-character-functions
_SingleCharFunc = namedtuple('ControlCharacter', ('name', 'code', 'desc'))
BEL = _SingleCharFunc(name='BEL', code='Ctrl-G', desc="Bell (Ctrl-G).")
BS  = _SingleCharFunc(name='BS',  code='Ctrl-H', desc="Backspace (Ctrl-H).")
CR  = _SingleCharFunc(name='CR',  code='Ctrl-M', desc="Carriage Return (Ctrl-M).")
ENQ = _SingleCharFunc(name='ENQ', code='Ctrl-E', desc="Return Terminal Status (Ctrl-E).  Default response is an empty string, but may be overridden by a resource answerbackString.")
FF  = _SingleCharFunc(name='FF',  code='Ctrl-L', desc="Form Feed or New Page (NP).  (FF  is Ctrl-L).  FF  is treated the same as LF .")
LF  = _SingleCharFunc(name='LF',  code='Ctrl-J', desc="Line Feed or New Line (NL).  (LF  is Ctrl-J).")
SI  = _SingleCharFunc(name='SI',  code='Ctrl-O', desc="Switch to Standard Character Set (Ctrl-O is Shift In or LS0). This invokes the G0 character set (the default) as GL. VT200 and up implement LS0.")
SO  = _SingleCharFunc(name='SO',  code='Ctrl-N', desc="Switch to Alternate Character Set (Ctrl-N is Shift Out or LS1).  This invokes the G1 character set as GL. VT200 and up implement LS1.")
SP  = _SingleCharFunc(name='SP',  code='Space',  desc="Space.")
TAB = _SingleCharFunc(name='TAB', code='Ctrl-I', desc="Horizontal Tab (HT) (Ctrl-I).")
VT  = _SingleCharFunc(name='VT',  code='Ctrl-K', desc="Vertical Tab (Ctrl-K).  This is treated the same as LF.")


# ========================================================================= #
# Escape sequences                                                          #
# ∙ ESC ...                                                                 #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences         #
# ========================================================================= #




CSI = ESC + '['


# ========================================================================= #
# CSI SEQUENCES (Control Sequence Introducer)                               #
# ∙ CSI = ESC [ ...                                                         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences            #
# ========================================================================= #




SGR = CSI + '{code}m'


# ========================================================================= #
# SGR PARAMETERS (Select Graphic Rendition)                                 #
# ∙ SGR = CSI ... m                                                         #
# ∙ https://stackoverflow.com/questions/4842424                             #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters           #
# ========================================================================= #


_SgrParam = namedtuple('SgrParamter', ['code', 'type', 'name', 'desc', 'note'])

# Types
SGR_TYPE_STYLE = 'style'
SGR_TYPE_RESET = 'reset'
SGR_TYPE_COLOR = 'color'
SGR_TYPE_COLOR_SEL = 'color_selector'
SGR_TYPES = tuple([SGR_TYPE_STYLE, SGR_TYPE_RESET, SGR_TYPE_COLOR, SGR_TYPE_COLOR_SEL])

# Colors
_3BIT_COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# Generators
_SGR_PARAMETERS_ALT_FONTS = [_SgrParam(code=i, type=SGR_TYPE_STYLE, name=f'font_alt_{i - 10}', desc=f'Select alternate font: {i - 10}', note=None) for i in range(11, 20)]
_SGR_PARAMETERS_FG_COLORS = [_SgrParam(code=i, type=SGR_TYPE_COLOR, name=f'fg_{_3BIT_COLORS[i - 30]}', desc=f'Set foreground color: {_3BIT_COLORS[i - 30]}', note='See 3bit colors') for i in range(30, 38)]
_SGR_PARAMETERS_BG_COLORS = [_SgrParam(code=i, type=SGR_TYPE_COLOR, name=f'bg_{_3BIT_COLORS[i - 40]}', desc=f'Set background color: {_3BIT_COLORS[i - 40]}', note='See 3bit colors') for i in range(40, 48)]
_SGR_PARAMETERS_FG_COLORS_BRIGHT = [_SgrParam(code=i, type=SGR_TYPE_COLOR, name=f'fg_bright_{_3BIT_COLORS[i - 90]}', desc=f'Set bright foreground color: {_3BIT_COLORS[i - 90]}', note='See 3bit colors. aixterm (not in standard)') for i in range(90, 98)]
_SGR_PARAMETERS_BG_COLORS_BRIGHT = [_SgrParam(code=i, type=SGR_TYPE_COLOR, name=f'bg_bright_{_3BIT_COLORS[i - 100]}', desc=f'Set bright background color: {_3BIT_COLORS[i - 100]}', note='See 3bit colors. aixterm (not in standard)') for i in range(100, 108)]

# Info List
SGR_PARAM_LIST = [
    _SgrParam(code=0, type=SGR_TYPE_RESET, name='reset', desc='Reset / Normal', note='All attributes off.'),
    _SgrParam(code=1, type=SGR_TYPE_STYLE, name='bold', desc='Bold or increased intensity', note=None),
    _SgrParam(code=2, type=SGR_TYPE_STYLE, name='faint', desc='Faint (decreased intensity)', note='Not widely supported.'),
    _SgrParam(code=3, type=SGR_TYPE_STYLE, name='italic', desc='Italic', note='Not widely supported. Sometimes treated as inverse.'),
    _SgrParam(code=4, type=SGR_TYPE_STYLE, name='underline', desc='Underline', note=None),
    _SgrParam(code=5, type=SGR_TYPE_STYLE, name='blink', desc='Slow Blink', note='Less than 150 blinks per minute'),
    _SgrParam(code=6, type=SGR_TYPE_STYLE, name='blink_rapid', desc='Rapid Blink', note='MS-DOS ANSI.SYS; 150+ blicks per minute. Not widely supported'),
    _SgrParam(code=7, type=SGR_TYPE_STYLE, name='invert', desc='[[reverse video]]', note='Swap foreground and background colors'),
    _SgrParam(code=8, type=SGR_TYPE_STYLE, name='conceal', desc='Conceal', note='Not widely supported.'),
    _SgrParam(code=9, type=SGR_TYPE_STYLE, name='strikethrough', desc='Crossed-out', note='Characters legible, but marked for deletion.  Not widely supported.'),
    _SgrParam(code=10, type=SGR_TYPE_STYLE, name='font_primary', desc='Primary(default) font', note=None),
    *_SGR_PARAMETERS_ALT_FONTS, # 11-19 Alternate Font
    _SgrParam(code=20, type=SGR_TYPE_STYLE, name='franktur', desc='Fraktur', note='Latin calligraphic hand. Hardly ever supported.'),  # https://en.wikipedia.org/wiki/Fraktur # might instead be reset_style (not color)
    _SgrParam(code=21, type=SGR_TYPE_RESET, name='reset_bold', desc='Bold off or Double Underline', note='Bold off not widely supported; double underline hardly ever supported.'),
    _SgrParam(code=22, type=SGR_TYPE_RESET, name='reset_intensity', desc='Normal color or intensity', note='Neither bold nor faint.'),
    _SgrParam(code=23, type=SGR_TYPE_RESET, name='reset_italic', desc='Not italic, not Fraktur', note=None),
    _SgrParam(code=24, type=SGR_TYPE_RESET, name='reset_underline', desc='Underline off', note='Not singly or doubly underlined.'),
    _SgrParam(code=25, type=SGR_TYPE_RESET, name='reset_blink', desc='Blink off', note=None),
    # 26 <reset blink fast?>
    _SgrParam(code=27, type=SGR_TYPE_RESET, name='reset_inverse', desc='Inverse off', note=None),
    _SgrParam(code=28, type=SGR_TYPE_RESET, name='reset_conceal', desc='Reveal', note='Conceal off.'),
    _SgrParam(code=29, type=SGR_TYPE_RESET, name='reset_strikethrough', desc='Not crossed out', note=None),
    *_SGR_PARAMETERS_FG_COLORS, # 30-37 Set foreground color
    _SgrParam(code=38, type=SGR_TYPE_COLOR_SEL, name='fg_select', desc='Set general foreground color', note='Next arguments are `5;n` or `2;r;g;b`, see below.'),
    _SgrParam(code=39, type=SGR_TYPE_RESET, name='reset_fg', desc='Default foreground color', note='Implementation defined (according to standard).'),
    *_SGR_PARAMETERS_BG_COLORS, # 40-47 Set background color
    _SgrParam(code=48, type=SGR_TYPE_COLOR_SEL, name='bg_select', desc='Set general background color', note='Next arguments are `5;n` or `2;r;g;b`, see 8bit and 24bit.'),
    _SgrParam(code=49, type=SGR_TYPE_RESET, name='reset_bg', desc='Default background color', note='Implementation defined (according to standard)'),
    # 50 <unused>
    _SgrParam(code=51, type=SGR_TYPE_STYLE, name='frame', desc='Framed', note=None),
    _SgrParam(code=52, type=SGR_TYPE_STYLE, name='encircle', desc='Encircled', note=None),
    _SgrParam(code=53, type=SGR_TYPE_STYLE, name='overline', desc='Overlined', note=None),
    _SgrParam(code=54, type=SGR_TYPE_RESET, name='reset_frame', desc='Not framed or encircled', note=None),
    _SgrParam(code=55, type=SGR_TYPE_RESET, name='reset_overline', desc='Not overlined', note=None),
    # 56-59 <unused>
    _SgrParam(code=60, type=SGR_TYPE_STYLE, name='ideogram_underline', desc='ideogram underline', note='Hardly ever supported.'),
    _SgrParam(code=61, type=SGR_TYPE_STYLE, name='ideogram_double_underline', desc='ideogram double underline', note='Hardly ever supported.'),
    _SgrParam(code=62, type=SGR_TYPE_STYLE, name='ideogram_overline', desc='ideogram overline', note='Hardly ever supported.'),
    _SgrParam(code=63, type=SGR_TYPE_STYLE, name='ideogram_double_overline', desc='ideogram double overline', note='Hardly ever supported.'),
    _SgrParam(code=64, type=SGR_TYPE_STYLE, name='ideogram_stress', desc='ideogram stress marking', note='Hardly ever supported.'),
    _SgrParam(code=65, type=SGR_TYPE_RESET, name='reset_ideogram', desc='ideogram attributes off', note='Reset the effects of all of 60-64.'),
    # 66-89 <unused>
    *_SGR_PARAMETERS_FG_COLORS_BRIGHT,  # 90-97 Set bright foreground color
    # 98-99 <unused>
    *_SGR_PARAMETERS_BG_COLORS_BRIGHT,  # 100-107 Set bright background color
]

# Info Dicts
NAME_TO_SGR = {}
CODE_TO_SGR = {}
TYPE_TO_SGRS = {}

# Fill Dicts
for sgr in SGR_PARAM_LIST:
    if sgr.name in NAME_TO_SGR: raise KeyError(f'Duplicate Keys Found: {sgr.name}')
    NAME_TO_SGR[sgr.name] = sgr
    if sgr.code in CODE_TO_SGR: raise KeyError(f'Duplicate Keys Found: {sgr.name}')
    CODE_TO_SGR[sgr.code] = sgr
    if sgr.type not in TYPE_TO_SGRS: TYPE_TO_SGRS[sgr.type] = []
    TYPE_TO_SGRS[sgr.type].append(sgr)


# ========================================================================= #
# SGR COLORS                                                                #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#Colors                   #
# ========================================================================= #


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# 3/4 BIT                                                                   #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# TYPES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


RgbColor = Tuple[int, int, int]
HslColor = Tuple[float, int, int]


class TermColors(NamedTuple):
    vga: RgbColor
    windows_console: RgbColor
    windows_powershell: RgbColor
    windows_10_consolepowershell_6: RgbColor
    terminal_app: RgbColor
    putty: RgbColor
    mirc: RgbColor
    xterm: RgbColor
    x: RgbColor
    ubuntu: RgbColor


class Color3Or4Bit(NamedTuple):
    name: str
    fg_code: int
    bg_code: int
    colors: TermColors


# VARS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


COLORS_3_BIT = (
    Color3Or4Bit(name='Black',          fg_code=30, bg_code=40,  colors=TermColors(vga=(0, 0, 0),       windows_console=(0, 0, 0),       windows_powershell=(0, 0, 0),       windows_10_consolepowershell_6=(12, 12, 12),    terminal_app=(0, 0, 0),       putty=(0, 0, 0),       mirc=(0, 0, 0),       xterm=(0, 0, 0),       x=(0, 0, 0),       ubuntu=(1, 1, 1)      )),
    Color3Or4Bit(name='Red',            fg_code=31, bg_code=41,  colors=TermColors(vga=(170, 0, 0),     windows_console=(128, 0, 0),     windows_powershell=(128, 0, 0),     windows_10_consolepowershell_6=(197, 15, 31),   terminal_app=(194, 54, 33),   putty=(187, 0, 0),     mirc=(127, 0, 0),     xterm=(205, 0, 0),     x=(255, 0, 0),     ubuntu=(222, 56, 43)  )),
    Color3Or4Bit(name='Green',          fg_code=32, bg_code=42,  colors=TermColors(vga=(0, 170, 0),     windows_console=(0, 128, 0),     windows_powershell=(0, 128, 0),     windows_10_consolepowershell_6=(19, 161, 14),   terminal_app=(37, 188, 36),   putty=(0, 187, 0),     mirc=(0, 147, 0),     xterm=(0, 205, 0),     x=(0, 255, 0),     ubuntu=(57, 181, 74)  )),
    Color3Or4Bit(name='Yellow',         fg_code=33, bg_code=43,  colors=TermColors(vga=(170, 85, 0),    windows_console=(128, 128, 0),   windows_powershell=(238, 237, 240), windows_10_consolepowershell_6=(193, 156, 0),   terminal_app=(173, 173, 39),  putty=(187, 187, 0),   mirc=(252, 127, 0),   xterm=(205, 205, 0),   x=(255, 255, 0),   ubuntu=(255, 199, 6)  )),
    Color3Or4Bit(name='Blue',           fg_code=34, bg_code=44,  colors=TermColors(vga=(0, 0, 170),     windows_console=(0, 0, 128),     windows_powershell=(0, 0, 128),     windows_10_consolepowershell_6=(0, 55, 218),    terminal_app=(73, 46, 225),   putty=(0, 0, 187),     mirc=(0, 0, 127),     xterm=(0, 0, 238),     x=(0, 0, 255),     ubuntu=(0, 111, 184)  )),
    Color3Or4Bit(name='Magenta',        fg_code=35, bg_code=45,  colors=TermColors(vga=(170, 0, 170),   windows_console=(128, 0, 128),   windows_powershell=(1, 36, 86),     windows_10_consolepowershell_6=(136, 23, 152),  terminal_app=(211, 56, 211),  putty=(187, 0, 187),   mirc=(156, 0, 156),   xterm=(205, 0, 205),   x=(255, 0, 255),   ubuntu=(118, 38, 113) )),
    Color3Or4Bit(name='Cyan',           fg_code=36, bg_code=46,  colors=TermColors(vga=(0, 170, 170),   windows_console=(0, 128, 128),   windows_powershell=(0, 128, 128),   windows_10_consolepowershell_6=(58, 150, 221),  terminal_app=(51, 187, 200),  putty=(0, 187, 187),   mirc=(0, 147, 147),   xterm=(0, 205, 205),   x=(0, 255, 255),   ubuntu=(44, 181, 233) )),
    Color3Or4Bit(name='White',          fg_code=37, bg_code=47,  colors=TermColors(vga=(170, 170, 170), windows_console=(192, 192, 192), windows_powershell=(192, 192, 192), windows_10_consolepowershell_6=(204, 204, 204), terminal_app=(203, 204, 205), putty=(187, 187, 187), mirc=(210, 210, 210), xterm=(229, 229, 229), x=(255, 255, 255), ubuntu=(204, 204, 204))),
)

COLORS_4_BIT_EXTENSION = (
    Color3Or4Bit(name='Bright Black',   fg_code=90, bg_code=100, colors=TermColors(vga=(85, 85, 85),    windows_console=(128, 128, 128), windows_powershell=(128, 128, 128), windows_10_consolepowershell_6=(118, 118, 118), terminal_app=(129, 131, 131), putty=(85, 85, 85),    mirc=(127, 127, 127), xterm=(127, 127, 127), x=None,              ubuntu=(128, 128, 128))),
    Color3Or4Bit(name='Bright Red',     fg_code=91, bg_code=101, colors=TermColors(vga=(255, 85, 85),   windows_console=(255, 0, 0),     windows_powershell=(255, 0, 0),     windows_10_consolepowershell_6=(231, 72, 86),   terminal_app=(252, 57, 31),   putty=(255, 85, 85),   mirc=(255, 0, 0),     xterm=(255, 0, 0),     x=None,              ubuntu=(255, 0, 0)    )),
    Color3Or4Bit(name='Bright Green',   fg_code=92, bg_code=102, colors=TermColors(vga=(85, 255, 85),   windows_console=(0, 255, 0),     windows_powershell=(0, 255, 0),     windows_10_consolepowershell_6=(22, 198, 12),   terminal_app=(49, 231, 34),   putty=(85, 255, 85),   mirc=(0, 252, 0),     xterm=(0, 255, 0),     x=(144, 238, 144),   ubuntu=(0, 255, 0)    )),
    Color3Or4Bit(name='Bright Yellow',  fg_code=93, bg_code=103, colors=TermColors(vga=(255, 255, 85),  windows_console=(255, 255, 0),   windows_powershell=(255, 255, 0),   windows_10_consolepowershell_6=(249, 241, 165), terminal_app=(234, 236, 35),  putty=(255, 255, 85),  mirc=(255, 255, 0),   xterm=(255, 255, 0),   x=(255, 255, 224),   ubuntu=(255, 255, 0)  )),
    Color3Or4Bit(name='Bright Blue',    fg_code=94, bg_code=104, colors=TermColors(vga=(85, 85, 255),   windows_console=(0, 0, 255),     windows_powershell=(0, 0, 255),     windows_10_consolepowershell_6=(59, 120, 255),  terminal_app=(88, 51, 255),   putty=(85, 85, 255),   mirc=(0, 0, 252),     xterm=(92, 92, 255),   x=(173, 216, 230),   ubuntu=(0, 0, 255)    )),
    Color3Or4Bit(name='Bright Magenta', fg_code=95, bg_code=105, colors=TermColors(vga=(255, 85, 255),  windows_console=(255, 0, 255),   windows_powershell=(255, 0, 255),   windows_10_consolepowershell_6=(180, 0, 158),   terminal_app=(249, 53, 248),  putty=(255, 85, 255),  mirc=(255, 0, 255),   xterm=(255, 0, 255),   x=None,              ubuntu=(255, 0, 255)  )),
    Color3Or4Bit(name='Bright Cyan',    fg_code=96, bg_code=106, colors=TermColors(vga=(85, 255, 255),  windows_console=(0, 255, 255),   windows_powershell=(0, 255, 255),   windows_10_consolepowershell_6=(97, 214, 214),  terminal_app=(20, 240, 240),  putty=(85, 255, 255),  mirc=(0, 255, 255),   xterm=(0, 255, 255),   x=(224, 255, 255),   ubuntu=(0, 255, 255)  )),
    Color3Or4Bit(name='Bright White',   fg_code=97, bg_code=107, colors=TermColors(vga=(255, 255, 255), windows_console=(255, 255, 255), windows_powershell=(255, 255, 255), windows_10_consolepowershell_6=(242, 242, 242), terminal_app=(233, 235, 235), putty=(255, 255, 255), mirc=(255, 255, 255), xterm=(255, 255, 255), x=None,              ubuntu=(255, 255, 255))),
)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# 8 BIT                                                                     #
# ∙   0->  7: standard colors (as in ESC [ 30–37 m)                         #
# ∙   8-> 15: high intensity colors (as in ESC [ 90–97 m)                   #
# ∙  16->231: 6×6×6 cube (216 colors): 16 + 36*r + 6*g + b (0<=r, g, b<=5)  #
#             0=0x00, 95=0x5F, 135=0x87, 175=0xAF, 215=0xD7, 255=0xFF       #
# ∙ 232->255: grayscale from black to white in 24 steps (3% to 97%)         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit                    #
# ∙ https://jonasjacek.github.io/colors/data.json                           #
# ∙ https://github.com/sindresorhus/xterm-colors                            #
# ∙ https://gist.github.com/jasonm23/2868981                                #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# TYPES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


class Color8Bit(NamedTuple):
    name: str
    code: int
    hex: str
    rgb: RgbColor
    hsl: HslColor


# VARS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


from kolr.term.rgb256 import COLORS_8_BIT
COLORS_8_BIT = COLORS_8_BIT


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# 24 BIT                                                                    #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit                   #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


# # # # # # # # # # #
# # # REFERENCE # # #
# # # # # # # # # # #


# ESC, BGN, END = '\u001b', '[', 'm'

# 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, 7:white

# CODE_3BIT_FG_DARK = '3{n}'  # n=[0-7]
# CODE_3BIT_BG_DARK = '4{n}'  # n=[0-7]
# CODE_3BIT_FG_BRIGHT = '4{n}'  # n=[0-7]
# CODE_3BIT_BG_BRIGHT = '4{n}'  # n=[0-7]

#   0->  7:  standard colors (as in ESC [ 30–37 m)
#   8-> 15:  high intensity colors (as in ESC [ 90–97 m)
#  16->231:  6×6×6 cube (216 colors): 16 + 36×r + 6×g + b (0 ≤ r, g, b ≤ 5)
# 232->255:  grayscale from black to white in 24 steps

# CODE_8BIT_FG = ESC + BGN + '38:5:{n}' + END  # n=[0-255]
# CODE_8BIT_BG = ESC + BGN + '48:5:{n}' + END  # n=[0-255]

# CODE_24BIT_FG = ESC + BGN + '38;2;{r};{g};{b}' + END  # r=[0-255], g=[0-255], b=[0-255]
# CODE_24BIT_BG = ESC + BGN + '48;2;{r};{g};{b}' + END  # r=[0-255], g=[0-255], b=[0-255]


# # # # # # # # # # #
# # # TEMPLATES # # #
# # # # # # # # # # #


# ESC_CODE = '\u001b'
# ESC_CODE_TEMPLATE = '{esc}[{code}m'
#
# ZONE_FG = '3'
# ZONE_BG = '4'
#
# CODE_TEMPLATE = '{code}'
# CODE_TEMPLATE_3BIT = '{z}{i}'  # z=[3:fg|4:bg], i=[0-7]
# CODE_TEMPLATE_8BIT = '{z}8:5:{i}'  # z=[3:fg|4:bg], i=[0-255]
# CODE_TEMPLATE_24BIT = '{z}8;2;{r};{g};{b}'  # z=[3:fg|4:bg], r=[0-255], g=[0-255], b=[0-255]
#
# NAMES_3BIT = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
# STYLE_3BIt = ['']
#
#
# def _make_esc_code(template=CODE_TEMPLATE, escaped=True, **kwargs):
#     code = template.format(**kwargs)
#     return ESC_CODE_TEMPLATE.format(esc=ESC_CODE if escaped else '', code=code)



