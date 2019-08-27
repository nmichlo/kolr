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


# # C1 (8-Bit) Control Characters
# # https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
# IND   = ESC + 'D'  #  \x84  #  IND    # Index                        #
# NEL   = ESC + 'E'  #  \x85  #  NEL    # Next Line                    #
# HTS   = ESC + 'H'  #  \x88  #  HTS    # Tab Set                      #
# RI    = ESC + 'M'  #  \x8d  #  RI     # Reverse Index                #
# SS2   = ESC + 'N'  #  \x8e  #  SS2    # Single Shift Two             #  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
# SS3   = ESC + 'O'  #  \x8f  #  SS3    # Single Shift Three           #  Selects a single character from one of the alternative character sets. In xterm, SS2 selects the G2 character set, and SS3 selects the G3 character set.
# DCS   = ESC + 'P'  #  \x90  #  DCS    # Device Control String        #  Terminated by ST. Xterm's uses of this sequence include defining User-Defined Keys, and requesting or setting Termcap/Terminfo data.
# SPA   = ESC + 'V'  #  \x96  #  SPA    # Start of Guarded Area        #
# EPA   = ESC + 'W'  #  \x97  #  EPA    # End of Guarded Area          #
# SOS   = ESC + 'X'  #  \x98  #  SOS    # Start of String              #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
# DECID = ESC + 'Z'  #  \x9a  #  DECID  # Return Terminal ID           #  Obsolete form of CSI c (DA).
# CSI   = ESC + '['  #  \x9b  #  CSI    # Control Sequence Introducer  #  Most of the useful sequences, see next section.
# ST    = ESC + '\\' #  \x9c  #  ST     # String Terminator            #  Terminates strings in other controls.:8.3.143
# OSC   = ESC + ']'  #  \x9d  #  OSC    # Operating System Command     #  Starts a control string for the operating system to use, terminated by ST.:8.3.89 In xterm, they may also be terminated by BEL. In xterm, the curses_screen title can be set by OSC 0;this is the curses_screen title BEL.
# PM    = ESC + '^'  #  \x9e  #  PM     # Privacy Message              #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
# APC   = ESC + '_'  #  \x9f  #  APC    # Application Program Command  #  Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application:8.3.2,8.3.128 or privacy discipline.:8.3.94  These functions are not implemented and the arguments are ignored by xterm.
# RIS   = ESC + 'c'  #  None  #  RIS    # Reset to Initial State       #  Resets the device to its original state.  This may include (if applicable): reset graphic rendition, clear tabulation stops, reset to default font, and more.


# ========================================================================= #
# C1 (8-Bit) Control Characters                                             #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
# Comments are from https://invisible-island.net/xterm/ctlseqs/ctlseqs.html #
# Only non-comment code is from Nathan Michlo                               #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#                         XTerm Control Sequences                           #
#                                                                           #
#                                Edward Moy                                 #
#                    University of California, Berkeley                     #
#                                                                           #
#                                Revised by                                 #
#                                                                           #
#                              Stephen Gildea                               #
#                           X Consortium (1994)                             #
#                                                                           #
#                              Thomas Dickey                                #
#                       XFree86 Project (1996-2006)                         #
#                     invisible-island.net (2006-2019)                      #
#                updated for XTerm Patch #348 (2019/07/11)                  #
# ========================================================================= #


# The xterm program recognizes both 8-bit and 7-bit control characters.
# It generates 7-bit controls (by default) or 8-bit if S8C1T is enabled.
# The following pairs of 7-bit and 8-bit control characters are equiva-
# lent:

IND   = ESC + 'D'   # ESC D   | Index (IND  is 0x84).
NEL   = ESC + 'E'   # ESC E   | Next Line (NEL  is 0x85).
HTS   = ESC + 'H'   # ESC H   | Tab Set (HTS  is 0x88).
RI    = ESC + 'M'   # ESC M   | Reverse Index (RI  is 0x8d).
SS2   = ESC + 'N'   # ESC N   | Single Shift Select of G2 Character Set (SS2  is 0x8e), VT220. This affects next character only.
SS3   = ESC + 'O'   # ESC O   | Single Shift Select of G3 Character Set (SS3  is 0x8f), VT220. This affects next character only.
DCS   = ESC + 'P'   # ESC P   | Device Control String (DCS  is 0x90).
SPA   = ESC + 'V'   # ESC V   | Start of Guarded Area (SPA  is 0x96).
EPA   = ESC + 'W'   # ESC W   | End of Guarded Area (EPA  is 0x97).
SOS   = ESC + 'X'   # ESC X   | Start of String (SOS  is 0x98).
DECID = ESC + 'Z'   # ESC Z   | Return Terminal ID (DECID is 0x9a).  Obsolete form of CSI c  (DA).
CSI   = ESC + '['   # ESC [   | Control Sequence Introducer (CSI  is 0x9b).
ST    = ESC + '\\'  # ESC \   | String Terminator (ST  is 0x9c).
OSC   = ESC + ']'   # ESC ]   | Operating System Command (OSC  is 0x9d).
PM    = ESC + '^'   # ESC ^   | Privacy Message (PM  is 0x9e).
APC   = ESC + '_'   # ESC _   | Application Program Command (APC  is 0x9f).

