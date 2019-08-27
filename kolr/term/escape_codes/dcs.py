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
from kolr.term.escape_codes.esc import DCS, ST


# ========================================================================= #
# Device-Control functions                                                  #
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


# DCS Ps ; Ps | Pt ST
#           User-Defined Keys (DECUDK), VT220 and up.
#
#           The first parameter:
#             Ps = 0  -> Clear all UDK definitions before starting (default).
#             Ps = 1  -> Erase Below (default).
#
#           The second parameter:
#             Ps = 0  <- Lock the keys (default).
#             Ps = 1  <- Do not lock.
#
#           The third parameter is a ';'-separated list of strings denot-
#           ing the key-code separated by a '/' from the hex-encoded key
#           value.  The key codes correspond to the DEC function-key codes
#           (e.g., F6=17).

decudk = DCS + Ps[0, 1] + ';' + Ps[0, 1] + '|' + Pt + ST

# DCS $ q Pt ST
#           Request Status String (DECRQSS), VT420 and up.
#           The string following the "q" is one of the following:
#             m       -> SGR
#             " p     -> DECSCL
#             SP q    -> DECSCUSR
#             " q     -> DECSCA
#             r       -> DECSTBM
#             s       -> DECSLRM
#             t       -> DECSLPP
#             $ |     -> DECSCPP
#             * |     -> DECSNLS
#           xterm responds with DCS 1 $ r Pt ST for valid requests,
#           replacing the Pt with the corresponding CSI string, or DCS 0 $
#           r Pt ST for invalid requests.

decrqss = DCS + '$q' + Pt['m', '"p',' q','"q','r','s','t','$','*'] + ST

# DCS Ps $ t Pt ST
#           Restore presentation status (DECRSPS), VT320 and up.  The con-
#           trol can be converted from a response from DECCIR or DECTABSR
#           by changing the first "u" to a "t"
#             Ps = 1  -> DECCIR
#             Ps = 2  -> DECTABSR

decrsps = DCS + Ps[1, 2] + '$t' + Pt + ST

# DCS + p Pt ST
#           Set Termcap/Terminfo Data (xterm).  The string following the
#           "p" is a name to use for retrieving data from the terminal
#           database.  The data will be used for the "tcap" keyboard con-
#           figuration's function- and special-keys, as well as by the
#           Request Termcap/Terminfo String control.

_std = DCS + '+p' + Pt + ST

# DCS + q Pt ST
#           Request Termcap/Terminfo String (xterm).  The string following
#           the "q" is a list of names encoded in hexadecimal (2 digits
#           per character) separated by ; which correspond to termcap or
#           terminfo key names.
#           A few special features are also recognized, which are not key
#           names:
#           o   Co for termcap colors (or colors for terminfo colors), and
#           o   TN for termcap name (or name for terminfo name).
#           o   RGB for the ncurses direct-color extension.
#               Only a terminfo name is provided, since termcap applica-
#               tions cannot use this information.
#           xterm responds with
#           DCS 1 + r Pt ST for valid requests, adding to Pt an = , and
#           the value of the corresponding string that xterm would send,
#           or
#           DCS 0 + r Pt ST for invalid requests.
#           The strings are encoded in hexadecimal (2 digits per charac-
#           ter).

_rts = DCS + '+q' + Pt + ST


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
