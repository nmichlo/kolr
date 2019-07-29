# Color support detection largely based on colorful (by Timo Furrer) with
# additions from the javascript supports-color library (by Sindre Sorhus).
#
# colorful: https://github.com/timofurrer/colorful/blob/master/colorful/terminal.py
# supports-color: https://github.com/chalk/supports-color/blob/master/index.js
#
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
# Original License
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
#
# The MIT License (MIT)
#
# Copyright (c) 2017 Timo Furrer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# ========================================================================= #
# VARS                                                                      #
# ========================================================================= #


# Valid color modes for kolr
ANSI_MONO_COLOR   = 0x0
ANSI_3_BIT_COLOR  = 0x7
ANSI_4_BIT_COLOR  = 0xF
ANSI_8_BIT_COLOR  = 0xFF
ANSI_24_BIT_COLOR = 0xFFFFFF


# ========================================================================= #
# DETECTOR                                                                  #
# ========================================================================= #


def detect_color_support(env=None):
    """
    Detect the largest color palette supported by the terminal.
    :return: one of ANSI_MONOCHROME|ANSI_3_BIT_COLOR|ANSI_4_BIT_COLOR|ANSI_8_BIT_COLOR|ANSI_24_BIT_COLOR
    """

    if env is None:
        import os
        env = os.environ

    def is_enabled(string):
        # all right, alright, very well, of course, by all means, sure,
        # certainly, absolutely, indeed, affirmative, agreed, roger, aye
        # yeah, yah, yep, yup, uh-huh, okay, ok, okey-dokey, okey-doke, righty-ho
        return string.lower() in {'1', 'on', 'y', 'yes', 'enable', 'enabled'}

    if is_enabled(env.get('KOLR_FORCE_MONO', '0')):
        return ANSI_MONO_COLOR
    elif is_enabled(env.get('KOLR_FORCE_3_BIT', '0')):
        return ANSI_3_BIT_COLOR
    elif is_enabled(env.get('KOLR_FORCE_4_BIT', '0')):
        return ANSI_4_BIT_COLOR
    elif is_enabled(env.get('KOLR_FORCE_8_BIT', '0')):
        return ANSI_8_BIT_COLOR
    elif is_enabled(env.get('KOLR_FORCE_24_BIT', '0')):
        return ANSI_24_BIT_COLOR

    # if we are not a tty
    import sys
    if not sys.stdout.isatty():
        return ANSI_MONO_COLOR

    if env.get('TERM', None) == 'dumb':
        return ANSI_MONO_COLOR

    # Windows 10 build 10586 is the first to support 8-bit colors.
    # Windows 10 build 14931 is the first to support 24-bit colors.
    import platform
    if 'win32' in platform.platform():
        version = platform.version().split('.')
        if int(version[0]) > 10 and (int(version[2]) >= 10586):
            return ANSI_24_BIT_COLOR if (int(version[2]) >= 14931) else ANSI_8_BIT_COLOR
        return ANSI_8_BIT_COLOR

    if 'CI' in env:
        if any(key in env for key in ['TRAVIS', 'CIRCLECI', 'APPVEYOR', 'GITLAB_CI']):
            return ANSI_4_BIT_COLOR
        if env.get('CI_NAME', None) == 'codeship':
            return ANSI_4_BIT_COLOR

    if env.get('TEAMCITY_VERSION', None):
        # return /^(9\.(0*[1-9]\d*)\.|\d{2,}\.)/.test(env.TEAMCITY_VERSION) ? 1 : 0
        return ANSI_4_BIT_COLOR

    colorterm_env = env.get('COLORTERM', None)
    if colorterm_env:
        if colorterm_env in {'truecolor', '24bit'}:
            return ANSI_24_BIT_COLOR
        if colorterm_env in {'8bit'}:
            return ANSI_8_BIT_COLOR

    # TODO: replace with dedicated terminal detection
    termprog_env = env.get('TERM_PROGRAM', None)
    if termprog_env:
        if termprog_env in {'iTerm.app'}:
            version = int(env.get('TERM_PROGRAM_VERSION', '2').split('.')[0])
            return ANSI_24_BIT_COLOR if version >= 3 else ANSI_8_BIT_COLOR
        if termprog_env in {'Hyper'}:
            return ANSI_24_BIT_COLOR
        if termprog_env in {'Apple_Terminal'}:
            return ANSI_8_BIT_COLOR

    term_env = env.get('TERM', None)
    if term_env:
        if term_env in {'screen-256', 'screen-256color', 'xterm-256', 'xterm-256color'} or ('-256' in term_env):
            return ANSI_8_BIT_COLOR
        if term_env in {'screen', 'xterm', 'vt100', 'vt220', 'rxvt', 'color', 'ansi', 'cygwin', 'linux'}:
            return ANSI_4_BIT_COLOR

    if colorterm_env:
        # if there was no match with $TERM either but we
        # had one with $COLORTERM, we use it!
        return ANSI_4_BIT_COLOR

    return ANSI_3_BIT_COLOR  # return ANSI_3_MONO_COLOR


# ========================================================================= #
# DETECT                                                                    #
# ========================================================================= #


COLOR_SUPPORT = detect_color_support()

MAX_IS_MONO   = (COLOR_SUPPORT == ANSI_MONO_COLOR)
MAX_IS_3_BIT  = (COLOR_SUPPORT == ANSI_3_BIT_COLOR)
MAX_IS_4_BIT  = (COLOR_SUPPORT == ANSI_4_BIT_COLOR)
MAX_IS_8_BIT  = (COLOR_SUPPORT == ANSI_8_BIT_COLOR)
MAX_IS_24_BIT = (COLOR_SUPPORT == ANSI_24_BIT_COLOR)

ALLOWS_MONO   = (COLOR_SUPPORT >= ANSI_MONO_COLOR)
ALLOWS_3_BIT  = (COLOR_SUPPORT >= ANSI_3_BIT_COLOR)
ALLOWS_4_BIT  = (COLOR_SUPPORT >= ANSI_4_BIT_COLOR)
ALLOWS_8_BIT  = (COLOR_SUPPORT >= ANSI_8_BIT_COLOR)
ALLOWS_24_BIT = (COLOR_SUPPORT >= ANSI_24_BIT_COLOR)

NO_SUPPORT = MAX_IS_MONO


# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    print('Detected Number of Support Colors:', COLOR_SUPPORT)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
