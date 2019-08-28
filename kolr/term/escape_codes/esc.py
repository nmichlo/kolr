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


from kolr.term.escape_codes._params import C, Ps, Pm, Pt


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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# C1 (8-Bit) Control Characters
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


#   The xterm program recognizes both 8-bit and 7-bit control characters.
#   It generates 7-bit controls (by default) or 8-bit if S8C1T is enabled.
#   The following pairs of 7-bit and 8-bit control characters are equiva-
#   lent:

IND   = ESC + 'D'   # IND   | Index                        | \x84 |
NEL   = ESC + 'E'   # NEL   | Next Line                    | \x85 |
HTS   = ESC + 'H'   # HTS   | Tab Set                      | \x88 |
RI    = ESC + 'M'   # RI    | Reverse Index                | \x8d |
SS2   = ESC + 'N'   # SS2   | Single Shift Two             | \x8e |  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
SS3   = ESC + 'O'   # SS3   | Single Shift Three           | \x8f |  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
DCS   = ESC + 'P'   # DCS   | Device Control String        | \x90 |  Terminated by ST. Xterm's uses of this sequence include defining User-Defined Keys, and requesting or setting Termcap/Terminfo data.
SPA   = ESC + 'V'   # SPA   | Start of Guarded Area        | \x96 |
EPA   = ESC + 'W'   # EPA   | End of Guarded Area          | \x97 |
SOS   = ESC + 'X'   # SOS   | Start of String              | \x98 |  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
DECID = ESC + 'Z'   # DECID | Return Terminal ID           | \x9a |  Obsolete form of CSI c (DA).
CSI   = ESC + '['   # CSI   | Control Sequence Introducer  | \x9b |  Most of the useful sequences, see next section.
ST    = ESC + '\\'  # ST    | String Terminator            | \x9c |  Terminates strings in other controls.:8.3.143
OSC   = ESC + ']'   # OSC   | Operating System Command     | \x9d |  Starts a control string for the operating system to use, terminated by ST.:8.3.89 In xterm, they may also be terminated by BEL. In xterm, the curses_screen title can be set by OSC 0;this is the curses_screen title BEL.
PM    = ESC + '^'   # PM    | Privacy Message              | \x9e |  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
APC   = ESC + '_'   # APC   | Application Program Command  | \x9f |  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.

#   These control characters are used in the vtXXX emulation.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Controls beginning with ESC
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Controls-beginning-with-ESC
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# This excludes controls where ESC  is part of a 7-bit equivalent to 8-bit
# C1 controls, ordered by the final character(s).

