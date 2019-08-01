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


from typing import Tuple, NamedTuple


# ========================================================================= #
# Escape Character                                                          #
# ∙ octal=\033 ∙ hex=\x1B ∙ decimal=27 ∙ keyboard=^[                        #
# ========================================================================= #


ESC = '\033'


# ========================================================================= #
# Escape sequences                                                          #
# ∙ ESC ...                                                                 #
# ∙ https://invisible-island.net/xterm/ctlseqs/ctlseqs.html                 #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences         #
# ========================================================================= #


# - - - - - - - - - - - - - - - - - TYPES - - - - - - - - - - - - - - - - - #


class ControlChar(NamedTuple):
    # alt
    bits7: str
    bits8: str
    short: str
    name: str
    desc: str


class SingleCharFunc(NamedTuple):
    short: str
    code: str
    desc: str


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


# C1 (8-Bit) Control Characters
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
CONTROL_CHARACTERS = [
    ControlChar(bits7=ESC + 'D',  bits8='\x84', short='IND',   name='Index',                       desc=""),
    ControlChar(bits7=ESC + 'E',  bits8='\x85', short='NEL',   name='Next Line',                   desc=""),
    ControlChar(bits7=ESC + 'H',  bits8='\x88', short='HTS',   name='Tab Set',                     desc=""),
    ControlChar(bits7=ESC + 'M',  bits8='\x8d', short='RI',    name='Reverse Index',               desc=""),
    ControlChar(bits7=ESC + 'N',  bits8='\x8e', short='SS2',   name='Single Shift Two',            desc="Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set."),
    ControlChar(bits7=ESC + 'O',  bits8='\x8f', short='SS3',   name='Single Shift Three',          desc="Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set."),
    ControlChar(bits7=ESC + 'P',  bits8='\x90', short='DCS',   name='Device Control String',       desc="Terminated by ST. Xterm's uses of this sequence include defining User-Defined Keys, and requesting or setting Termcap/Terminfo data."),
    ControlChar(bits7=ESC + 'V',  bits8='\x96', short='SPA',   name='Start of Guarded Area',       desc=""),
    ControlChar(bits7=ESC + 'W',  bits8='\x97', short='EPA',   name='End of Guarded Area',         desc=""),
    ControlChar(bits7=ESC + 'X',  bits8='\x98', short='SOS',   name='Start of String',             desc="Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm."),
    ControlChar(bits7=ESC + 'Z',  bits8='\x9a', short='DECID', name='Return Terminal ID',          desc="Obsolete form of CSI c (DA)."),
    ControlChar(bits7=ESC + '[',  bits8='\x9b', short='CSI',   name='Control Sequence Introducer', desc="Most of the useful sequences, see next section."),
    ControlChar(bits7=ESC + '\\', bits8='\x9c', short='ST',    name='String Terminator',           desc="Terminates strings in other controls.:8.3.143"),
    ControlChar(bits7=ESC + ']',  bits8='\x9d', short='OSC',   name='Operating System Command',    desc="Starts a control string for the operating system to use, terminated by ST.:8.3.89 In xterm, they may also be terminated by BEL. In xterm, the window title can be set by OSC 0;this is the window title BEL."),
    ControlChar(bits7=ESC + '^',  bits8='\x9e', short='PM',    name='Privacy Message',             desc="Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm."),
    ControlChar(bits7=ESC + '_',  bits8='\x9f', short='APC',   name='Application Program Command', desc="Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm."),
    ControlChar(bits7=ESC + 'c',  bits8=None,   short='RIS',   name='Reset to Initial State',      desc='Resets the device to its original state.  This may include (if applicable): reset graphic rendition, clear tabulation stops, reset to default font, and more.'),
]

