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
from kolr.term.escape_codes.esc import OSC, ST


# ========================================================================= #
# Operating System Commands
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

# OSC Ps ; Pt BEL
# OSC Ps ; Pt ST
#           Set Text Parameters.  For colors and font, if Pt is a "?", the
#           control sequence elicits a response which consists of the con-
#           trol sequence which would set the corresponding value.  The
#           dtterm control sequences allow you to determine the icon name
#           and window title.
#             Ps = 0  -> Change Icon Name and Window Title to Pt.
#             Ps = 1  -> Change Icon Name to Pt.
#             Ps = 2  -> Change Window Title to Pt.
#             Ps = 3  -> Set X property on top-level window.  Pt should be
#           in the form "prop=value", or just "prop" to delete the prop-
#           erty.
#             Ps = 4 ; c ; spec -> Change Color Number c to the color
#           specified by spec.  This can be a name or RGB specification as
#           per XParseColor.  Any number of c/spec pairs may be given.
#           The color numbers correspond to the ANSI colors 0-7, their
#           bright versions 8-15, and if supported, the remainder of the
#           88-color or 256-color table.
#
#           If a "?" is given rather than a name or RGB specification,
#           xterm replies with a control sequence of the same form which
#           can be used to set the corresponding color.  Because more than
#           one pair of color number and specification can be given in one
#           control sequence, xterm can make more than one reply.
#
#             Ps = 5 ; c ; spec -> Change Special Color Number c to the
#           color specified by spec.  This can be a name or RGB specifica-
#           tion as per XParseColor.  Any number of c/spec pairs may be
#           given.  The special colors can also be set by adding the maxi-
#           mum number of colors to these codes in an OSC 4  control:
#
#               Pc = 0  <- resource colorBD (BOLD).
#               Pc = 1  <- resource colorUL (UNDERLINE).
#               Pc = 2  <- resource colorBL (BLINK).
#               Pc = 3  <- resource colorRV (REVERSE).
#               Pc = 4  <- resource colorIT (ITALIC).
#
#             Ps = 6 ; c ; f -> Enable/disable Special Color Number c.
#           OSC 6  is the same as OSC 1 0 6 .
#
#           The 10 colors (below) which may be set or queried using 1 0
#           through 1 9  are denoted dynamic colors, since the correspond-
#           ing control sequences were the first means for setting xterm's
#           colors dynamically, i.e., after it was started.  They are not
#           the same as the ANSI colors (however, the dynamic text fore-
#           ground and background colors are used when ANSI colors are
#           reset using SGR 3 9  and 4 9 , respectively).  These controls
#           may be disabled using the allowColorOps resource.  At least
#           one parameter is expected for Pt.  Each successive parameter
#           changes the next color in the list.  The value of Ps tells the
#           starting point in the list.  The colors are specified by name
#           or RGB specification as per XParseColor.
#
#           If a "?" is given rather than a name or RGB specification,
#           xterm replies with a control sequence of the same form which
#           can be used to set the corresponding dynamic color.  Because
#           more than one pair of color number and specification can be
#           given in one control sequence, xterm can make more than one
#           reply.
#
#             Ps = 1 0  -> Change VT100 text foreground color to Pt.
#             Ps = 1 1  -> Change VT100 text background color to Pt.
#             Ps = 1 2  -> Change text cursor color to Pt.
#             Ps = 1 3  -> Change mouse foreground color to Pt.
#             Ps = 1 4  -> Change mouse background color to Pt.
#             Ps = 1 5  -> Change Tektronix foreground color to Pt.
#             Ps = 1 6  -> Change Tektronix background color to Pt.
#             Ps = 1 7  -> Change highlight background color to Pt.
#             Ps = 1 8  -> Change Tektronix cursor color to Pt.
#             Ps = 1 9  -> Change highlight foreground color to Pt.
#
#             Ps = 4 6  -> Change Log File to Pt.  This is normally dis-
#           abled by a compile-time option.
#
#             Ps = 5 0  -> Set Font to Pt.  These controls may be disabled
#           using the allowFontOps resource.  If Pt begins with a "#",
#           index in the font menu, relative (if the next character is a
#           plus or minus sign) or absolute.  A number is expected but not
#           required after the sign (the default is the current entry for
#           relative, zero for absolute indexing).
#
#           The same rule (plus or minus sign, optional number) is used
#           when querying the font.  The remainder of Pt is ignored.
#
#           A font can be specified after a "#" index expression, by
#           adding a space and then the font specifier.
#
#           If the TrueType Fonts menu entry is set (the renderFont
#           resource), then this control sets/queries the faceName
#           resource.
#
#             Ps = 5 1  -> reserved for Emacs shell.
#
#             Ps = 5 2  -> Manipulate Selection Data.  These controls may
#           be disabled using the allowWindowOps resource.  The parameter
#           Pt is parsed as
#                Pc ; Pd
#           The first, Pc, may contain zero or more characters from the
#           set c , p , q , s , 0 , 1 , 2 , 3 , 4 , 5 , 6 , and 7 .  It is
#           used to construct a list of selection parameters for clip-
#           board, primary, secondary, select, or cut buffers 0 through 7
#           respectively, in the order given.  If the parameter is empty,
#           xterm uses s 0 , to specify the configurable primary/clipboard
#           selection and cut buffer 0.
#
#           The second parameter, Pd, gives the selection data.  Normally
#           this is a string encoded in base64 (RFC-4648).  The data
#           becomes the new selection, which is then available for pasting
#           by other applications.
#
#           If the second parameter is a ? , xterm replies to the host
#           with the selection data encoded using the same protocol.  It
#           uses the first selection found by asking successively for each
#           item from the list of selection parameters.
#
#           If the second parameter is neither a base64 string nor ? ,
#           then the selection is cleared.
#
#             Ps = 1 0 4 ; c -> Reset Color Number c.  It is reset to the
#           color specified by the corresponding X resource.  Any number
#           of c parameters may be given.  These parameters correspond to
#           the ANSI colors 0-7, their bright versions 8-15, and if sup-
#           ported, the remainder of the 88-color or 256-color table.  If
#           no parameters are given, the entire table will be reset.
#
#             Ps = 1 0 5 ; c -> Reset Special Color Number c.  It is reset
#           to the color specified by the corresponding X resource.  Any
#           number of c parameters may be given.  These parameters corre-
#           spond to the special colors which can be set using an OSC 5
#           control (or by adding the maximum number of colors using an
#           OSC 4  control).
#
#             Ps = 1 0 6 ; c ; f -> Enable/disable Special Color Number c.
#           The second parameter tells xterm to enable the corresponding
#           color mode if nonzero, disable it if zero.
#
#               Pc = 0  <- resource colorBDMode (BOLD).
#               Pc = 1  <- resource colorULMode (UNDERLINE).
#               Pc = 2  <- resource colorBLMode (BLINK).
#               Pc = 3  <- resource colorRVMode (REVERSE).
#               Pc = 4  <- resource colorITMode (ITALIC).
#               Pc = 5  <- resource colorAttrMode (Override ANSI).
#
#           The dynamic colors can also be reset to their default
#           (resource) values:
#             Ps = 1 1 0  -> Reset VT100 text foreground color.
#             Ps = 1 1 1  -> Reset VT100 text background color.
#             Ps = 1 1 2  -> Reset text cursor color.
#             Ps = 1 1 3  -> Reset mouse foreground color.
#             Ps = 1 1 4  -> Reset mouse background color.
#             Ps = 1 1 5  -> Reset Tektronix foreground color.
#             Ps = 1 1 6  -> Reset Tektronix background color.
#             Ps = 1 1 7  -> Reset highlight color.
#             Ps = 1 1 8  -> Reset Tektronix cursor color.
#             Ps = 1 1 9  -> Reset highlight foreground color.
#
#             Ps = I  ; c -> Set icon to file.  Sun shelltool, CDE dtterm.
#           The file is expected to be XPM format, and uses the same
#           search logic as the iconHint resource.
#
#             Ps = l  ; c -> Set window title.  Sun shelltool, CDE dtterm.
#
#             Ps = L  ; c -> Set icon label.  Sun shelltool, CDE dtterm.

_osctp = OSC + Ps + ';' + Pt + ST