# These control characters are used in the vtXXX emulation.


# ========================================================================= #
# Controls beginning with ESC                                               #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
# Comments are from https://invisible-island.net/xterm/ctlseqs/ctlseqs.html #
# Only non-comment code is from Nathan Michlo                               #
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~  #
#                         XTerm Control Sequences                           #
#                                                                           #
#                                Edward Moy                                 #
#                    University of California, Berkeley                     #
#                                                                           #
#                                Revised by                                 #
#                                                                           #
#                              Stephen Gildea                               #
#                           X Consortium (1994)                             #
#                                                                           #
#                              Thomas Dickey                                #
#                       XFree86 Project (1996-2006)                         #
#                     invisible-island.net (2006-2019)                      #
#                updated for XTerm Patch #348 (2019/07/11)                  #
# ========================================================================= #


# This excludes controls where ESC  is part of a 7-bit equivalent to 8-bit
# C1 controls, ordered by the final character(s).

S7C1T         = ESC + ' F'  # ESC SP F   | 7-bit controls (S7C1T), VT220.  This tells the terminal to send C1 control characters as 7-bit sequences, e.g., its responses to queries.  DEC VT200 and up always accept 8-bit control sequences except when configured for VT100 mode.
S8C1T         = ESC + ' G'  # ESC SP G   | 8-bit controls (S8C1T), VT220.  This tells the terminal to send C1 control characters as 8-bit sequences, e.g., its responses to queries.  DEC VT200 and up always accept 8-bit control sequences except when configured for VT100 mode.
_ACL1         = ESC + ' L'  # ESC SP L   | Set ANSI conformance level 1 (dpANS X3.134.1).
_ACL2         = ESC + ' M'  # ESC SP M   | Set ANSI conformance level 2 (dpANS X3.134.1).
_ACL3         = ESC + ' N'  # ESC SP N   | Set ANSI conformance level 3 (dpANS X3.134.1).
DECDHL_top    = ESC + '#3'  # ESC # 3    | DEC double-height line, top half (DECDHL), VT100.
DECDHL_bottom = ESC + '#4'  # ESC # 4    | DEC double-height line, bottom half (DECDHL), VT100.
DECSWL        = ESC + '#5'  # ESC # 5    | DEC single-width line (DECSWL), VT100.
DECDWL        = ESC + '#6'  # ESC # 6    | DEC double-width line (DECDWL), VT100.
DECALN        = ESC + '#8'  # ESC # 8    | DEC Screen Alignment Test (DECALN), VT100.
_CSD          = ESC + '%@'  # ESC % @    | Select default character set.  That is ISO 8859-1 (ISO 2022).
_CSU          = ESC + '%G'  # ESC % G    | Select UTF-8 character set, ISO 2022.

# ESC ( C   Designate G0 Character Set, VT100, ISO 2022.
#           Final character C for designating 94-character sets.  In this
#           list,
#           o   0 , A  and B  were introduced in the VT100,
#           o   most were introduced in the VT200 series,
#           o   a few were introduced in the VT300 series, and
#           o   a few more were introduced in the VT500 series.
#           The VT220 character sets, together with a few others (such as
#           Portuguese) are activated by the National Replacement Charac-
#           ter Set (NRCS) controls.  The term "replacement" says that the
#           character set is formed by replacing some of the characters in
#           a set (termed the Multinational Character Set) with more use-
#           ful ones for a given language.  The ASCII and DEC Supplemental
#           character sets make up the two halves of the Multinational
#           Character set, initially mapped to GL and GR.
#           The valid final characters C for this control are:
#             C = A  -> United Kingdom (UK), VT100.
#             C = B  -> United States (USASCII), VT100.
#             C = 4  -> Dutch, VT200.
#             C = C  or 5  -> Finnish, VT200.
#             C = R  or f  -> French, VT200.
#             C = Q  or 9  -> French Canadian, VT200.
#             C = K  -> German, VT200.
#             C = " >  -> Greek, VT500.
#             C = % =  -> Hebrew, VT500.
#             C = Y  -> Italian, VT200.
#             C = ` , E  or 6  -> Norwegian/Danish, VT200.
#             C = % 6  -> Portuguese, VT300.
#             C = Z  -> Spanish, VT200.
#             C = H  or 7  -> Swedish, VT200.
#             C = =  -> Swiss, VT200.
#             C = % 2  -> Turkish, VT500.
#           The final character A  is a special case, since the same final
#           character is used by the VT300-control for the 96-character
#           British Latin-1.
#           There are a few other 94-character sets:
#             C = 0  -> DEC Special Character and Line Drawing Set, VT100.
#             C = <  -> DEC Supplemental, VT200.
#             C = >  -> DEC Technical, VT300.
#           These are documented as NRCS:
#             C = % 5  -> DEC Supplemental Graphics, VT300.
#             C = & 4  -> DEC Cyrillic, VT500.
#             C = " ?  -> DEC Greek, VT500.
#             C = " 4  -> DEC Hebrew, VT500.
#             C = % 0  -> DEC Turkish, VT500.
#           The VT520 reference manual lists a few more, but no documenta-
#           tion has been found for the mappings:
#             C = & 5  -> DEC Russian, VT500.
#             C = % 3  -> SCS NRCS, VT500.