# Single Character Functions
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Single-character-functions
SINGLE_CHAR_FUNCTIONS = [
    SingleCharFunc(short='BEL', code='Ctrl-G', desc="Bell (Ctrl-G)."),
    SingleCharFunc(short='BS',  code='Ctrl-H', desc="Backspace (Ctrl-H)."),
    SingleCharFunc(short='CR',  code='Ctrl-M', desc="Carriage Return (Ctrl-M)."),
    SingleCharFunc(short='ENQ', code='Ctrl-E', desc="Return Terminal Status (Ctrl-E).  Default response is an empty string, but may be overridden by a resource answerbackString."),
    SingleCharFunc(short='FF',  code='Ctrl-L', desc="Form Feed or New Page (NP).  (FF  is Ctrl-L).  FF  is treated the same as LF ."),
    SingleCharFunc(short='LF',  code='Ctrl-J', desc="Line Feed or New Line (NL).  (LF  is Ctrl-J)."),
    SingleCharFunc(short='SI',  code='Ctrl-O', desc="Switch to Standard Character Set (Ctrl-O is Shift In or LS0). This invokes the G0 character set (the default) as GL. VT200 and up implement LS0."),
    SingleCharFunc(short='SO',  code='Ctrl-N', desc="Switch to Alternate Character Set (Ctrl-N is Shift Out or LS1).  This invokes the G1 character set as GL. VT200 and up implement LS1."),
    SingleCharFunc(short='SP',  code='Space',  desc="Space."),
    SingleCharFunc(short='TAB', code='Ctrl-I', desc="Horizontal Tab (HT) (Ctrl-I)."),
    SingleCharFunc(short='VT',  code='Ctrl-K', desc="Vertical Tab (Ctrl-K).  This is treated the same as LF."),
]


# ========================================================================= #
# CSI SEQUENCES (Control Sequence Introducer)                               #
# ∙ CSI = ESC [ ...                                                         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences            #
# ========================================================================= #


# - - - - - - - - - - - - - - - - - TYPES - - - - - - - - - - - - - - - - - #


class CsiSequence(NamedTuple):
    code: str
    short: str
    name: str
    desc: str


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


CSI_SEQUENCES = [
    CsiSequence(code='CSI n A',     short='CUU', name='Cursor Up',                    desc='Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.'),
    CsiSequence(code='CSI n B',     short='CUD', name='Cursor Down',                  desc='Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.'),
    CsiSequence(code='CSI n C',     short='CUF', name='Cursor Forward',               desc='Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.'),
    CsiSequence(code='CSI n D',     short='CUB', name='Cursor Back',                  desc='Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.'),
    CsiSequence(code='CSI n E',     short='CNL', name='Cursor Next Line',             desc='Moves cursor to beginning of the line n (default 1) lines down.  (not ANSI.SYS)'),
    CsiSequence(code='CSI n F',     short='CPL', name='Cursor Previous Line',         desc='Moves cursor to beginning of the line n (default 1) lines up.  (not ANSI.SYS)'),
    CsiSequence(code='CSI n G',     short='CHA', name='Cursor Horizontal Absolute',   desc='Moves the cursor to column n (default 1).  (not ANSI.SYS)'),
    CsiSequence(code='CSI n ; m H', short='CUP', name='Cursor Position',              desc='Moves the cursor to row n, column m.  The values are 1-based, and default to 1 (top left corner) if omitted.  A sequence such as CSI ;5H is a synonym for CSI 1;5H as well as CSI 17;H is the same as CSI 17H and CSI 17;1H'),
    CsiSequence(code='CSI n J',     short='ED',  name='Erase in Display',             desc='Clears part of the screen. If n is 0 (or missing), clear from cursor to end of screen. If n is 1, clear from cursor to beginning of the screen. If n is 2, clear entire screen (and moves cursor to upper left on DOS ANSI.SYS).  If n is 3, clear entire screen and delete all lines saved in the scrollback buffer (this feature was added for xterm and is supported by other terminal applications).'),
    CsiSequence(code='CSI n K',     short='EL',  name='Erase in Line',                desc='Erases part of the line. If n is 0 (or missing), clear from cursor to the end of the line. If n is 1, clear from cursor to beginning of the line. If n is 2, clear entire line.  Cursor position does not change.'),
    CsiSequence(code='CSI n S',     short='SU',  name='Scroll Up',                    desc='Scroll whole page up by n (default 1) lines.  New lines are added at the bottom.  (not ANSI.SYS)'),
    CsiSequence(code='CSI n T',     short='SD',  name='Scroll Down',                  desc='Scroll whole page down by n (default 1) lines.  New lines are added at the top.  (not ANSI.SYS)'),
    CsiSequence(code='CSI n ; m f', short='HVP', name='Horizontal Vertical Position', desc='Same as CUP'),
    CsiSequence(code='CSI n m',     short='SGR', name='Select Graphic Rendition',     desc='Sets the appearance of the following characters, see SGR parameters below.'),
    CsiSequence(code='CSI 5i',      short=None,  name='AUX Port On',                  desc='Enable aux serial port usually for local serial printer'),
    CsiSequence(code='CSI 4i',      short=None,  name='AUX Port Off',                 desc='Disable aux serial port usually for local serial printer'),
    CsiSequence(code='CSI 6n',      short='DSR', name='Device Status Report',         desc='Reports the cursor position (CPR) to the application as (as though typed at the keyboard) ESC[n;mR, where n is the row and m is the column.)'),
    CsiSequence(code='CSI s',       short='SCP', name='Save Cursor Position',         desc='Saves the cursor position/state.'),
    CsiSequence(code='CSI u',       short='RCP', name='Restore Cursor Position',      desc='Restores the cursor position/state.'),
]

