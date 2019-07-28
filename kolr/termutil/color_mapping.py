# Nathan Michlo

from collections import namedtuple


# ========================================================================= #
# Terminal Names                                                            #
# ========================================================================= #


TERM_VGA = 'VGA'
TERM_WIN = 'WindowsConsole'
TERM_WPS = 'WindowsPowerShell'
TERM_W10 = 'Widows10'
TERM_OSX = 'Terminal.app'
TERM_PTY = 'PuTTY'
TERM_MIR = 'mIRC'
TERM_XTM = 'xterm'
TERM_X   = 'X'
TERM_UBT = 'Ubuntu'

TERMINALS = {TERM_VGA, TERM_WIN, TERM_WPS, TERM_W10, TERM_OSX, TERM_PTY, TERM_MIR, TERM_XTM, TERM_X, TERM_UBT}


# ========================================================================= #
# Colors                                                                    #
# https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit                    #
# ========================================================================= #


_TermColor = namedtuple('TermColor', ['name', 'code_fg', 'code_bg', 'color_map'])


_TERM_COLORS = [
    _TermColor('black',          30, 40,  {TERM_VGA: (0,  0,  0),   TERM_WIN: (0,  0,  0),   TERM_WPS: (0,  0,  0),   TERM_W10: (12, 12, 12),  TERM_OSX: (0,  0,  0),   TERM_PTY: (0,  0,  0),   TERM_MIR: (0,  0,  0),   TERM_XTM: (0,  0,  0),   TERM_X: (0,0,0),       TERM_UBT: (1,  1,  1)  }),
    _TermColor('red',            31, 41,  {TERM_VGA: (170,0,  0),   TERM_WIN: (128,0,  0),   TERM_WPS: (128,0,  0),   TERM_W10: (197,15, 31),  TERM_OSX: (194,54, 33),  TERM_PTY: (187,0,  0),   TERM_MIR: (127,0,  0),   TERM_XTM: (205,0,  0),   TERM_X: (255,0,0),     TERM_UBT: (222,56, 43) }),
    _TermColor('green',          32, 42,  {TERM_VGA: (0,  170,0),   TERM_WIN: (0,  128,0),   TERM_WPS: (0,  128,0),   TERM_W10: (19, 161,14),  TERM_OSX: (37, 188,36),  TERM_PTY: (0,  187,0),   TERM_MIR: (0,  147,0),   TERM_XTM: (0,  205,0),   TERM_X: (0,255,0),     TERM_UBT: (57, 181,74) }),
    _TermColor('yellow',         33, 43,  {TERM_VGA: (170,85, 0),   TERM_WIN: (128,128,0),   TERM_WPS: (238,237,240), TERM_W10: (193,156,0),   TERM_OSX: (173,173,39),  TERM_PTY: (187,187,0),   TERM_MIR: (252,127,0),   TERM_XTM: (205,205,0),   TERM_X: (255,255,0),   TERM_UBT: (255,199,6)  }),
    _TermColor('blue',           34, 44,  {TERM_VGA: (0,  0,  170), TERM_WIN: (0,  0,  128), TERM_WPS: (0,  0,  128), TERM_W10: (0,  55, 218), TERM_OSX: (73, 46, 225), TERM_PTY: (0,  0,  187), TERM_MIR: (0,  0,  127), TERM_XTM: (0,  0,  238), TERM_X: (0,0,255),     TERM_UBT: (0,  111,184)}),
    _TermColor('magenta',        35, 45,  {TERM_VGA: (170,0,  170), TERM_WIN: (128,0,  128), TERM_WPS: (1,  36, 86),  TERM_W10: (136,23, 152), TERM_OSX: (211,56, 211), TERM_PTY: (187,0,  187), TERM_MIR: (156,0,  156), TERM_XTM: (205,0,  205), TERM_X: (255,0,255),   TERM_UBT: (118,38, 113)}),
    _TermColor('cyan',           36, 46,  {TERM_VGA: (0,  170,170), TERM_WIN: (0,  128,128), TERM_WPS: (0,  128,128), TERM_W10: (58, 150,221), TERM_OSX: (51, 187,200), TERM_PTY: (0,  187,187), TERM_MIR: (0,  147,147), TERM_XTM: (0,  205,205), TERM_X: (0,255,255),   TERM_UBT: (44, 181,233)}),
    _TermColor('white',          37, 47,  {TERM_VGA: (170,170,170), TERM_WIN: (192,192,192), TERM_WPS: (192,192,192), TERM_W10: (204,204,204), TERM_OSX: (203,204,205), TERM_PTY: (187,187,187), TERM_MIR: (210,210,210), TERM_XTM: (229,229,229), TERM_X: (255,255,255), TERM_UBT: (204,204,204)}),
    _TermColor('bright_black',   90, 100, {TERM_VGA: (85, 85, 85),  TERM_WIN: (128,128,128), TERM_WPS: (128,128,128), TERM_W10: (118,118,118), TERM_OSX: (129,131,131), TERM_PTY: (85, 85, 85),  TERM_MIR: (127,127,127), TERM_XTM: (127,127,127), TERM_X: None,          TERM_UBT: (128,128,128)}),
    _TermColor('bright_red',     91, 101, {TERM_VGA: (255,85, 85),  TERM_WIN: (255,0,  0),   TERM_WPS: (255,0,  0),   TERM_W10: (231,72, 86),  TERM_OSX: (252,57, 31),  TERM_PTY: (255,85, 85),  TERM_MIR: (255,0,  0),   TERM_XTM: (255,0,  0),   TERM_X: None,          TERM_UBT: (255,0,  0)  }),
    _TermColor('bright_green',   92, 102, {TERM_VGA: (85, 255,85),  TERM_WIN: (0,  255,0),   TERM_WPS: (0,  255,0),   TERM_W10: (22, 198,12),  TERM_OSX: (49, 231,34),  TERM_PTY: (85, 255,85),  TERM_MIR: (0,  252,0),   TERM_XTM: (0,  255,0),   TERM_X: (144,238,144), TERM_UBT: (0,  255,0)  }),
    _TermColor('bright_yellow',  93, 103, {TERM_VGA: (255,255,85),  TERM_WIN: (255,255,0),   TERM_WPS: (255,255,0),   TERM_W10: (249,241,165), TERM_OSX: (234,236,35),  TERM_PTY: (255,255,85),  TERM_MIR: (255,255,0),   TERM_XTM: (255,255,0),   TERM_X: (255,255,224), TERM_UBT: (255,255,0)  }),
    _TermColor('bright_blue',    94, 104, {TERM_VGA: (85, 85, 255), TERM_WIN: (0,  0,  255), TERM_WPS: (0,  0,  255), TERM_W10: (59, 120,255), TERM_OSX: (88, 51, 255), TERM_PTY: (85, 85, 255), TERM_MIR: (0,  0,  252), TERM_XTM: (92, 92, 255), TERM_X: (173,216,230), TERM_UBT: (0,  0,  255)}),
    _TermColor('bright_magenta', 95, 105, {TERM_VGA: (255,85, 255), TERM_WIN: (255,0,  255), TERM_WPS: (255,0,  255), TERM_W10: (180,0,  158), TERM_OSX: (249,53, 248), TERM_PTY: (255,85, 255), TERM_MIR: (255,0,  255), TERM_XTM: (255,0,  255), TERM_X: None,          TERM_UBT: (255,0,  255)}),
    _TermColor('bright_cyan',    96, 106, {TERM_VGA: (85, 255,255), TERM_WIN: (0,  255,255), TERM_WPS: (0,  255,255), TERM_W10: (97, 214,214), TERM_OSX: (20, 240,240), TERM_PTY: (85, 255,255), TERM_MIR: (0,  255,255), TERM_XTM: (0,  255,255), TERM_X: (224,255,255), TERM_UBT: (0,  255,255)}),
    _TermColor('bright_white',   97, 107, {TERM_VGA: (255,255,255), TERM_WIN: (255,255,255), TERM_WPS: (255,255,255), TERM_W10: (242,242,242), TERM_OSX: (233,235,235), TERM_PTY: (255,255,255), TERM_MIR: (255,255,255), TERM_XTM: (255,255,255), TERM_X: None,          TERM_UBT: (255,255,255)}),
]