__allowed = ['A', 'B', '4', 'C', '5', 'R', 'f', 'Q', '9', 'K', '"', '%=', 'Y', '`', 'E', '6', '%6', 'Z', 'H', '7', '=', '%2', '0', '<', '>', '%5', '&4', '"?', '"4', '%0', '&5', '%3']
_dcs0v2       = ESC + '(' + C[__allowed]  # ESC ( C   | Designate G0 Character Set, ISO 2022, VT100.
_dcs1v2       = ESC + ')' + C[__allowed]  # ESC ) C   | Designate G1 Character Set, ISO 2022, VT100. The same character sets apply as for ESC ( C.
_dcs2v2       = ESC + '*' + C[__allowed]  # ESC * C   | Designate G2 Character Set, ISO 2022, VT220. The same character sets apply as for ESC ( C.
_dcs3v2       = ESC + '+' + C[__allowed]  # ESC + C   | Designate G3 Character Set, ISO 2022, VT220. The same character sets apply as for ESC ( C.

# ESC - C   Designate G1 Character Set, VT300.
#           These controls apply only to 96-character sets.  Unlike the
#           94-character sets, these can have different values than ASCII
#           space and DEL for the mapping of 0x20 and 0x7f.  The valid
#           final characters C for this control are:
#             C = A  -> ISO Latin-1 Supplemental (VT300).
#             C = F  -> ISO Greek Supplemental (VT500).
#             C = H  -> ISO Hebrew Supplemental (VT500).
#             C = L  -> ISO Latin-Cyrillic (VT500).
#             C = M  -> ISO Latin-5 Supplemental (VT500).

__allowed = ['A', 'F', 'H', 'L', 'M']
_dcs1v3       = ESC + '-' + C[__allowed]  # ESC - C   | Designate G1 Character Set, VT300.
_dcs2v3       = ESC + '.' + C[__allowed]  # ESC . C   | Designate G2 Character Set, VT300. The same character sets apply as for ESC - C.
_dcs3v3       = ESC + '/' + C[__allowed]  # ESC / C   | Designate G3 Character Set, VT300. The same character sets apply as for ESC - C.

DECBI         = ESC + '6'   # ESC 6   | Back Index (DECBI), VT420 and up.
DECSC         = ESC + '7'   # ESC 7   | Save Cursor (DECSC), VT100.
DECRC         = ESC + '8'   # ESC 8   | Restore Cursor (DECRC), VT100.
DECFI         = ESC + '9'   # ESC 9   | Forward Index (DECFI), VT420 and up.
DECKPAM       = ESC + '='   # ESC =   | Application Keypad (DECKPAM).
DECKPNM       = ESC + '>'   # ESC >   | Normal Keypad (DECKPNM), VT100.
_CLL          = ESC + 'F'   # ESC F   | Cursor to lower left corner of screen.  This is enabled by the hpLowerleftBugCompat resource.
RIS           = ESC + 'c'   # ESC c   | Full Reset (RIS), VT100.
_ML           = ESC + 'l'   # ESC l   | Memory Lock (per HP terminals).  Locks memory above the cursor.
_MU           = ESC + 'm'   # ESC m   | Memory Unlock (per HP terminals).
LS2           = ESC + 'n'   # ESC n   | Invoke the G2 Character Set as GL (LS2) as GL.
LS3           = ESC + 'o'   # ESC o   | Invoke the G3 Character Set as GL (LS3) as GL.
LS3R          = ESC + '|'   # ESC |   | Invoke the G3 Character Set as GR (LS3R).
LS2R          = ESC + '}'   # ESC }   | Invoke the G2 Character Set as GR (LS2R).
LS1R          = ESC + '~'   # ESC ~   | Invoke the G1 Character Set as GR (LS1R), VT100.


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
