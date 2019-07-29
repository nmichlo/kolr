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


# ========================================================================= #
# TERMINAL VARS                                                             #
# ========================================================================= #


# Valid TERMINAL_EMULATOR options:
TERM__JETBRAINS_JEDITERM = 'JetBrains-JediTerm'  # TERMINAL_EMULATOR=JetBrains-JediTerm, TERM=xterm-256color

# List of valid options for TERMINAL_EMULATOR:
TERMINAL_EMULATORS = {
    TERM__JETBRAINS_JEDITERM,
}

# Valid TERM_PROGRAM options:
TERM__HYPER= 'Hyper'                  # Hyper: TERM_PROGRAM=Hyper, TERM=xterm-256color
TERM__ITERM_APP= 'iTerm.app'          # iTerm: TERM=xterm-256color, TERM_PROGRAM=iTerm.app
TERM__TERMINAL_APP= 'Apple_Terminal'  # Terminal.app: TERM=xterm-256color, TERM_PROGRAM=Apple_Terminal

# List of valid options for TERM_PROGRAM:
TERM_PROGRAMS = {
    TERM__HYPER,
    TERM__ITERM_APP,
    TERM__TERMINAL_APP,
}

# Other Terminal:
TERM__COOL_RETRO_TERM = 'cool-retro-term'
TERM__KITTY = 'kitty'
TERM__ALACRITTY = 'alacritty'


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
        if termprog_env in TERM_PROGRAMS:
            return termprog_env
        print(f'TERM_PROGRAM does not match, please report this: {os.environ}\n')

    termemulator_env = os.environ.get('TERMINAL_EMULATOR', None)
    if termemulator_env:
        if termemulator_env in TERMINAL_EMULATORS:
            return termemulator_env
        print(f'TERMINAL_EMULATOR does not match, please report this: {os.environ}\n')

    if TERM__COOL_RETRO_TERM in os.environ.get('KB_LAYOUT_DIR', '') or TERM__COOL_RETRO_TERM in os.environ.get('COLORSCHEMES_DIR', ''):
        # cool-retro-term: TERM=xterm, KB_LAYOUT_DIR: /Applications/cool-retro-term.app/Contents/MacOS/../PlugIns/QMLTermWidget/kb-layouts, COLORSCHEMES_DIR: /Applications/cool-retro-term.app/Contents/MacOS/../PlugIns/QMLTermWidget/color-schemes
        return TERM__COOL_RETRO_TERM
    if os.environ.get('ALACRITTY_LOG', None) is not None:
        # Alacritty: # TERM=xterm-256color ALACRITTY_LOG=/var/folders/.../T/Alacritty-68540.log
        return TERM__ALACRITTY
    if (os.environ.get('KITTY_WINDOW_ID', None) is not None) or (TERM__KITTY in os.environ.get('TERMINFO', '')) or (TERM__KITTY in os.environ.get('TERM', '')):
        # Kitty: KITTY_WINDOW_ID=1, TERMINFO=/Applications/kitty.app/Contents/Frameworks/kitty/..., TERM=xterm-kitty
        return TERM__KITTY

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


TERMINAL = detect_terminal()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


if __name__ == '__main__':
    print('Detected Terminal:', TERMINAL)