CSI_SEQUENCES_PRIVATE = [
    CsiSequence(code='CSI ? 25 h',   short=None, name='Show Cursor',           desc='DECTCEM Shows the cursor, from the VT320.'),
    CsiSequence(code='CSI ? 25 l',   short=None, name='Hide Cursor',           desc='DECTCEM Hides the cursor.'),
    CsiSequence(code='CSI ? 1049 h', short=None, name='Enable Screen Buffer',  desc='Enable alternative screen buffer'),
    CsiSequence(code='CSI ? 1049 l', short=None, name='Disable Screen Buffer', desc='Disable alternative screen buffer'),
    CsiSequence(code='CSI ? 2004 h', short=None, name='Enable Bracket Paste',  desc='Turn on bracketed paste mode. Text pasted into the terminal will be surrounded by ESC  From Unix terminal emulators.'),
    CsiSequence(code='CSI ? 2004 l', short=None, name='Disable Bracked Pase',  desc='Turn off bracketed paste mode.'),
]


# ========================================================================= #
# SGR PARAMETERS (Select Graphic Rendition)                                 #
# ∙ SGR = CSI ... m                                                         #
# ∙ https://stackoverflow.com/questions/4842424                             #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters           #
# ========================================================================= #


# - - - - - - - - - - - - - - - - - TYPES - - - - - - - - - - - - - - - - - #


class SgrParam(NamedTuple):
    code: int
    type: str
    name: str
    desc: str
    note: str


_SGR_TYPE_STYLE = 'style'
_SGR_TYPE_RESET = 'reset'
_SGR_TYPE_COLOR = 'color'
_SGR_TYPE_COLOR_SEL = 'color_selector'
_SGR_TYPES = (_SGR_TYPE_STYLE, _SGR_TYPE_RESET, _SGR_TYPE_COLOR, _SGR_TYPE_COLOR_SEL)


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


COLOR_NAMES_3BIT = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


_SGR_PARAMS_ALT_FONTS        = [SgrParam(code=i, type=_SGR_TYPE_STYLE, name=f'font_alt_{i-10}',                      desc=f'Select alternate font: {i - 10}',                          note='') for i in range(11, 20)]
_SGR_PARAMS_FG_COLORS        = [SgrParam(code=i, type=_SGR_TYPE_COLOR, name=f'fg_{COLOR_NAMES_3BIT[i - 30]}',        desc=f'Set foreground color: {COLOR_NAMES_3BIT[i - 30]}',         note='') for i in range(30, 38)]
_SGR_PARAMS_BG_COLORS        = [SgrParam(code=i, type=_SGR_TYPE_COLOR, name=f'bg_{COLOR_NAMES_3BIT[i - 40]}',        desc=f'Set background color: {COLOR_NAMES_3BIT[i - 40]}',         note='') for i in range(40, 48)]
_SGR_PARAMS_FG_COLORS_BRIGHT = [SgrParam(code=i, type=_SGR_TYPE_COLOR, name=f'fg_bright_{COLOR_NAMES_3BIT[i - 90]}', desc=f'Set bright foreground color: {COLOR_NAMES_3BIT[i - 90]}',  note='aixterm (not in standard)') for i in range(90, 98)]
_SGR_PARAMS_BG_COLORS_BRIGHT = [SgrParam(code=i, type=_SGR_TYPE_COLOR, name=f'bg_bright_{COLOR_NAMES_3BIT[i - 100]}',desc=f'Set bright background color: {COLOR_NAMES_3BIT[i - 100]}', note='aixterm (not in standard)') for i in range(100, 108)]


