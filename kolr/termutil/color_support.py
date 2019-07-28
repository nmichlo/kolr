"""
Color support detection largely based on colorful (by Timo Furrer)
with additions from supports-color (by Sindre Sorhus) translated from javascript.

colorful:
> https://github.com/timofurrer/colorful/blob/master/colorful/terminal.py
> :copyright: (c) 2017 by Timo Furrer <tuxtimo@gmail.com>
> :license: MIT, see LICENSE for more details.

supports-color:
> https://github.com/chalk/supports-color/blob/master/index.js
"""


# ========================================================================= #
# KERNAL VARS                                                               #
# ========================================================================= #


# Valid color modes for kolr
import platform

ANSI_MONOCHROME   = 0x0
ANSI_3_BIT_COLOR  = 0x7
ANSI_4_BIT_COLOR  = 0xF
ANSI_8_BIT_COLOR  = 0xFF
ANSI_24_BIT_COLOR = 0xFFFFFF


# ========================================================================= #
# DETECTOR                                                                  #
# ========================================================================= #


def _detect_color_support():
    """
    Detect the largest color palette supported by the terminal.
    :return: one of ANSI_MONOCHROME|ANSI_3_BIT_COLOR|ANSI_4_BIT_COLOR|ANSI_8_BIT_COLOR|ANSI_24_BIT_COLOR
    """

    import sys
    import os

    def is_enabled(string):
        # all right, alright, very well, of course, by all means, sure,
        # certainly, absolutely, indeed, affirmative, agreed, roger, aye
        # yeah, yah, yep, yup, uh-huh, okay, ok, okey-dokey, okey-doke, righty-ho
        return string.lower() in {'1', 'on', 'y', 'yes', 'enable', 'enabled'}

    # | # 0:monochrome, 1:4bit, 2:8bit, 3:24bit
    # | if (forceColor == 0):
    # |     return 0
    # | if (hasFlag('color=16m') or hasFlag('color=full') or hasFlag('color=truecolor')):
    # |     return 3
    # | if (hasFlag('color=256')):
    # |     return
    # | if (stream and not stream.isTTY and forceColor is None):
    # |     return 0
    # | min = forceColor or 0

    if is_enabled(os.environ.get('KOLR_FORCE_MONOCHROME', '0')):
        return ANSI_MONOCHROME
    elif is_enabled(os.environ.get('KOLR_FORCE_3_BIT', '0')):
        return ANSI_3_BIT_COLOR
    elif is_enabled(os.environ.get('KOLR_FORCE_4_BIT', '0')):
        return ANSI_4_BIT_COLOR
    elif is_enabled(os.environ.get('KOLR_FORCE_8_BIT', '0')):
        return ANSI_8_BIT_COLOR
    elif is_enabled(os.environ.get('KOLR_FORCE_24_BIT', '0')):
        return ANSI_24_BIT_COLOR

    # if we are not a tty
    if not sys.stdout.isatty():
        return ANSI_MONOCHROME

    # | if (env.TERM == 'dumb'):
    # |     return min

    if os.environ.get('TERM', None) == 'dumb':
        return ANSI_MONOCHROME

    # Windows 10 build 10586 is the first to support 8-bit colors.
    # Windows 10 build 14931 is the first to support 24-bit colors.
    if 'win32' in platform.platform():
        version = platform.version().split('.')
        if int(version[0]) > 10 and (int(version[2]) >= 10586):
            return ANSI_24_BIT_COLOR if (int(version[2]) >= 14931) else ANSI_8_BIT_COLOR
        return ANSI_8_BIT_COLOR

    if 'CI' in os.environ:
        if any(key in os.environ for key in ['TRAVIS', 'CIRCLECI', 'APPVEYOR', 'GITLAB_CI']):
            return ANSI_4_BIT_COLOR
        if os.environ.get('CI_NAME', None) == 'codeship':
            return ANSI_4_BIT_COLOR

    # | if ('TEAMCITY_VERSION' in env):
    # |     return /^(9\.(0*[1-9]\d*)\.|\d{2,}\.)/.test(env.TEAMCITY_VERSION) ? 1 : 0

    if os.environ.get('TEAMCITY_VERSION', None):
        return ANSI_4_BIT_COLOR

    colorterm_env = os.environ.get('COLORTERM', None)
    if colorterm_env:
        if colorterm_env in {'truecolor', '24bit'}:
            return ANSI_24_BIT_COLOR
        if colorterm_env in {'8bit'}:
            return ANSI_8_BIT_COLOR

    termprog_env = os.environ.get('TERM_PROGRAM', None)
    if termprog_env:
        if termprog_env in {'iTerm.app'}:
            version = int(os.environ.get('TERM_PROGRAM_VERSION', '2').split('.')[0])
            return ANSI_24_BIT_COLOR if version >= 3 else ANSI_8_BIT_COLOR
        if termprog_env in {'Hyper'}:
            return ANSI_24_BIT_COLOR
        if termprog_env in {'Apple_Terminal'}:
            return ANSI_8_BIT_COLOR

    term_env = os.environ.get('TERM', None)
    if term_env:
        if term_env in {'screen-256', 'screen-256color', 'xterm-256', 'xterm-256color'} or ('-256' in term_env):
            return ANSI_8_BIT_COLOR
        if term_env in {'screen', 'xterm', 'vt100', 'vt220', 'rxvt', 'color', 'ansi', 'cygwin', 'linux'}:
            return ANSI_4_BIT_COLOR

    # | if ('COLORTERM' in env):
    # |     return 1
    # | return min

    if colorterm_env:
        # if there was no match with $TERM either but we
        # had one with $COLORTERM, we use it!
        return ANSI_4_BIT_COLOR

    return ANSI_3_BIT_COLOR


# ========================================================================= #
# DETECT                                                                    #
# ========================================================================= #


COLOR_SUPPORT          = _detect_color_support()

IS_MONOCHROME          = (COLOR_SUPPORT == ANSI_MONOCHROME)
IS_3_BIT_COLOR         = (COLOR_SUPPORT == ANSI_3_BIT_COLOR)
IS_4_BIT_COLOR         = (COLOR_SUPPORT == ANSI_4_BIT_COLOR)
IS_8_BIT_COLOR         = (COLOR_SUPPORT == ANSI_8_BIT_COLOR)
IS_24_BIT_COLOR        = (COLOR_SUPPORT == ANSI_24_BIT_COLOR)

HAS_MONOCHROME_SUPPORT = (COLOR_SUPPORT >= ANSI_MONOCHROME)
HAS_3_BIT_SUPPORT      = (COLOR_SUPPORT >= ANSI_3_BIT_COLOR)
HAS_4_BIT_SUPPORT      = (COLOR_SUPPORT >= ANSI_4_BIT_COLOR)
HAS_8_BIT_SUPPORT      = (COLOR_SUPPORT >= ANSI_8_BIT_COLOR)
HAS_24_BIT_SUPPORT     = (COLOR_SUPPORT >= ANSI_24_BIT_COLOR)

HAS_NO_SUPPORT         = IS_MONOCHROME


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
