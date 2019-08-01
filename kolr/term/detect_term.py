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


# ========================================================================= #
# TERMINAL VARS                                                             #
# ========================================================================= #


# Valid TERMINAL_EMULATOR options:
CODE__JETBRAINS_JEDITERM = 'JetBrains-JediTerm'  # TERMINAL_EMULATOR=JetBrains-JediTerm, TERM=xterm-256color

# List of valid options for TERMINAL_EMULATOR:
_TERMINAL_EMULATORS = {
    CODE__JETBRAINS_JEDITERM,
}

# Valid TERM_PROGRAM options:
CODE__HYPER= 'Hyper'                  # Hyper: TERM_PROGRAM=Hyper, TERM=xterm-256color
CODE__ITERM_APP= 'iTerm.app'          # iTerm: TERM=xterm-256color, TERM_PROGRAM=iTerm.app
CODE__TERMINAL_APP= 'Apple_Terminal'  # Terminal.app: TERM=xterm-256color, TERM_PROGRAM=Apple_Terminal

# List of valid options for TERM_PROGRAM:
_TERM_PROGRAMS = {
    CODE__HYPER,
    CODE__ITERM_APP,
    CODE__TERMINAL_APP,
}

# Other Terminal:
CODE__COOL_RETRO_TERM = 'cool-retro-term'
CODE__KITTY = 'kitty'
CODE__ALACRITTY = 'alacritty'


# ========================================================================= #
# DETECTOR                                                                  #
# ========================================================================= #


def detect_terminal():
    """
    Naive attempt to detect the terminal program.
    TODO: This needs a lot of work, could merge detect color and detect termial logic?
    :return: possible detected terminal
    """
    import os

    termprog_env = os.environ.get('TERM_PROGRAM', None)
    if termprog_env:
        if termprog_env in _TERM_PROGRAMS:
            return termprog_env
        print(f'TERM_PROGRAM does not match, please report this: {os.environ}\n')

    termemulator_env = os.environ.get('TERMINAL_EMULATOR', None)
    if termemulator_env:
        if termemulator_env in _TERMINAL_EMULATORS:
            return termemulator_env
        print(f'TERMINAL_EMULATOR does not match, please report this: {os.environ}\n')

    if CODE__COOL_RETRO_TERM in os.environ.get('KB_LAYOUT_DIR', '') or CODE__COOL_RETRO_TERM in os.environ.get('COLORSCHEMES_DIR', ''):
        # cool-retro-term: TERM=xterm, KB_LAYOUT_DIR: /Applications/cool-retro-term.app/Contents/MacOS/../PlugIns/QMLTermWidget/kb-layouts, COLORSCHEMES_DIR: /Applications/cool-retro-term.app/Contents/MacOS/../PlugIns/QMLTermWidget/color-schemes
        return CODE__COOL_RETRO_TERM
    if os.environ.get('ALACRITTY_LOG', None) is not None:
        # Alacritty: # TERM=xterm-256color ALACRITTY_LOG=/var/folders/.../T/Alacritty-68540.log
        return CODE__ALACRITTY
    if (os.environ.get('KITTY_WINDOW_ID', None) is not None) or (CODE__KITTY in os.environ.get('TERMINFO', '')) or (CODE__KITTY in os.environ.get('TERM', '')):
        # Kitty: KITTY_WINDOW_ID=1, TERMINFO=/Applications/kitty.app/Contents/Frameworks/kitty/..., TERM=xterm-kitty
        return CODE__KITTY

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

    print(f'Unable to match terminal, please report this: {os.environ}\n')

    return None


# ========================================================================= #
# DETECT                                                                    #
# ========================================================================= #


DETECTED_TERMINAL = detect_terminal()


# ========================================================================= #
# TERMINAL COLORS                                                           #
# ========================================================================= #


