# Nathan Michlo

from collections import namedtuple


# ========================================================================= #
# SGR PARAMETERS (Select Graphic Rendition)                                 #
# https://stackoverflow.com/questions/4842424                               #
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters             #
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
    _SgrParam(code=20, type=SGR_TYPE_STYLE, name='franktur', desc='Fraktur', note='Latin calligraphic hand. Hardly ever supported.'),  # https://en.wikipedia.org/wiki/Fraktur
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
# REFERENCE                                                                 #
# ========================================================================= #


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


# ========================================================================= #
# TEMPLATES                                                                 #
# ========================================================================= #


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


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