SGR_PARAMS = [
    SgrParam(code=0,  type=_SGR_TYPE_RESET,     name='reset',                     desc='Reset / Normal',               note='All attributes off.'),
    SgrParam(code=1,  type=_SGR_TYPE_STYLE,     name='bold',                      desc='Bold or increased intensity',  note=''),
    SgrParam(code=2,  type=_SGR_TYPE_STYLE,     name='faint',                     desc='Faint (decreased intensity)',  note='Not widely supported.'),
    SgrParam(code=3,  type=_SGR_TYPE_STYLE,     name='italic',                    desc='Italic',                       note='Not widely supported. Sometimes treated as inverse.'),
    SgrParam(code=4,  type=_SGR_TYPE_STYLE,     name='underline',                 desc='Underline',                    note=''),
    SgrParam(code=5,  type=_SGR_TYPE_STYLE,     name='blink',                     desc='Slow Blink',                   note='Less than 150 blinks per minute'),
    SgrParam(code=6,  type=_SGR_TYPE_STYLE,     name='blink_rapid',               desc='Rapid Blink',                  note='MS-DOS ANSI.SYS; 150+ blicks per minute. Not widely supported'),
    SgrParam(code=7,  type=_SGR_TYPE_STYLE,     name='invert',                    desc='[[reverse video]]',            note='Swap foreground and background colors'),
    SgrParam(code=8,  type=_SGR_TYPE_STYLE,     name='conceal',                   desc='Conceal',                      note='Not widely supported.'),
    SgrParam(code=9,  type=_SGR_TYPE_STYLE,     name='strikethrough',             desc='Crossed-out',                  note='Characters legible, but marked for deletion.  Not widely supported.'),
    SgrParam(code=10, type=_SGR_TYPE_STYLE,     name='font_primary',              desc='Primary(default) font',        note=''),
    *_SGR_PARAMS_ALT_FONTS,  # 11-19 Alternate Font
    SgrParam(code=20, type=_SGR_TYPE_STYLE,     name='franktur',                  desc='Fraktur',                      note='Latin calligraphic hand. Hardly ever supported.'),  # https://en.wikipedia.org/wiki/Fraktur # might instead be reset_style (not color)
    SgrParam(code=21, type=_SGR_TYPE_RESET,     name='reset_bold',                desc='Bold off or Double Underline', note='Bold off not widely supported; double underline hardly ever supported.'),
    SgrParam(code=22, type=_SGR_TYPE_RESET,     name='reset_intensity',           desc='Normal color or intensity',    note='Neither bold nor faint.'),
    SgrParam(code=23, type=_SGR_TYPE_RESET,     name='reset_italic',              desc='Not italic, not Fraktur',      note=''),
    SgrParam(code=24, type=_SGR_TYPE_RESET,     name='reset_underline',           desc='Underline off',                note='Not singly or doubly underlined.'),
    SgrParam(code=25, type=_SGR_TYPE_RESET,     name='reset_blink',               desc='Blink off',                    note=''),
    # 26 <reset blink fast?>
    SgrParam(code=27, type=_SGR_TYPE_RESET,     name='reset_inverse',             desc='Inverse off',                  note=''),
    SgrParam(code=28, type=_SGR_TYPE_RESET,     name='reset_conceal',             desc='Reveal',                       note='Conceal off.'),
    SgrParam(code=29, type=_SGR_TYPE_RESET,     name='reset_strikethrough',       desc='Not crossed out',              note=''),
    *_SGR_PARAMS_FG_COLORS,  # 30-37 Set foreground color
    SgrParam(code=38, type=_SGR_TYPE_COLOR_SEL, name='fg_select',                 desc='Set general foreground color', note='Next arguments are `5;n` or `2;r;g;b`, see below.'),
    SgrParam(code=39, type=_SGR_TYPE_RESET,     name='reset_fg',                  desc='Default foreground color',     note='Implementation defined (according to standard).'),
    *_SGR_PARAMS_BG_COLORS,  # 40-47 Set background color
    SgrParam(code=48, type=_SGR_TYPE_COLOR_SEL, name='bg_select',                 desc='Set general background color', note='Next arguments are `5;n` or `2;r;g;b`, see 8bit and 24bit.'),
    SgrParam(code=49, type=_SGR_TYPE_RESET,     name='reset_bg',                  desc='Default background color',     note='Implementation defined (according to standard)'),
    # 50 <unused>
    SgrParam(code=51, type=_SGR_TYPE_STYLE,     name='frame',                     desc='Framed',                       note=''),
    SgrParam(code=52, type=_SGR_TYPE_STYLE,     name='encircle',                  desc='Encircled',                    note=''),
    SgrParam(code=53, type=_SGR_TYPE_STYLE,     name='overline',                  desc='Overlined',                    note=''),
    SgrParam(code=54, type=_SGR_TYPE_RESET,     name='reset_frame',               desc='Not framed or encircled',      note=''),
    SgrParam(code=55, type=_SGR_TYPE_RESET,     name='reset_overline',            desc='Not overlined',                note=''),
    # 56-59 <unused>
    SgrParam(code=60, type=_SGR_TYPE_STYLE,     name='ideogram_underline',        desc='ideogram underline',           note='Hardly ever supported.'),
    SgrParam(code=61, type=_SGR_TYPE_STYLE,     name='ideogram_double_underline', desc='ideogram double underline',    note='Hardly ever supported.'),
    SgrParam(code=62, type=_SGR_TYPE_STYLE,     name='ideogram_overline',         desc='ideogram overline',            note='Hardly ever supported.'),
    SgrParam(code=63, type=_SGR_TYPE_STYLE,     name='ideogram_double_overline',  desc='ideogram double overline',     note='Hardly ever supported.'),
    SgrParam(code=64, type=_SGR_TYPE_STYLE,     name='ideogram_stress',           desc='ideogram stress marking',      note='Hardly ever supported.'),
    SgrParam(code=65, type=_SGR_TYPE_RESET,     name='reset_ideogram',            desc='ideogram attributes off',      note='Reset the effects of all of 60-64.'),
    # 66-89 <unused>
    *_SGR_PARAMS_FG_COLORS_BRIGHT,  # 90-97 Set bright foreground color
    # 98-99 <unused>
    *_SGR_PARAMS_BG_COLORS_BRIGHT,  # 100-107 Set bright background color
]

