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

#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#
#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
#
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #


from kolr.term.escape_codes.esc import CSI


# ========================================================================= #
# CSI SEQUENCES (Control Sequence Introducer)                               #
# ∙ CSI = ESC [ ...                                                         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences            #
# ========================================================================= #


cuu = lambda n:     f'{CSI}{n}A'      #  CUU   # Cursor Up                    # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
cud = lambda n:     f'{CSI}{n}B'      #  CUD   # Cursor Down                  # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
cuf = lambda n:     f'{CSI}{n}C'      #  CUF   # Cursor Forward               # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
cub = lambda n:     f'{CSI}{n}D'      #  CUB   # Cursor Back                  # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
cnl = lambda n:     f'{CSI}{n}E'      #  CNL   # Cursor Next Line             # Moves cursor to beginning of the line n (default 1) lines down.  (not ANSI.SYS)
cpl = lambda n:     f'{CSI}{n}F'      #  CPL   # Cursor Previous Line         # Moves cursor to beginning of the line n (default 1) lines up.  (not ANSI.SYS)
cha = lambda n:     f'{CSI}{n}G'      #  CHA   # Cursor Horizontal Absolute   # Moves the cursor to column n (default 1).  (not ANSI.SYS)
cup = lambda y, x:  f'{CSI}{y};{x}H'  #  CUP   # Cursor Position              # Moves the cursor to row y, column x.  The values are 1-based, and default to 1 (top left corner) if omitted.  A sequence such as CSI ;5H is a synonym for CSI 1;5H as well as CSI 17;H is the same as CSI 17H and CSI 17;1H
ed  = lambda n:     f'{CSI}{n}J'      #  ED    # Erase in Display             # Clears part of the screen. If n is 0 (or missing), clear from cursor to end of screen. If n is 1, clear from cursor to beginning of the screen. If n is 2, clear entire screen (and moves cursor to upper left on DOS ANSI.SYS).  If n is 3, clear entire screen and delete all lines saved in the scrollback buffer (this feature was added for xterm and is supported by other terminal applications).
el  = lambda n:     f'{CSI}{n}K'      #  EL    # Erase in Line                # Erases part of the line. If n is 0 (or missing), clear from cursor to the end of the line. If n is 1, clear from cursor to beginning of the line. If n is 2, clear entire line.  Cursor position does not change.
su  = lambda n:     f'{CSI}{n}S'      #  SU    # Scroll Up                    # Scroll whole page up by n (default 1) lines.  New lines are added at the bottom.  (not ANSI.SYS)
sd  = lambda n:     f'{CSI}{n}T'      #  SD    # Scroll Down                  # Scroll whole page down by n (default 1) lines.  New lines are added at the top.  (not ANSI.SYS)
hvp = lambda y, x:  f'{CSI}{y};{x}f'  #  HVP   # Horizontal Vertical Position # Same as CUP
sgr = lambda *code: f'{CSI}{";".join(str(c) for c in code)}m'  #  SGR   # Select Graphic Rendition     # Sets the appearance of the following characters, see SGR parameters below.
APE = CSI + '5i'                      #  APE?  # AUX Port On                  # Enable aux serial port usually for local serial printer
APD = CSI + '4i'                      #  APD?  # AUX Port Off                 # Disable aux serial port usually for local serial printer
DSR = CSI + '6n'                      #  DSR   # Device Status Report         # Reports the cursor position (CPR) to the application as (as though typed at the keyboard) ESC[n;mR, where n is the row and m is the column.)
SCP = CSI + 's'                       #  SCP   # Save Cursor Position         # Saves the cursor position/state.
RCP = CSI + 'u'                       #  RCP   # Restore Cursor Position      # Restores the cursor position/state.

CS  = CSI + '?25h'                    #  CS?   # Show Cursor                  # DECTCEM Shows the cursor, from the VT320.
CH  = CSI + '?25l'                    #  CH?   # Hide Cursor                  # DECTCEM Hides the cursor.
SBE = CSI + '?1049h'                  #  SBE?  # Enable Screen Buffer         # Enable alternative screen buffer
SBD = CSI + '?1049l'                  #  SBD?  # Disable Screen Buffer        # Disable alternative screen buffer
BPE = CSI + '?2004h'                  #  BPE?  # Enable Bracket Paste         # Turn on bracketed paste mode. Text pasted into the terminal will be surrounded by ESC  From Unix terminal emulators.
BPD = CSI + '?2004l'                  #  BPD?  # Disable Bracked Paste        # Turn off bracketed paste mode.


# ========================================================================= \#
# END                                                                       \#
# ========================================================================= \#