_4_BIT_COLOR_INFO = [
    ('Black',          {'vga': (0, 0, 0),       'windows_console': (0, 0, 0),       'windows_powershell': (0, 0, 0),       'windows_10_consolepowershell_6': (12, 12, 12),    'terminal_app': (0, 0, 0),       'putty': (0, 0, 0),       'mirc': (0, 0, 0),       'xterm': (0, 0, 0),       'x': (0, 0, 0),       'ubuntu': (1, 1, 1)      }),
    ('Red',            {'vga': (170, 0, 0),     'windows_console': (128, 0, 0),     'windows_powershell': (128, 0, 0),     'windows_10_consolepowershell_6': (197, 15, 31),   'terminal_app': (194, 54, 33),   'putty': (187, 0, 0),     'mirc': (127, 0, 0),     'xterm': (205, 0, 0),     'x': (255, 0, 0),     'ubuntu': (222, 56, 43)  }),
    ('Green',          {'vga': (0, 170, 0),     'windows_console': (0, 128, 0),     'windows_powershell': (0, 128, 0),     'windows_10_consolepowershell_6': (19, 161, 14),   'terminal_app': (37, 188, 36),   'putty': (0, 187, 0),     'mirc': (0, 147, 0),     'xterm': (0, 205, 0),     'x': (0, 255, 0),     'ubuntu': (57, 181, 74)  }),
    ('Yellow',         {'vga': (170, 85, 0),    'windows_console': (128, 128, 0),   'windows_powershell': (238, 237, 240), 'windows_10_consolepowershell_6': (193, 156, 0),   'terminal_app': (173, 173, 39),  'putty': (187, 187, 0),   'mirc': (252, 127, 0),   'xterm': (205, 205, 0),   'x': (255, 255, 0),   'ubuntu': (255, 199, 6)  }),
    ('Blue',           {'vga': (0, 0, 170),     'windows_console': (0, 0, 128),     'windows_powershell': (0, 0, 128),     'windows_10_consolepowershell_6': (0, 55, 218),    'terminal_app': (73, 46, 225),   'putty': (0, 0, 187),     'mirc': (0, 0, 127),     'xterm': (0, 0, 238),     'x': (0, 0, 255),     'ubuntu': (0, 111, 184)  }),
    ('Magenta',        {'vga': (170, 0, 170),   'windows_console': (128, 0, 128),   'windows_powershell': (1, 36, 86),     'windows_10_consolepowershell_6': (136, 23, 152),  'terminal_app': (211, 56, 211),  'putty': (187, 0, 187),   'mirc': (156, 0, 156),   'xterm': (205, 0, 205),   'x': (255, 0, 255),   'ubuntu': (118, 38, 113) }),
    ('Cyan',           {'vga': (0, 170, 170),   'windows_console': (0, 128, 128),   'windows_powershell': (0, 128, 128),   'windows_10_consolepowershell_6': (58, 150, 221),  'terminal_app': (51, 187, 200),  'putty': (0, 187, 187),   'mirc': (0, 147, 147),   'xterm': (0, 205, 205),   'x': (0, 255, 255),   'ubuntu': (44, 181, 233) }),
    ('White',          {'vga': (170, 170, 170), 'windows_console': (192, 192, 192), 'windows_powershell': (192, 192, 192), 'windows_10_consolepowershell_6': (204, 204, 204), 'terminal_app': (203, 204, 205), 'putty': (187, 187, 187), 'mirc': (210, 210, 210), 'xterm': (229, 229, 229), 'x': (255, 255, 255), 'ubuntu': (204, 204, 204)}),
    ('Bright Black',   {'vga': (85, 85, 85),    'windows_console': (128, 128, 128), 'windows_powershell': (128, 128, 128), 'windows_10_consolepowershell_6': (118, 118, 118), 'terminal_app': (129, 131, 131), 'putty': (85, 85, 85),    'mirc': (127, 127, 127), 'xterm': (127, 127, 127), 'x': None,            'ubuntu': (128, 128, 128)}),
    ('Bright Red',     {'vga': (255, 85, 85),   'windows_console': (255, 0, 0),     'windows_powershell': (255, 0, 0),     'windows_10_consolepowershell_6': (231, 72, 86),   'terminal_app': (252, 57, 31),   'putty': (255, 85, 85),   'mirc': (255, 0, 0),     'xterm': (255, 0, 0),     'x': None,            'ubuntu': (255, 0, 0)    }),
    ('Bright Green',   {'vga': (85, 255, 85),   'windows_console': (0, 255, 0),     'windows_powershell': (0, 255, 0),     'windows_10_consolepowershell_6': (22, 198, 12),   'terminal_app': (49, 231, 34),   'putty': (85, 255, 85),   'mirc': (0, 252, 0),     'xterm': (0, 255, 0),     'x': (144, 238, 144), 'ubuntu': (0, 255, 0)    }),
    ('Bright Yellow',  {'vga': (255, 255, 85),  'windows_console': (255, 255, 0),   'windows_powershell': (255, 255, 0),   'windows_10_consolepowershell_6': (249, 241, 165), 'terminal_app': (234, 236, 35),  'putty': (255, 255, 85),  'mirc': (255, 255, 0),   'xterm': (255, 255, 0),   'x': (255, 255, 224), 'ubuntu': (255, 255, 0)  }),
    ('Bright Blue',    {'vga': (85, 85, 255),   'windows_console': (0, 0, 255),     'windows_powershell': (0, 0, 255),     'windows_10_consolepowershell_6': (59, 120, 255),  'terminal_app': (88, 51, 255),   'putty': (85, 85, 255),   'mirc': (0, 0, 252),     'xterm': (92, 92, 255),   'x': (173, 216, 230), 'ubuntu': (0, 0, 255)    }),
    ('Bright Magenta', {'vga': (255, 85, 255),  'windows_console': (255, 0, 255),   'windows_powershell': (255, 0, 255),   'windows_10_consolepowershell_6': (180, 0, 158),   'terminal_app': (249, 53, 248),  'putty': (255, 85, 255),  'mirc': (255, 0, 255),   'xterm': (255, 0, 255),   'x': None,            'ubuntu': (255, 0, 255)  }),
    ('Bright Cyan',    {'vga': (85, 255, 255),  'windows_console': (0, 255, 255),   'windows_powershell': (0, 255, 255),   'windows_10_consolepowershell_6': (97, 214, 214),  'terminal_app': (20, 240, 240),  'putty': (85, 255, 255),  'mirc': (0, 255, 255),   'xterm': (0, 255, 255),   'x': (224, 255, 255), 'ubuntu': (0, 255, 255)  }),
    ('Bright White',   {'vga': (255, 255, 255), 'windows_console': (255, 255, 255), 'windows_powershell': (255, 255, 255), 'windows_10_consolepowershell_6': (242, 242, 242), 'terminal_app': (233, 235, 235), 'putty': (255, 255, 255), 'mirc': (255, 255, 255), 'xterm': (255, 255, 255), 'x': None,            'ubuntu': (255, 255, 255)}),
]


def get_detected_4bit_colors():
    term = DETECTED_TERMINAL if (DETECTED_TERMINAL in _4_BIT_COLOR_INFO[0][1]) else 'xterm'
    return [(name, colors[term]) for name, colors in _4_BIT_COLOR_INFO]


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


if __name__ == '__main__':
    print('Detected Terminal:', DETECTED_TERMINAL)