# Info Dicts
_NAME_TO_SGR = {}
_CODE_TO_SGR = {}
_TYPE_TO_SGRS = {}

# Fill Dicts
for sgr in SGR_PARAMS:
    if sgr.name in _NAME_TO_SGR: raise KeyError(f'Duplicate Keys Found: {sgr.name}')
    _NAME_TO_SGR[sgr.name] = sgr
    if sgr.code in _CODE_TO_SGR: raise KeyError(f'Duplicate Keys Found: {sgr.name}')
    _CODE_TO_SGR[sgr.code] = sgr
    if sgr.type not in _TYPE_TO_SGRS: _TYPE_TO_SGRS[sgr.type] = []
    _TYPE_TO_SGRS[sgr.type].append(sgr)


# ========================================================================= #
# SGR COLORS                                                                #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#Colors                   #
# ========================================================================= #


# ------------------------------------------------------------------------- #
# 3/4 BIT                                                                   #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit                  #
# ------------------------------------------------------------------------- #


# - - - - - - - - - - - - - - - - - TYPES - - - - - - - - - - - - - - - - - #


RgbColor = Tuple[int, int, int]


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


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


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


# ------------------------------------------------------------------------- #
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
# ------------------------------------------------------------------------- #


# - - - - - - - - - - - - - - - - - TYPES - - - - - - - - - - - - - - - - - #


from kolr.term.rgb256 import Color8Bit


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


from kolr.term.rgb256 import COLORS_8_BIT


# ------------------------------------------------------------------------- #
# 24 BIT                                                                    #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit                   #
# ------------------------------------------------------------------------- #


# TODO


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