_TERM_COLORS_3_BIT = [_TERM_COLORS[i] for i in range(2**3)]
_TERM_COLORS_4_BIT = [_TERM_COLORS[i] for i in range(2**4)]


# ========================================================================= #
# DETECTOR                                                                  #
# ========================================================================= #


def _detect_terminal():
    """
    Naive attempt to detect the terminal program.
    TODO: This needs lots of work, could merge detect color and detect termial logic?
    :return: possible detected terminal
    """
    import os

    # _plat = sys.platform.lower()
    # if 'darwin' in _plat:
    #     IS_MACOS = True
    # elif 'linux' in _plat:
    #     IS_LINUX = True
    # elif 'solaris' in _plat:
    #     IS_SOLARIS = True
    # elif 'freebsd' in _plat:
    #     IS_FREEBSD = True
    # elif 'cygwin' in _plat:
    #     IS_CYGWIN = True  # Emulates POSIX standards, to make porting Unix-based apps to Windows easier
    # elif 'msys' in _plat:
    #     IS_MINGW = True  # Minimal env. for Windows port of GNU compiler tools: GCC, Make, Bash, etc.
    # elif 'win32' in _plat:
    #     IS_WIN32 = True

    termprog_env = os.environ.get('TERM_PROGRAM', None)
    if termprog_env:
        if termprog_env in TERMINALS:
            return termprog_env
        print(f'TERM_PROGRAM does not match, please report this: {termprog_env}')

    term_env = os.environ.get('TERM', None)
    if term_env:
        if term_env in TERMINALS:
            return termprog_env
        print(f'TERM does not match, please report this: {term_env}')

    return TERM_VGA


# ========================================================================= #
# DETECT                                                                    #
# ========================================================================= #


TERMINAL = _detect_terminal()

COLORS_3_BIT = [(_TERM_COLORS[i].name, _TERM_COLORS[i].color_map[TERMINAL]) for i in range(2**3)]
COLORS_4_BIT = [(_TERM_COLORS[i].name, _TERM_COLORS[i].color_map[TERMINAL]) for i in range(2**4)]


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
