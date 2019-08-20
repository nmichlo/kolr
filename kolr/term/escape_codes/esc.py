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
# Escape Character                                                          #
# ∙ octal=\033 ∙ hex=\x1B ∙ decimal=27 ∙ keyboard=^[                        #
# ========================================================================= #


ESC = '\033'


# ========================================================================= #
# Escape sequences                                                          #
# ∙ ESC ...                                                                 #
# ∙ https://invisible-island.net/xterm/ctlseqs/ctlseqs.html                 #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences         #
# ∙ http://www.termsys.demon.co.uk/vtansi.htm                               #
# ∙ https://wiki.bash-hackers.org/scripting/terminalcodes                   #
# ========================================================================= #


# C1 (8-Bit) Control Characters
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
IND   = ESC + 'D'  #  \x84  #  IND    # Index                        #
NEL   = ESC + 'E'  #  \x85  #  NEL    # Next Line                    #
HTS   = ESC + 'H'  #  \x88  #  HTS    # Tab Set                      #
RI    = ESC + 'M'  #  \x8d  #  RI     # Reverse Index                #
SS2   = ESC + 'N'  #  \x8e  #  SS2    # Single Shift Two             #  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
SS3   = ESC + 'O'  #  \x8f  #  SS3    # Single Shift Three           #  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
DCS   = ESC + 'P'  #  \x90  #  DCS    # Device Control String        #  Terminated by ST. Xterm's uses of this sequence include defining User-Defined Keys, and requesting or setting Termcap/Terminfo data.
SPA   = ESC + 'V'  #  \x96  #  SPA    # Start of Guarded Area        #
EPA   = ESC + 'W'  #  \x97  #  EPA    # End of Guarded Area          #
SOS   = ESC + 'X'  #  \x98  #  SOS    # Start of String              #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
DECID = ESC + 'Z'  #  \x9a  #  DECID  # Return Terminal ID           #  Obsolete form of CSI c (DA).
CSI   = ESC + '['  #  \x9b  #  CSI    # Control Sequence Introducer  #  Most of the useful sequences, see next section.
ST    = ESC + '\\' #  \x9c  #  ST     # String Terminator            #  Terminates strings in other controls.:8.3.143
OSC   = ESC + ']'  #  \x9d  #  OSC    # Operating System Command     #  Starts a control string for the operating system to use, terminated by ST.:8.3.89 In xterm, they may also be terminated by BEL. In xterm, the curses_screen title can be set by OSC 0;this is the curses_screen title BEL.
PM    = ESC + '^'  #  \x9e  #  PM     # Privacy Message              #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
APC   = ESC + '_'  #  \x9f  #  APC    # Application Program Command  #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
RIS   = ESC + 'c'  #  None  #  RIS    # Reset to Initial State       #  Resets the device to its original state.  This may include (if applicable): reset graphic rendition, clear tabulation stops, reset to default font, and more.


# ========================================================================= \#
# END                                                                       \#
# ========================================================================= \#