S7C1T      = ESC + ' F'  # ESC SP F   | 7-bit controls (S7C1T), VT220.  This tells the terminal to send C1 control characters as 7-bit sequences, e.g., its responses to queries.  DEC VT200 and up always accept 8-bit control sequences except when configured for VT100 mode.
S8C1T      = ESC + ' G'  # ESC SP G   | 8-bit controls (S8C1T), VT220.  This tells the terminal to send C1 control characters as 8-bit sequences, e.g., its responses to queries.  DEC VT200 and up always accept 8-bit control sequences except when configured for VT100 mode.
_ACL1      = ESC + ' L'  # ESC SP L   | Set ANSI conformance level 1 (dpANS X3.134.1).
_ACL2      = ESC + ' M'  # ESC SP M   | Set ANSI conformance level 2 (dpANS X3.134.1).
_ACL3      = ESC + ' N'  # ESC SP N   | Set ANSI conformance level 3 (dpANS X3.134.1).
DECDHL_top = ESC + '#3'  # ESC # 3    | DEC double-height line, top half (DECDHL), VT100.
DECDHL_btm = ESC + '#4'  # ESC # 4    | DEC double-height line, bottom half (DECDHL), VT100.
DECSWL     = ESC + '#5'  # ESC # 5    | DEC single-width line (DECSWL), VT100.
DECDWL     = ESC + '#6'  # ESC # 6    | DEC double-width line (DECDWL), VT100.
DECALN     = ESC + '#8'  # ESC # 8    | DEC Screen Alignment Test (DECALN), VT100.
_CSD       = ESC + '%@'  # ESC % @    | Select default character set.  That is ISO 8859-1 (ISO 2022).
_CSU       = ESC + '%G'  # ESC % G    | Select UTF-8 character set, ISO 2022.
_dcs0v100  = ESC + '(' + C['A', 'B', '4', 'C', '5', 'R', 'f', 'Q', '9', 'K', '"', '%=', 'Y', '`', 'E', '6', '%6', 'Z', 'H', '7', '=', '%2', '0', '<', '>', '%5', '&4', '"?', '"4', '%0', '&5', '%3']  # ESC ( C    | Designate G0 Character Set, ISO 2022, VT100. Final character C for designating 94-character sets.
_dcs1v100  = ESC + ')' + C['A', 'B', '4', 'C', '5', 'R', 'f', 'Q', '9', 'K', '"', '%=', 'Y', '`', 'E', '6', '%6', 'Z', 'H', '7', '=', '%2', '0', '<', '>', '%5', '&4', '"?', '"4', '%0', '&5', '%3']  # ESC ) C    | Designate G1 Character Set, ISO 2022, VT100. The same character sets apply as for ESC ( C.
_dcs2v220  = ESC + '*' + C['A', 'B', '4', 'C', '5', 'R', 'f', 'Q', '9', 'K', '"', '%=', 'Y', '`', 'E', '6', '%6', 'Z', 'H', '7', '=', '%2', '0', '<', '>', '%5', '&4', '"?', '"4', '%0', '&5', '%3']  # ESC * C    | Designate G2 Character Set, ISO 2022, VT220. The same character sets apply as for ESC ( C.
_dcs3v220  = ESC + '+' + C['A', 'B', '4', 'C', '5', 'R', 'f', 'Q', '9', 'K', '"', '%=', 'Y', '`', 'E', '6', '%6', 'Z', 'H', '7', '=', '%2', '0', '<', '>', '%5', '&4', '"?', '"4', '%0', '&5', '%3']  # ESC + C    | Designate G3 Character Set, ISO 2022, VT220. The same character sets apply as for ESC ( C.
_dcs1v300  = ESC + '-' + C['A', 'F', 'H', 'L', 'M']  # ESC - C    | Designate G1 Character Set, VT300. Final character C for designating 96-character sets. Unlike 94 can have different values than ASCII space and DEL for the mapping of 0x20 and 0x7f.
_dcs2v300  = ESC + '.' + C['A', 'F', 'H', 'L', 'M']  # ESC . C    | Designate G2 Character Set, VT300. The same character sets apply as for ESC - C.
_dcs3v300  = ESC + '/' + C['A', 'F', 'H', 'L', 'M']  # ESC / C    | Designate G3 Character Set, VT300. The same character sets apply as for ESC - C.
DECBI      = ESC + '6'   # ESC 6      | Back Index (DECBI), VT420 and up.
DECSC      = ESC + '7'   # ESC 7      | Save Cursor (DECSC), VT100.
DECRC      = ESC + '8'   # ESC 8      | Restore Cursor (DECRC), VT100.
DECFI      = ESC + '9'   # ESC 9      | Forward Index (DECFI), VT420 and up.
DECKPAM    = ESC + '='   # ESC =      | Application Keypad (DECKPAM).
DECKPNM    = ESC + '>'   # ESC >      | Normal Keypad (DECKPNM), VT100.
_CLL       = ESC + 'F'   # ESC F      | Cursor to lower left corner of screen.  This is enabled by the hpLowerleftBugCompat resource.
RIS        = ESC + 'c'   # ESC c      | Full Reset / Reset to Initial State (RIS), VT100. | Resets the device to its original state.  This may include (if applicable): reset graphic rendition, clear tabulation stops, reset to default font, and more.
_ML        = ESC + 'l'   # ESC l      | Memory Lock (per HP terminals).  Locks memory above the cursor.
_MU        = ESC + 'm'   # ESC m      | Memory Unlock (per HP terminals).
LS2        = ESC + 'n'   # ESC n      | Invoke the G2 Character Set as GL (LS2) as GL.
LS3        = ESC + 'o'   # ESC o      | Invoke the G3 Character Set as GL (LS3) as GL.
LS3R       = ESC + '|'   # ESC |      | Invoke the G3 Character Set as GR (LS3R).
LS2R       = ESC + '}'   # ESC }      | Invoke the G2 Character Set as GR (LS2R).
LS1R       = ESC + '~'   # ESC ~      | Invoke the G1 Character Set as GR (LS1R), VT100.


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
