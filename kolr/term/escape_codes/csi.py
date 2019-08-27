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


from kolr.term.escape_codes._params import C, Ps, Pm, Pt, ParamMeta
from kolr.term.escape_codes.esc import CSI


# ========================================================================= #
# CSI SEQUENCES (Control Sequence Introducer)                               #
# ∙ CSI = ESC [ ...                                                         #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences            #
# ========================================================================= #


# cuu = lambda n:     f'{CSI}{n}A'      #  CUU   # Cursor Up                    # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
# cud = lambda n:     f'{CSI}{n}B'      #  CUD   # Cursor Down                  # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
# cuf = lambda n:     f'{CSI}{n}C'      #  CUF   # Cursor Forward               # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
# cub = lambda n:     f'{CSI}{n}D'      #  CUB   # Cursor Back                  # Moves the cursor n (default 1) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect.
# cnl = lambda n:     f'{CSI}{n}E'      #  CNL   # Cursor Next Line             # Moves cursor to beginning of the line n (default 1) lines down.  (not ANSI.SYS)
# cpl = lambda n:     f'{CSI}{n}F'      #  CPL   # Cursor Previous Line         # Moves cursor to beginning of the line n (default 1) lines up.  (not ANSI.SYS)
# cha = lambda n:     f'{CSI}{n}G'      #  CHA   # Cursor Horizontal Absolute   # Moves the cursor to column n (default 1).  (not ANSI.SYS)
# cup = lambda y, x:  f'{CSI}{y};{x}H'  #  CUP   # Cursor Position              # Moves the cursor to row y, column x.  The values are 1-based, and default to 1 (top left corner) if omitted.  A sequence such as CSI ;5H is a synonym for CSI 1;5H as well as CSI 17;H is the same as CSI 17H and CSI 17;1H
# ed  = lambda n:     f'{CSI}{n}J'      #  ED    # Erase in Display             # Clears part of the screen. If n is 0 (or missing), clear from cursor to _finalise of screen. If n is 1, clear from cursor to beginning of the screen. If n is 2, clear entire screen (and moves cursor to upper left on DOS ANSI.SYS).  If n is 3, clear entire screen and delete all lines saved in the scrollback buffer (this feature was added for xterm and is supported by other terminal applications).
# el  = lambda n:     f'{CSI}{n}K'      #  EL    # Erase in Line                # Erases part of the line. If n is 0 (or missing), clear from cursor to the _finalise of the line. If n is 1, clear from cursor to beginning of the line. If n is 2, clear entire line.  Cursor position does not change.
# su  = lambda n:     f'{CSI}{n}S'      #  SU    # Scroll Up                    # Scroll whole page up by n (default 1) lines.  New lines are added at the bottom.  (not ANSI.SYS)
# sd  = lambda n:     f'{CSI}{n}T'      #  SD    # Scroll Down                  # Scroll whole page down by n (default 1) lines.  New lines are added at the top.  (not ANSI.SYS)
# hvp = lambda y, x:  f'{CSI}{y};{x}f'  #  HVP   # Horizontal Vertical Position # Same as CUP
# sgr = lambda *code: f'{CSI}{";".join(str(c) for c in code)}m'  #  SGR   # Select Graphic Rendition     # Sets the appearance of the following characters, see SGR parameters below.
# APE = CSI + '5i'                      #  APE?  # AUX Port On                  # Enable aux serial port usually for local serial printer
# APD = CSI + '4i'                      #  APD?  # AUX Port Off                 # Disable aux serial port usually for local serial printer
# DSR = CSI + '6n'                      #  DSR   # Device Status Report         # Reports the cursor position (CPR) to the application as (as though typed at the keyboard) ESC[n;mR, where n is the row and m is the column.)
# SCP = CSI + 's'                       #  SCP   # Save Cursor Position         # Saves the cursor position/state.
# RCP = CSI + 'u'                       #  RCP   # Restore Cursor Position      # Restores the cursor position/state.
#
# CS  = CSI + '?25h'                    #  CS?   # Show Cursor                  # DECTCEM Shows the cursor, from the VT320.
# CH  = CSI + '?25l'                    #  CH?   # Hide Cursor                  # DECTCEM Hides the cursor.
# SBE = CSI + '?1049h'                  #  SBE?  # Enable Screen Buffer         # Enable alternative screen buffer
# SBD = CSI + '?1049l'                  #  SBD?  # Disable Screen Buffer        # Disable alternative screen buffer
# BPE = CSI + '?2004h'                  #  BPE?  # Enable Bracket Paste         # Turn on bracketed paste mode. Text pasted into the terminal will be surrounded by ESC  From Unix terminal emulators.
# BPD = CSI + '?2004l'                  #  BPD?  # Disable Bracked Paste        # Turn off bracketed paste mode.


# ========================================================================= #
# Functions using CSI , ordered by the final character(s)                   #
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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - -OPTIONS- - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


ich = CSI + Ps + '@'             # CSI Ps @          Insert Ps (Blank) Character(s) (default = 1) (ICH).
sl  = CSI + Ps + ' @'            # CSI Ps SP @       Shift left Ps columns(s) (default = 1) (SL), ECMA-48.
cuu = CSI + Ps + 'A'             # CSI Ps A          Cursor Up Ps Times (default = 1) (CUU).
sr  = CSI + Ps + ' A'            # CSI Ps SP A       Shift right Ps columns(s) (default = 1) (SR), ECMA-48.
cud = CSI + Ps + 'B'             # CSI Ps B          Cursor Down Ps Times (default = 1) (CUD).
cuf = CSI + Ps + 'C'             # CSI Ps C          Cursor Forward Ps Times (default = 1) (CUF).
cub = CSI + Ps + 'D'             # CSI Ps D          Cursor Backward Ps Times (default = 1) (CUB).
cnl = CSI + Ps + 'E'             # CSI Ps E          Cursor Next Line Ps Times (default = 1) (CNL).
cpl = CSI + Ps + 'F'             # CSI Ps F          Cursor Preceding Line Ps Times (default = 1) (CPL).
cha = CSI + Ps + 'G'             # CSI Ps G          Cursor Character Absolute  [column] (default = [row,1]) (CHA).
cup = CSI + Ps + ';' + Ps + 'H'  # CSI Ps ; Ps H     Cursor Position [row;column] (default = [1,1]) (CUP).
cht = CSI + Ps + 'I'             # CSI Ps I          Cursor Forward Tabulation Ps tab stops (default = 1) (CHT).


class ed(metaclass=ParamMeta):
    """[CSI Ps J] Erase in Display (ED), VT100."""
    __seq = CSI + Ps[0, 1, 2, 3] + 'J'
    ERASE_BELOW = __seq(0)  # Ps = 0  -> Erase Below (default).
    ERASE_ABOVE = __seq(1)  # Ps = 1  -> Erase Above.
    ERASE_ALL   = __seq(2)  # Ps = 2  -> Erase All.
    ERASE_SAVED = __seq(3)  # Ps = 3  -> Erase Saved Lines (xterm).

# CSI ? Ps J
class decsed(metaclass=ParamMeta):
    """Erase in Display (DECSED), VT220."""
    __seq = CSI + '?' + Ps[0, 1, 2, 3] + 'J'
    ERASE_BELOW = __seq(0)  # Ps = 0  -> Selective Erase Below (default).
    ERASE_ABOVE = __seq(1)  # Ps = 1  -> Selective Erase Above.
    ERASE_ALL   = __seq(2)  # Ps = 2  -> Selective Erase All.
    ERASE_SAVED = __seq(3)  # Ps = 3  -> Selective Erase Saved Lines (xterm).


# CSI Ps K
class el(metaclass=ParamMeta):
    """Erase in Line (EL), VT100."""
    __seq = CSI + Ps[0, 1, 2] + 'K'
    ERASE_RIGHT = __seq(0)  # Ps = 0  -> Erase to Right (default).
    ERASE_LEFT  = __seq(1)  # Ps = 1  -> Erase to Left.
    ERASE_ALL   = __seq(2)  # Ps = 2  -> Erase All.


# CSI ? Ps K
class decsel(metaclass=ParamMeta):
    """Erase in Line (DECSEL), VT220."""
    __seq = CSI + '?' + Ps[0, 1, 2] + 'K'
    ERASE_RIGHT = __seq(0) # Ps = 0  -> Selective Erase to Right (default).
    ERASE_LEFT  = __seq(1) # Ps = 1  -> Selective Erase to Left.
    ERASE_ALL   = __seq(2) # Ps = 2  -> Selective Erase All.


il       = CSI + Ps + 'L'                            # CSI Ps L                       | Insert Ps Line(s) (default = 1) (IL).
dl       = CSI + Ps + 'M'                            # CSI Ps M                       | Delete Ps Line(s) (default = 1) (DL).
dch      = CSI + Ps + 'P'                            # CSI Ps P                       | Delete Ps Character(s) (default = 1) (DCH).
su       = CSI + Ps + 'S'                            # CSI Ps S                       | Scroll up Ps lines (default = 1) (SU), VT420, ECMA-48.
sd_vt420 = CSI + Ps + 'T'                            # CSI Ps T                       | Scroll down Ps lines (default = 1) (SD), VT420.
_hmt     = CSI + Ps+';'+Ps+';'+Ps+';'+Ps+';'+Ps+'T'  # CSI Ps ; Ps ; Ps ; Ps ; Ps T   | Initiate highlight mouse tracking.  Parameters are [func;startx;starty;firstrow;lastrow].  See the section Mouse Tracking.


# CSI > Ps ; Ps T
class _tmfr(metaclass=ParamMeta):
    """
    Reset one or more features of the title modes to the default value.
    Normally, "reset" disables the feature.  It is possible to disable
    the ability to reset features by compiling a different default
    for the title modes into xterm. (See discussion of Title Modes).
    """
    __seq = CSI + '>' + Ps + ';' + Ps + 'T'
    @staticmethod
    def no_set_labels_hex(x):    return _tmfr.__seq(0, x)  # Ps = 0  -> Do not set window/icon labels using hexadecimal.
    @staticmethod
    def no_query_labels_hex(x):  return _tmfr.__seq(1, x)  # Ps = 1  -> Do not query window/icon labels using hexadecimal.
    @staticmethod
    def no_set_labels_utf8(x):   return _tmfr.__seq(2, x)  # Ps = 2  -> Do not set window/icon labels using UTF-8.
    @staticmethod
    def no_query_labels_utf8(x): return _tmfr.__seq(3, x)  # Ps = 3  -> Do not query window/icon labels using UTF-8.


ech       = CSI + Ps + 'X'       # CSI Ps X        | Erase Ps Character(s) (default = 1) (ECH).
cbt       = CSI + Ps + 'Z'       # CSI Ps Z        | Cursor Backward Tabulation Ps tab stops (default = 1) (CBT)
sd_ecma48 = CSI + Ps + '^'       # CSI Ps ^        | Scroll down Ps lines (default = 1) (SD), ECMA-48. This was a publication error in the original ECMA-48 5th edition (1991) corrected in 2003.
hpa       = CSI + Pm + '`'       # CSI Pm `        | Character Position Absolute  [column] (default = [row,1]) (HPA).
hpr       = CSI + Pm + 'a'       # CSI Pm a        | Character Position Relative  [columns] (default = [row,col+1]) (HPR).
rep       = CSI + Ps + 'b'       # CSI Ps b        | Repeat the preceding graphic character Ps times (REP).
vpa       = CSI + Pm + 'd'       # CSI Pm d        | Line Position Absolute  [row] (default = [1,column]) (VPA).
vpr       = CSI + Pm + 'e'       # CSI Pm e        | Line Position Relative  [rows] (default = [row+1,column]) (VPR).
hvp       = CSI + Ps+';'+Ps+'f'  # CSI Ps ; Ps f   | Horizontal and Vertical Position [row;column] (default = [1,1]) (HVP).


# CSI Ps g
class tbc(metaclass=ParamMeta):
    """Tab Clear (TBC)."""
    __seq = CSI + Ps[0, 3] + 'g'
    CLEAR_CURRENT = __seq(0)  # Ps = 0  -> Clear Current Column (default).
    CLEAR_ALL     = __seq(0)  # Ps = 3  -> Clear All.


# CSI Pm h
class sm(metaclass=ParamMeta):
    """Set Mode (SM)."""
    __seq = CSI + Ps[2, 4, 12, 20] + 'h'
    AM  = __seq(2)   # Ps = 2  -> Keyboard Action Mode (AM).
    IRM = __seq(4)   # Ps = 4  -> Insert Mode (IRM).
    SRM = __seq(12)  # Ps = 1 2  -> Send/receive (SRM).
    LNM = __seq(20)  # Ps = 2 0  -> Automatic Newline (LNM).


# CSI ? Pm h
class decset(metaclass=ParamMeta):
    """DEC Private Mode Set (DECSET)."""
    __allowed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 18, 19, 25, 30, 35, 38, 40, 41, 42, 44, 45, 46, 47, 66, 67, 69, 95, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1010, 1011, 1015, 1034, 1035, 1036, 1037, 1039, 1040, 1041, 1042, 1043, 1044, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1060, 1061, 2004]
    __seq = CSI + '?' + Ps[__allowed] + 'h'
    DECCKM                          = __seq(1)     # Ps = 1  -> Application Cursor Keys (DECCKM), VT100.
    DECANM                          = __seq(2)     # Ps = 2  -> Designate USASCII for character sets G0-G3 (DECANM), VT100, and set VT100 mode.
    DECCOLM                         = __seq(3)     # Ps = 3  -> 132 Column Mode (DECCOLM), VT100.
    DECSCLM                         = __seq(4)     # Ps = 4  -> Smooth (Slow) Scroll (DECSCLM), VT100.
    DECSCNM                         = __seq(5)     # Ps = 5  -> Reverse Video (DECSCNM), VT100.
    DECOM                           = __seq(6)     # Ps = 6  -> Origin Mode (DECOM), VT100.
    DECAWM                          = __seq(7)     # Ps = 7  -> Auto-wrap Mode (DECAWM), VT100.
    DECARM                          = __seq(8)     # Ps = 8  -> Auto-repeat Keys (DECARM), VT100.
    MOUSE_EVENTS_X10                = __seq(9)     # Ps = 9  -> Send Mouse X & Y on button press.  See the section Mouse Tracking.  This is the X10 xterm mouse protocol.
    TOOLBAR                         = __seq(10)    # Ps = 1 0  -> Show toolbar (rxvt).
    BLINK_CURSOR_A                  = __seq(12)    # Ps = 1 2  -> Start Blinking Cursor (AT&T 610).
    BLINK_CURSOR_M                  = __seq(13)    # Ps = 1 3  -> Start Blinking Cursor (set only via resource or menu).
    BLINK_CURSOR_XOR                = __seq(14)    # Ps = 1 4  -> Enable XOR of Blinking Cursor control sequence and menu.
    DECPFF                          = __seq(18)    # Ps = 1 8  -> Print form feed (DECPFF), VT220.
    DECPEX                          = __seq(19)    # Ps = 1 9  -> Set print extent to full screen (DECPEX), VT220.
    DECTCEM                         = __seq(25)    # Ps = 2 5  -> Show Cursor (DECTCEM), VT220.
    SCROLLBAR                       = __seq(30)    # Ps = 3 0  -> Show scrollbar (rxvt).
    FONT_SHIFTING_FUNCTIONS         = __seq(35)    # Ps = 3 5  -> Enable font-shifting functions (rxvt).
    DECTEK                          = __seq(38)    # Ps = 3 8  -> Enter Tektronix Mode (DECTEK), VT240, xterm.
    MODE_80_TO_132                  = __seq(40)    # Ps = 4 0  -> Allow 80 -> 132 Mode, xterm.
    MORE_1_FIX                      = __seq(41)    # Ps = 4 1  -> more(1) fix (see curses resource).
    DECNRCM                         = __seq(42)    # Ps = 4 2  -> Enable National Replacement Character sets (DECNRCM), VT220.
    MARGIN_BELL                     = __seq(44)    # Ps = 4 4  -> Turn On Margin Bell, xterm.
    REVERSE_WRAP_MODE               = __seq(45)    # Ps = 4 5  -> Reverse-wraparound Mode, xterm.
    LOGGING                         = __seq(46)    # Ps = 4 6  -> Start Logging, xterm.  This is normally disabled by a compile-time option.
    ALT_BUFFER                      = __seq(47)    # Ps = 4 7  -> Use Alternate Screen Buffer, xterm.  This may be disabled by the titeInhibit resource.
    DECNKM                          = __seq(66)    # Ps = 6 6  -> Application keypad (DECNKM), VT320.
    DECBKM                          = __seq(67)    # Ps = 6 7  -> Backarrow key sends backspace (DECBKM), VT340, VT420.
    DECLRMM                         = __seq(69)    # Ps = 6 9  -> Enable left and right margin mode (DECLRMM), VT420 and up.
    DECNCSM                         = __seq(95)    # Ps = 9 5  -> Do not clear screen when DECCOLM is set/reset (DECNCSM), VT510 and up.
    MOUSE_EVENTS_X11                = __seq(1000)  # Ps = 1 0 0 0  -> Send Mouse X & Y on button press and release.  See the section Mouse Tracking.  This is the X11 xterm mouse protocol.
    MOUSE_TRACKING_HILITE           = __seq(1001)  # Ps = 1 0 0 1  -> Use Hilite Mouse Tracking, xterm.
    MOUSE_TRACKING_CELL             = __seq(1002)  # Ps = 1 0 0 2  -> Use Cell Motion (button event) Mouse Tracking, xterm.
    MOUSE_TRACKING_ALL              = __seq(1003)  # Ps = 1 0 0 3  -> Use All Motion (any event) Mouse Tracking, xterm.
    FOCUS_EVENTS                    = __seq(1004)  # Ps = 1 0 0 4  -> Send FocusIn/FocusOut events, xterm.
    MOUSE_MODE_UTF8                 = __seq(1005)  # Ps = 1 0 0 5  -> Enable UTF-8 Mouse Mode, xterm.
    MOUSE_MODE_SGR                  = __seq(1006)  # Ps = 1 0 0 6  -> Enable SGR Mouse Mode, xterm.
    ALT_SCROLL_MODE                 = __seq(1007)  # Ps = 1 0 0 7  -> Enable Alternate Scroll Mode, xterm.  This corresponds to the alternateScroll resource.
    SCROLL_BOTTOM_ON_TTY            = __seq(1010)  # Ps = 1 0 1 0  -> Scroll to bottom on tty output (rxvt).
    SCROLL_BOTTOM_ON_KEY            = __seq(1011)  # Ps = 1 0 1 1  -> Scroll to bottom on key press (rxvt).
    MOUSE_MODE_URXVT                = __seq(1015)  # Ps = 1 0 1 5  -> Enable urxvt Mouse Mode.
    RESOURCE_8_BIT_INPUT            = __seq(1034)  # Ps = 1 0 3 4  -> Interpret "meta" key, xterm.  This sets eighth bit of keyboard input (and enables the eightBitInput resource).
    RESOURCE_NUM_LOCK               = __seq(1035)  # Ps = 1 0 3 5  -> Enable special modifiers for Alt and Num-Lock keys, xterm.  This enables the numLock resource.
    RESOURCE_META_SENDS_ESCAPE      = __seq(1036)  # Ps = 1 0 3 6  -> Send ESC   when Meta modifies a key, xterm. This enables the metaSendsEscape resource.
    SEND_DEL                        = __seq(1037)  # Ps = 1 0 3 7  -> Send DEL from the editing-keypad Delete key, xterm.
    RESOURCE_ALT_SENDS_ESC          = __seq(1039)  # Ps = 1 0 3 9  -> Send ESC  when Alt modifies a key, xterm. This enables the altSendsEscape resource, xterm.
    RESOURCE_KEEP_SELECTION         = __seq(1040)  # Ps = 1 0 4 0  -> Keep selection even if not highlighted, xterm.  This enables the keepSelection resource.
    RESOURCE_SELECT_TO_CLIPBOARD    = __seq(1041)  # Ps = 1 0 4 1  -> Use the CLIPBOARD selection, xterm.  This enables the selectToClipboard resource.
    RESOURCE_BELL_IS_URGENT         = __seq(1042)  # Ps = 1 0 4 2  -> Enable Urgency window manager hint when Control-G is received, xterm.  This enables the bellIsUrgent resource.
    RESOURCE_POP_ON_BELL            = __seq(1043)  # Ps = 1 0 4 3  -> Enable raising of the window when Control-G is received, xterm.  This enables the popOnBell resource.
    RESOURCE_KEEP_CLIPBOARD         = __seq(1044)  # Ps = 1 0 4 4  -> Reuse the most recent data copied to CLIPBOARD, xterm.  This enables the keepClipboard resource.
    RESOURCE_ALT_BUFFER_SWITCHING   = __seq(1046)  # Ps = 1 0 4 6  -> Enable switching to/from Alternate Screen Buffer, xterm.  This works for terminfo-based systems, updating the titeInhibit resource.
    RESOURCE_ALT_BUFFER             = __seq(1047)  # Ps = 1 0 4 7  -> Use Alternate Screen Buffer, xterm.  This may be disabled by the titeInhibit resource.
    RESOURCE_SAVE_CURSOR            = __seq(1048)  # Ps = 1 0 4 8  -> Save cursor as in DECSC, xterm.  This may be disabled by the titeInhibit resource.
    RESOURCE_SAVE_CURSOR_ALT_BUFFER = __seq(1049)  # Ps = 1 0 4 9  -> Save cursor as in DECSC, xterm.  After saving the cursor, switch to the Alternate Screen Buffer, clearing it first.  This may be disabled by the titeInhibit resource.  This control combines the effects of the 1 0 4 7 and 1 0 4 8  modes.  Use this with terminfo-based applications rather than the 4 7  mode.
    FUNCTION_KEY_MODE_TERM          = __seq(1050)  # Ps = 1 0 5 0  -> Set terminfo/termcap function-key mode, xterm.
    FUNCTION_KEY_MODE_SUN           = __seq(1051)  # Ps = 1 0 5 1  -> Set Sun function-key mode, xterm.
    FUNCTION_KEY_MODE_HP            = __seq(1052)  # Ps = 1 0 5 2  -> Set HP function-key mode, xterm.
    FUNCTION_KEY_MODE_SCO           = __seq(1053)  # Ps = 1 0 5 3  -> Set SCO function-key mode, xterm.
    EMULATION_LEGACY                = __seq(1060)  # Ps = 1 0 6 0  -> Set legacy keyboard emulation (i.e, X11R6), xterm.
    EMULATION_VT220_KEYS            = __seq(1061)  # Ps = 1 0 6 1  -> Set VT220 keyboard emulation, xterm.
    BRACKET_PASTE                   = __seq(2004)  # Ps = 2 0 0 4  -> Set bracketed paste mode, xterm.


# CSI Pm i
class mc(metaclass=ParamMeta):
    """Media Copy (MC)."""
    __seq = CSI + Ps[0, 4, 5, 10, 11] + 'i'
    PRINT_SCREEN         = __seq(0)   # Ps = 0  -> Print screen (default).
    PRINT_CONTROLLER_OFF = __seq(4)   # Ps = 4  -> Turn off printer controller mode.
    PRINT_CONTROLLER_ON  = __seq(5)   # Ps = 5  -> Turn on printer controller mode.
    SCREEN_DUMP_HTML     = __seq(10)  # Ps = 1 0  -> HTML screen dump, xterm.
    SCREEN_DUMP_SVG      = __seq(11)  # Ps = 1 1  -> SVG screen dump, xterm.


# CSI ? Pm i
class mcs(metaclass=ParamMeta):
    """Media Copy (MC), DEC-specific."""
    __seq = CSI + '?' + Ps[1, 4, 5, 10, 11] + 'i'
    PRINT_CURSOR_LINE = __seq(1)   # Ps = 1  -> Print line containing cursor.
    AUTO_PRINT_OFF    = __seq(4)   # Ps = 4  -> Turn off autoprint mode.
    AUTO_PRINT_ON     = __seq(5)   # Ps = 5  -> Turn on autoprint mode.
    PRINT_DISPLAY     = __seq(10)  # Ps = 1 0  -> Print composed display, ignores DECPEX.
    PRINT_ALL_PAGES   = __seq(11)  # Ps = 1 1  -> Print all pages.


# CSI Pm l
class rm(metaclass=ParamMeta):
    """Reset Mode (RM)."""
    __seq = CSI + Ps[2, 4, 12, 20] + 'l'
    AM = __seq(2)  # Ps = 2  -> Keyboard Action Mode (AM).
    IRM = __seq(4)  # Ps = 4  -> Replace Mode (IRM).
    SRM = __seq(12) # Ps = 1 2  -> Send/receive (SRM).
    LNM = __seq(20) # Ps = 2 0  -> Normal Linefeed (LNM).


# CSI ? Pm l
class decrst(metaclass=ParamMeta):
    """DEC Private Mode Reset (DECRST)."""
    __allowed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 18, 19, 25, 30, 35, 40, 41, 42, 44, 45, 46, 47, 66, 67, 69, 95, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1010, 1011, 1015, 1034, 1035, 1036, 1037, 1039, 1040, 1041, 1042, 1043, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1060, 1061, 2004]
    __seq = CSI + '?' + Ps[__allowed] + 'l'
    DECCKM                          = __seq(1)     # Ps = 1  -> Normal Cursor Keys (DECCKM), VT100.
    DECANM                          = __seq(2)     # Ps = 2  -> Designate VT52 mode (DECANM), VT100.
    DECCOLM                         = __seq(3)     # Ps = 3  -> 80 Column Mode (DECCOLM), VT100.
    DECSCLM                         = __seq(4)     # Ps = 4  -> Jump (Fast) Scroll (DECSCLM), VT100.
    DECSCNM                         = __seq(5)     # Ps = 5  -> Normal Video (DECSCNM), VT100.
    DECOM                           = __seq(6)     # Ps = 6  -> Normal Cursor Mode (DECOM), VT100.
    DECAWM                          = __seq(7)     # Ps = 7  -> No Auto-wrap Mode (DECAWM), VT100.
    DECARM                          = __seq(8)     # Ps = 8  -> No Auto-repeat Keys (DECARM), VT100.
    MOUSE_EVENTS_X10                = __seq(9)     # Ps = 9  -> Don't send Mouse X & Y on button press, xterm.
    TOOLBAR                         = __seq(10)    # Ps = 1 0  -> Hide toolbar (rxvt).
    BLINK_CURSOR_A                  = __seq(12)    # Ps = 1 2  -> Stop Blinking Cursor (AT&T 610).
    BLINK_CURSOR_M                  = __seq(13)    # Ps = 1 3  -> Disable Blinking Cursor (reset only via resource or menu).
    BLINK_CURSOR_XOR                = __seq(14)    # Ps = 1 4  -> Disable XOR of Blinking Cursor control sequence and menu.
    DECPFF                          = __seq(18)    # Ps = 1 8  -> Don't print form feed (DECPFF).
    DECPEX                          = __seq(19)    # Ps = 1 9  -> Limit print to scrolling region (DECPEX).
    DECTCEM                         = __seq(25)    # Ps = 2 5  -> Hide Cursor (DECTCEM), VT220.
    SCROLLBAR                       = __seq(30)    # Ps = 3 0  -> Don't show scrollbar (rxvt).
    FONT_SHIFTING_FUNCTIONS         = __seq(35)    # Ps = 3 5  -> Disable font-shifting functions (rxvt).
    # <MISSING> DECTEK                             # Ps = 3 8
    MODE_80_TO_132                  = __seq(40)    # Ps = 4 0  -> Disallow 80 -> 132 Mode, xterm.
    MORE_1_FIX                      = __seq(41)    # Ps = 4 1  -> No more(1) fix (see curses resource).
    DECNRCM                         = __seq(42)    # Ps = 4 2  -> Disable National Replacement Character sets (DECNRCM), VT220.
    MARGIN_BELL                     = __seq(44)    # Ps = 4 4  -> Turn Off Margin Bell, xterm.
    REVERSE_WRAP_MODE               = __seq(45)    # Ps = 4 5  -> No Reverse-wraparound Mode, xterm.
    LOGGING                         = __seq(46)    # Ps = 4 6  -> Stop Logging, xterm.  This is normally disabled by a compile-time option.
    ALT_BUFFER                      = __seq(47)    # Ps = 4 7  -> Use Normal Screen Buffer, xterm.
    DECNKM                          = __seq(66)    # Ps = 6 6  -> Numeric keypad (DECNKM), VT320.
    DECBKM                          = __seq(67)    # Ps = 6 7  -> Backarrow key sends delete (DECBKM), VT340, VT420.
    DECLRMM                         = __seq(69)    # Ps = 6 9  -> Disable left and right margin mode (DECLRMM), VT420 and up.
    DECNCSM                         = __seq(95)    # Ps = 9 5  -> Clear screen when DECCOLM is set/reset (DECNCSM), VT510 and up.
    MOUSE_EVENTS_X11                = __seq(1000)  # Ps = 1 0 0 0  -> Don't send Mouse X & Y on button press and release.  See the section Mouse Tracking.
    MOUSE_TRACKING_HILITE           = __seq(1001)  # Ps = 1 0 0 1  -> Don't use Hilite Mouse Tracking, xterm.
    MOUSE_TRACKING_CELL             = __seq(1002)  # Ps = 1 0 0 2  -> Don't use Cell Motion (button event) Mouse Tracking, xterm.
    MOUSE_TRACKING_ALL              = __seq(1003)  # Ps = 1 0 0 3  -> Don't use All Motion (any event) Mouse Tracking, xterm.
    FOCUS_EVENTS                    = __seq(1004)  # Ps = 1 0 0 4  -> Don't send FocusIn/FocusOut events, xterm.
    MOUSE_MODE_UTF8                 = __seq(1005)  # Ps = 1 0 0 5  -> Disable UTF-8 Mouse Mode, xterm.
    MOUSE_MODE_SGR                  = __seq(1006)  # Ps = 1 0 0 6  -> Disable SGR Mouse Mode, xterm.
    ALT_SCROLL_MODE                 = __seq(1007)  # Ps = 1 0 0 7  -> Disable Alternate Scroll Mode, xterm.  This corresponds to the alternateScroll resource.
    SCROLL_BOTTOM_ON_TTY            = __seq(1010)  # Ps = 1 0 1 0  -> Don't scroll to bottom on tty output (rxvt).
    SCROLL_BOTTOM_ON_KEY            = __seq(1011)  # Ps = 1 0 1 1  -> Don't scroll to bottom on key press (rxvt).
    MOUSE_MODE_URXVT                = __seq(1015)  # Ps = 1 0 1 5  -> Disable urxvt Mouse Mode.
    RESOURCE_8_BIT_INPUT            = __seq(1034)  # Ps = 1 0 3 4  -> Don't interpret "meta" key, xterm.  This disables the eightBitInput resource.
    RESOURCE_NUM_LOCK               = __seq(1035)  # Ps = 1 0 3 5  -> Disable special modifiers for Alt and Num-Lock keys, xterm.  This disables the numLock resource.
    RESOURCE_META_SENDS_ESCAPE      = __seq(1036)  # Ps = 1 0 3 6  -> Don't send ESC  when Meta modifies a key, xterm.  This disables the metaSendsEscape resource.
    SEND_DEL                        = __seq(1037)  # Ps = 1 0 3 7  -> Send VT220 Remove from the editing-keypad Delete key, xterm.
    RESOURCE_ALT_SENDS_ESC          = __seq(1039)  # Ps = 1 0 3 9  -> Don't send ESC when Alt modifies a key, xterm.  This disables the altSendsEscape resource.
    RESOURCE_KEEP_SELECTION         = __seq(1040)  # Ps = 1 0 4 0  -> Do not keep selection when not highlighted, xterm.  This disables the keepSelection resource.
    RESOURCE_SELECT_TO_CLIPBOARD    = __seq(1041)  # Ps = 1 0 4 1  -> Use the PRIMARY selection, xterm.  This disables the selectToClipboard resource.
    RESOURCE_BELL_IS_URGENT         = __seq(1042)  # Ps = 1 0 4 2  -> Disable Urgency window manager hint when Control-G is received, xterm.  This disables the bellIsUrgent resource.
    RESOURCE_POP_ON_BELL            = __seq(1043)  # Ps = 1 0 4 3  -> Disable raising of the window when Control-G is received, xterm.  This disables the popOnBell resource.
    # <MISSING> RESOURCE_KEEP_CLIPBOARD            # Ps = 1 0 4 4
    RESOURCE_ALT_BUFFER_SWITCHING   = __seq(1046)  # Ps = 1 0 4 6  -> Disable switching to/from Alternate Screen Buffer, xterm.  This works for terminfo-based systems, updating the titeInhibit resource.  If currently using the Alternate Screen Buffer, xterm switches to the Normal Screen Buffer.
    RESOURCE_ALT_BUFFER             = __seq(1047)  # Ps = 1 0 4 7  -> Use Normal Screen Buffer, xterm.  Clear the screen first if in the Alternate Screen Buffer.  This may be disabled by the titeInhibit resource.
    RESOURCE_SAVE_CURSOR            = __seq(1048)  # Ps = 1 0 4 8  -> Restore cursor as in DECRC, xterm.  This may be disabled by the titeInhibit resource.
    RESOURCE_SAVE_CURSOR_ALT_BUFFER = __seq(1049)  # Ps = 1 0 4 9  -> Use Normal Screen Buffer and restore cursor as in DECRC, xterm.  This may be disabled by the titeInhibit resource.  This combines the effects of the 1 0 4 7  and 1 0 4 8  modes.  Use this with terminfo-based applications rather than the 4 7  mode.
    FUNCTION_KEY_MODE_TERM          = __seq(1050)  # Ps = 1 0 5 0  -> Reset terminfo/termcap function-key mode, xterm.
    FUNCTION_KEY_MODE_SUN           = __seq(1051)  # Ps = 1 0 5 1  -> Reset Sun function-key mode, xterm.
    FUNCTION_KEY_MODE_HP            = __seq(1052)  # Ps = 1 0 5 2  -> Reset HP function-key mode, xterm.
    FUNCTION_KEY_MODE_SCO           = __seq(1053)  # Ps = 1 0 5 3  -> Reset SCO function-key mode, xterm.
    EMULATION_LEGACY                = __seq(1060)  # Ps = 1 0 6 0  -> Reset legacy keyboard emulation (i.e, X11R6), xterm.
    EMULATION_VT220_KEYS            = __seq(1061)  # Ps = 1 0 6 1  -> Reset keyboard emulation to Sun/PC style, xterm.
    BRACKET_PASTE                   = __seq(2004)  # Ps = 2 0 0 4  -> Reset bracketed paste mode, xterm.


# CSI Pm m
class sgr(metaclass=ParamMeta):
    """Character Attributes (SGR)."""
    # TODO: 38, 48
    __allowed = [0, 1, 2, 3, 4, 5, 7, 8, 9, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107]
    __seq = CSI + Ps[__allowed] + 'm'

    RESET                       = __seq(0)   # Ps = 0  -> Normal (default), VT100.
    BOLD                        = __seq(1)   # Ps = 1  -> Bold, VT100.
    FAINT                       = __seq(2)   # Ps = 2  -> Faint, decreased intensity, ECMA-48 2nd.
    ITALIC                      = __seq(3)   # Ps = 3  -> Italicized, ECMA-48 2nd.
    UNDERLINE                   = __seq(4)   # Ps = 4  -> Underlined, VT100.
    # BLINK_RAPID                 = __seq(6)   # Ps = 5  -> Blink, VT100. This appears as Bold in X11R6 xterm.
    INVERT                      = __seq(7)   # Ps = 7  -> Inverse, VT100.
    CONCEAL                     = __seq(8)   # Ps = 8  -> Invisible, i.e., hidden, ECMA-48 2nd, VT300.
    STRIKETHROUGH               = __seq(9)   # Ps = 9  -> Crossed-out characters, ECMA-48 3rd.
    # FONT_PRIMARY              = __seq(10)
    # ↓↓↓↓↓ 11-19 Alternate Font ↓↓↓↓↓
    # FONT_ALT_1                = __seq(11)
    # FONT_ALT_2                = __seq(12)
    # FONT_ALT_3                = __seq(13)
    # FONT_ALT_4                = __seq(14)
    # FONT_ALT_5                = __seq(15)
    # FONT_ALT_6                = __seq(16)
    # FONT_ALT_7                = __seq(17)
    # FONT_ALT_8                = __seq(18)
    # FONT_ALT_9                = __seq(19)
    # ↑↑↑↑↑ 11-19 Alternate Font ↑↑↑↑↑
    # FRANKTUR                  = __seq(20)
    RESET_BOLD                  = __seq(21)  # Ps = 2 1  -> Doubly-underlined, ECMA-48 3rd.
    RESET_INTENSITY             = __seq(22)  # Ps = 2 2  -> Normal (neither bold nor faint), ECMA-48 3rd.
    RESET_ITALIC                = __seq(23)  # Ps = 2 3  -> Not italicized, ECMA-48 3rd.
    RESET_UNDERLINE             = __seq(24)  # Ps = 2 4  -> Not underlined, ECMA-48 3rd.
    RESET_BLINK                 = __seq(25)  # Ps = 2 5  -> Steady (not blinking), ECMA-48 3rd.
    # 26 <RESET BLINK FAST?>
    RESET_INVERSE               = __seq(27)  # Ps = 2 7  -> Positive (not inverse), ECMA-48 3rd.
    RESET_CONCEAL               = __seq(28)  # Ps = 2 8  -> Visible, i.e., not hidden, ECMA-48 3rd, VT300.
    RESET_STRIKETHROUGH         = __seq(29)  # Ps = 2 9  -> Not crossed-out, ECMA-48 3rd.
    # ↓↓↓↓↓ 30-37 Set Foreground Color ↓↓↓↓
    FG_BLACK                    = __seq(30)  # Ps = 3 0  -> Set foreground color to Black.
    FG_RED                      = __seq(31)  # Ps = 3 1  -> Set foreground color to Red.
    FG_GREEN                    = __seq(32)  # Ps = 3 2  -> Set foreground color to Green.
    FG_YELLOW                   = __seq(33)  # Ps = 3 3  -> Set foreground color to Yellow.
    FG_BLUE                     = __seq(34)  # Ps = 3 4  -> Set foreground color to Blue.
    FG_MAGENTA                  = __seq(35)  # Ps = 3 5  -> Set foreground color to Magenta.
    FG_CYAN                     = __seq(36)  # Ps = 3 6  -> Set foreground color to Cyan.
    FG_WHITE                    = __seq(37)  # Ps = 3 7  -> Set foreground color to White.
    # ↑↑↑↑↑ 30-37 Set Foreground Color ↑↑↑↑
    RESET_FG                    = __seq(39)  # Ps = 3 9  -> Set foreground color to default, ECMA-48 3rd.
    # ↓↓↓↓↓ 40-47 Set Background Color ↓↓↓↓
    BG_BLACK                    = __seq(40)  # Ps = 4 0  -> Set background color to Black.
    BG_RED                      = __seq(41)  # Ps = 4 1  -> Set background color to Red.
    BG_GREEN                    = __seq(42)  # Ps = 4 2  -> Set background color to Green.
    BG_YELLOW                   = __seq(43)  # Ps = 4 3  -> Set background color to Yellow.
    BG_BLUE                     = __seq(44)  # Ps = 4 4  -> Set background color to Blue.
    BG_MAGENTA                  = __seq(45)  # Ps = 4 5  -> Set background color to Magenta.
    BG_CYAN                     = __seq(46)  # Ps = 4 6  -> Set background color to Cyan.
    BG_WHITE                    = __seq(47)  # Ps = 4 7  -> Set background color to White.
    # ↑↑↑↑↑ 40-47 Set Background Color ↑↑↑↑
    RESET_BG                    = __seq(49)  # Ps = 4 9  -> Set background color to default, ECMA-48 3rd.
    # 50 <UNUSED>
    # FRAME                     = __seq(51)
    # ENCIRCLE                  = __seq(52)
    # OVERLINE                  = __seq(53)
    # RESET_FRAME               = __seq(54)
    # RESET_OVERLINE            = __seq(55)
    # 56-59 <UNUSED>
    # IDEOGRAM_UNDERLINE        = __seq(60)
    # IDEOGRAM_DOUBLE_UNDERLINE = __seq(61)
    # IDEOGRAM_OVERLINE         = __seq(62)
    # IDEOGRAM_DOUBLE_OVERLINE  = __seq(63)
    # IDEOGRAM_STRESS           = __seq(64)
    # RESET_IDEOGRAM            = __seq(65)
    # 66-89 <UNUSED>

    # Some of the above note the edition of ECMA-48 which first
    # describes a feature.  In its successive editions from 1979 to
    # 1991 (2nd 1979, 3rd 1984, 4th 1986, and 5th 1991), ECMA-48
    # listed codes through 6 5 (skipping several toward the end of
    # the range).  Most of the ECMA-48 codes not implemented in
    # xterm were never implemented in a hardware terminal.  Several
    # (such as 3 9  and 4 9 ) are either noted in ECMA-48 as imple-
    # mentation defined, or described in vague terms.

    # The successive editions of ECMA-48 give little attention to
    # changes from one edition to the next, except to comment on
    # features which have become obsolete.  ECMA-48 1st (1976) is
    # unavailable; there is no reliable source of information which
    # states whether "ANSI" color was defined in that edition, or
    # later (1979).  The VT100 (1978) implemented the most commonly
    # used non-color video attributes which are given in the 2nd
    # edition.

    # While 8-color support is described in ECMA-48 2nd edition, the
    # VT500 series (introduced in 1993) were the first DEC terminals
    # implementing "ANSI" color.  The DEC terminal's use of color is
    # known to differ from xterm; useful documentation on this
    # series became available too late to influence xterm.

    # If 16-color support is compiled, the following aixterm con-
    # trols apply.  Assume that xterm's resources are set so that
    # the ISO color codes are the first 8 of a set of 16.  Then the
    # aixterm colors are the bright versions of the ISO colors:

    # ↓↓↓↓↓ 90-97 Set Bright Foreground Col
    FG_BRIGHT_BLACK           = __seq(90)   # Ps = 9 0  -> Set foreground color to Black.
    FG_BRIGHT_RED             = __seq(91)   # Ps = 9 1  -> Set foreground color to Red.
    FG_BRIGHT_GREEN           = __seq(92)   # Ps = 9 2  -> Set foreground color to Green.
    FG_BRIGHT_YELLOW          = __seq(93)   # Ps = 9 3  -> Set foreground color to Yellow.
    FG_BRIGHT_BLUE            = __seq(94)   # Ps = 9 4  -> Set foreground color to Blue.
    FG_BRIGHT_MAGENTA         = __seq(95)   # Ps = 9 5  -> Set foreground color to Magenta.
    FG_BRIGHT_CYAN            = __seq(96)   # Ps = 9 6  -> Set foreground color to Cyan.
    FG_BRIGHT_WHITE           = __seq(97)   # Ps = 9 7  -> Set foreground color to White.
    # ↑↑↑↑↑ 90-97 Set Bright Foreground Col
    # 98-99 <UNUSED>
    # ↓↓↓↓↓ 100-107 Set Bright Background C
    BG_BRIGHT_BLACK           = __seq(100)  # Ps = 1 0 0  -> Set background color to Black.
    BG_BRIGHT_RED             = __seq(101)  # Ps = 1 0 1  -> Set background color to Red.
    BG_BRIGHT_GREEN           = __seq(102)  # Ps = 1 0 2  -> Set background color to Green.
    BG_BRIGHT_YELLOW          = __seq(103)  # Ps = 1 0 3  -> Set background color to Yellow.
    BG_BRIGHT_BLUE            = __seq(104)  # Ps = 1 0 4  -> Set background color to Blue.
    BG_BRIGHT_MAGENTA         = __seq(105)  # Ps = 1 0 5  -> Set background color to Magenta.
    BG_BRIGHT_CYAN            = __seq(106)  # Ps = 1 0 6  -> Set background color to Cyan.
    BG_BRIGHT_WHITE           = __seq(107)  # Ps = 1 0 7  -> Set background color to White.
    # ↑↑↑↑↑ 100-107 Set Bright Background C

    # If xterm is compiled with the 16-color support disabled, it supports the following, from rxvt:
    #   Ps = 1 0 0  -> Set foreground and background color to default.

    # XTerm maintains a color palette whose entries are identified by an index beginning with zero.  If 88- or 256-color support is compiled, the following apply:
    # o   All parameters are decimal integers.
    # o   RGB values range from zero (0) to 255.
    # o   ISO-8613-6 has been interpreted in more than one way;
    #     xterm allows the semicolons separating the subparameters
    #     in this control to be replaced by colons (but after the
    #     first colon, colons must be used).

    # These ISO-8613-6 controls (marked in ECMA-48 5th edition as "reserved for future standardization") are supported by xterm:
    #   Pm = 3 8 ; 2 ; Pi ; Pr ; Pg ; Pb -> Set foreground color to the closest match in xterm's palette for the given RGB Pr/Pg/Pb.  The color space identifier Pi is ignored.
    #   Pm = 3 8 ; 5 ; Ps -> Set foreground color to Ps.
    #   Pm = 4 8 ; 2 ; Pi ; Pr ; Pg ; Pb -> Set background color to the closest match in xterm's palette for the given RGB Pr/Pg/Pb.  The color space identifier Pi is ignored.
    #   Pm = 4 8 ; 5 ; Ps -> Set background color to Ps.

    # This variation on ISO-8613-6 is supported for compatibility with KDE konsole:
    #   Pm = 3 8 ; 2 ; Pr ; Pg ; Pb -> Set foreground color to the closest match in xterm's palette for the given RGB Pr/Pg/Pb.
    #   Pm = 4 8 ; 2 ; Pr ; Pg ; Pb -> Set background color to the closest match in xterm's palette for the given RGB Pr/Pg/Pb.

    __seq_rgb = CSI + Ps[38, 48] + ';2;' + Ps + ';' + Ps + ';' + Ps + 'm'
    __seq_256 = CSI + Ps[38, 48] + ';5;' + Ps + 'm'

    @staticmethod
    def fg_select_rgb(r, g, b):
        assert all(0 <= v < 256 for v in [r, g, b])
        return sgr.__seq_rgb(38, r, g, b)
    @staticmethod
    def fg_select_256(n):
        assert 0 <= n < 256
        return sgr.__seq_256(38, n)
    @staticmethod
    def bg_select_rgb(r, g, b):
        assert all(0 <= v < 256 for v in [r, g, b])
        return sgr.__seq_rgb(48, r, g, b)
    @staticmethod
    def bg_select_256(n):
        assert 0 <= n < 256
        return sgr.__seq_256(48, n)

    # If xterm is compiled with direct-color support, and the
    # resource directColor is true, then rather than choosing the
    # closest match, xterm asks the X server to directly render a given color.

# CSI > Ps ; Ps m
class _rd(metaclass=ParamMeta):
    """
    Set or reset resource-values used by xterm to decide whether
    to construct escape sequences holding information about the
    modifiers pressed with a given key.
    """
    __seq = CSI + '>' + Ps[0, 1, 2, 4] + ';' + Ps + 'm'
    # The first parameter identifies the resource to set/reset.  The
    # second parameter is the value to assign to the resource.
    # If the second parameter is omitted, the resource is reset to
    # its initial value.
    @staticmethod
    def keyboard(val):      return _rd.__seq(0, val)  # Ps = 0  -> modifyKeyboard.
    @staticmethod
    def cursor_keys(val):   return _rd.__seq(1, val)  # Ps = 1  -> modifyCursorKeys.
    @staticmethod
    def function_keys(val): return _rd.__seq(2, val)  # Ps = 2  -> modifyFunctionKeys.
    @staticmethod
    def other_keys(val):    return _rd.__seq(4, val)  # Ps = 4  -> modifyOtherKeys.
    # If no parameters are given, all resources are reset to their
    # initial values.


# CSI > Ps n
class _rd(metaclass=ParamMeta):
    """
    Disable modifiers which may be enabled via the CSI > Ps; Ps m
    sequence.  This corresponds to a resource value of "-1", which
    cannot be set with the other sequence.
    """
    __seq = CSI + '>' + Ps[0, 1, 2, 4] + 'n'
    # The parameter identifies the resource to be disabled:
    KEYBOARD      = __seq(0)  # Ps = 0  -> modifyKeyboard.
    CURSOR_KEYS   = __seq(1)  # Ps = 1  -> modifyCursorKeys.
    FUNCTION_KEYS = __seq(2)  # Ps = 2  -> modifyFunctionKeys.
    OTHER_KEYS    = __seq(4)  # Ps = 4  -> modifyOtherKeys.
    # If the parameter is omitted, modifyFunctionKeys is disabled.
    # When modifyFunctionKeys is disabled, xterm uses the modifier
    # keys to make an extended sequence of functions rather than
    # adding a parameter to each function key to denote the modifiers.


# CSI > Ps p
class _pms(metaclass=ParamMeta):
    """
    Set resource value pointerMode.  This is used by xterm to
    decide whether to hide the pointer cursor as the user types.
    """
    __seq = CSI + '>' + Ps[0, 1, 2, 3] + 'p'
    # Valid values for the parameter:
    NEVER_HIDE                 = __seq(0)  # Ps = 0  -> never hide the pointer.
    HIDE_IF_NOT_TRACKING       = __seq(1)  # Ps = 1  -> hide if the mouse tracking mode is not enabled.
    ALWAYS_HIDE_EXCEPT_LEAVING = __seq(2)  # Ps = 2  -> always hide the pointer, except when leaving the window.
    ALWAYS_HIDE                = __seq(3)  # Ps = 3  -> always hide the pointer, even if leaving/entering the window.
    # If no parameter is given, xterm uses the default, which is 1 .


decstr = CSI + '!p'     # CSI ! p   | Soft terminal reset (DECSTR), VT220 and up.


# CSI Ps ; Ps " p
class decscl(metaclass=ParamMeta):
    """Set conformance level (DECSCL), VT220 and up."""
    __seq = CSI + Ps[61, 62, 63, 64, 65] + ';' + Ps[0, 1, 2] + '"p'
    # The first parameter selects the conformance level.
    # Valid values are:
    @staticmethod
    def level_1(t): return decscl.__seq(61, t)  # Ps = 6 1  -> level 1, e.g., VT100.
    @staticmethod
    def level_2(t): return decscl.__seq(62, t)  # Ps = 6 2  -> level 2, e.g., VT200.
    @staticmethod
    def level_3(t): return decscl.__seq(63, t)  # Ps = 6 3  -> level 3, e.g., VT300.
    @staticmethod
    def level_4(t): return decscl.__seq(64, t)  # Ps = 6 4  -> level 4, e.g., VT400.
    @staticmethod
    def level_5(t): return decscl.__seq(65, t)  # Ps = 6 5  -> level 5, e.g., VT500.
    # The second parameter selects the C1 control transmission mode.
    # This is an optional parameter, ignored in conformance level 1.
    # Valid values are:
    #   Ps = 0  -> 8-bit controls.
    #   Ps = 1  -> 7-bit controls (DEC factory default).
    #   Ps = 2  -> 8-bit controls.
    # The 7-bit and 8-bit control modes can also be set by S7C1T and
    # S8C1T, but DECSCL is preferred.


xtpushsgr_a_alias = CSI + '#p'                  # CSI # p           |
xtpushsgr_alias   = CSI + Ps + ';' + Ps + '#p'  # CSI Ps ; Ps # p   | Push video attributes onto stack (XTPUSHSGR), xterm.  This is an alias for CSI # { , used to work around language limitations of C#.


# CSI Ps q
class decll(metaclass=ParamMeta):
    """Load LEDs (DECLL), VT100."""
    __seq = CSI + Ps[0, 1, 2, 3, 21, 22, 23] + 'q'
    CLEAR_ALL              = __seq(0)   # Ps = 0  -> Clear all LEDS (default).
    LIGHT_NUM_LOCK         = __seq(1)   # Ps = 1  -> Light Num Lock.
    LIGHT_CAPS_LOCK        = __seq(2)   # Ps = 2  -> Light Caps Lock.
    LIGHT_SCROLL_LOCK      = __seq(3)   # Ps = 3  -> Light Scroll Lock.
    EXTINGUISH_NUM_LOCK    = __seq(21)  # Ps = 2 1  -> Extinguish Num Lock.
    EXTINGUISH_CAPS_LOCK   = __seq(22)  # Ps = 2 2  -> Extinguish Caps Lock.
    EXTINGUISH_SCROLL_LOCK = __seq(23)  # Ps = 2 3  -> Extinguish Scroll Lock.


# CSI Ps SP q
class decscusr(metaclass=ParamMeta):
    """Set cursor style (DECSCUSR), VT520."""
    __seq = CSI + Ps[0, 1, 2, 3, 4, 5, 6] + ' q'
    BLINK_BLOCK         = __seq(0)  # Ps = 0  -> blinking block.
    BLINK_BLOCK_DEFAULT = __seq(1)  # Ps = 1  -> blinking block (default).
    STEADY_BLOCK        = __seq(2)  # Ps = 2  -> steady block.
    BLINK_UNDERLINE     = __seq(3)  # Ps = 3  -> blinking underline.
    STEADY_UNDERLINE    = __seq(4)  # Ps = 4  -> steady underline.
    BLINK_BAR           = __seq(5)  # Ps = 5  -> blinking bar (xterm).
    STEADY_BAR          = __seq(6)  # Ps = 6  -> steady bar (xterm).


# CSI Ps " q
class decsca(metaclass=ParamMeta):
    """Select character protection attribute (DECSCA)."""
    __seq = CSI + Ps[0, 1, 2] + '"q'
    CAN_ERASE_DEFAULT = __seq(0)  # Ps = 0  -> DECSED and DECSEL can erase (default).
    CANNOT_ERASE      = __seq(1)  # Ps = 1  -> DECSED and DECSEL cannot erase.
    CAN_ERASE         = __seq(2)  # Ps = 2  -> DECSED and DECSEL can erase.


xtpopsgr_alias = CSI + '#q'                                                # CSI # q                          | Pop video attributes from stack (XTPOPSGR), xterm.  This is an alias for CSI # } , used to work around language limitations of C#.
decstbm        = CSI + Ps + ';' + Ps + 'r'                                 # CSI Ps ; Ps r                    | Set Scrolling Region [top;bottom] (default = full size of window) (DECSTBM), VT100.
_rdpmv         = CSI + '?' + Ps + 'r'                                      # CSI ? Pm r                       | Restore DEC Private Mode Values.  The value of Ps previously saved is restored.  Ps values are the same as for DECSET.
deccara        = CSI + Ps+';'+Ps+';'+Ps+';'+Ps+';'+Ps[0, 1, 4, 5, 7]+'$r'  # CSI Pt ; Pl ; Pb ; Pr ; Ps $ r   | Change Attributes in Rectangular Area (DECCARA), VT400 and up. Pt ; Pl ; Pb ; Pr denotes the rectangle. Ps denotes the SGR attributes to change: 0, 1, 4, 5, 7.
scosc          = CSI + 's'                                                 # CSI s                            | Save cursor, available only when DECLRMM is disabled (SCOSC, also ANSI.SYS).
decslrm        = CSI + Ps + ';' + Ps + 's'                                 # CSI Pl ; Pr s                    | Set left and right margins (DECSLRM), VT420 and up.  This is available only when DECLRMM is enabled.
_sdpmv         = CSI + '?' + Ps + 's'                                      # CSI ? Pm s                       | Save DEC Private Mode Values.  Ps values are the same as for DECSET.


# CSI Ps ; Ps ; Ps t
class _wm(metaclass=ParamMeta):
    """Window manipulation (from dtterm, as well as extensions by xterm)."""
    __seq = CSI + Ps + ';' + Ps + ';' + Ps + 't'
    # These controls may be disabled using the allowWindowOps resource.

    # xterm uses Extended Window Manager Hints (EWMH) to maximize
    # the window.  Some window managers have incomplete support for
    # EWMH.  For instance, fvwm, flwm and quartz-wm advertise sup-
    # port for maximizing windows horizontally or vertically, but in
    # fact equate those to the maximize operation.

    # Valid values for the first (and any additional parameters) are:
    DEICONIFY                  = __seq(1,  None, None)     # Ps = 1  -> De-iconify window.
    ICONIFY                    = __seq(2,  None, None)     # Ps = 2  -> Iconify window.
    @staticmethod
    def move_window(x, y):      return _wm.__seq(3, x, y)  # Ps = 3 ;  x ;  y -> Move window to [x, y].
    @staticmethod
    def resize_window(w, h):    return _wm.__seq(4, h, w)  # Ps = 4 ;  height ;  width -> Resize the xterm window to given height and width in pixels.  Omitted parameters reuse the current height or width.  Zero parameters use the display's height or width.
    TO_FRONT                   = __seq(5,  None, None)     # Ps = 5  -> Raise the xterm window to the front of the stacking order.
    TO_BACK                    = __seq(6,  None, None)     # Ps = 6  -> Lower the xterm window to the bottom of the stacking order.
    REFRESH                    = __seq(7,  None, None)     # Ps = 7  -> Refresh the xterm window.
    @staticmethod
    def resize_text_area(w, h): return _wm.__seq(8, h, w)  # Ps = 8 ;  height ;  width -> Resize the text area to given height and width in characters.  Omitted parameters reuse the current height or width.  Zero parameters use the display's height or width.
    MAXIMIZED_RESTORE          = __seq(9,     0, None)     # Ps = 9 ;  0  -> Restore maximized window.
    MAXIMIZE                   = __seq(9,     1, None)     # Ps = 9 ;  1  -> Maximize window (i.e., resize to screen size).
    MAXIMIZE_V                 = __seq(9,     2, None)     # Ps = 9 ;  2  -> Maximize window vertically.
    MAXIMIZE_H                 = __seq(9,     3, None)     # Ps = 9 ;  3  -> Maximize window horizontally.
    FULL_SCREEN_UNDO           = __seq(10,    0, None)     # Ps = 1 0 ;  0  -> Undo full-screen mode.
    FULL_SCREEN                = __seq(10,    1, None)     # Ps = 1 0 ;  1  -> Change to full-screen.
    FULL_SCREEN_TOGGLE         = __seq(10,    2, None)     # Ps = 1 0 ;  2  -> Toggle full-screen.
    REPORT_ICONIFIED           = __seq(11, None, None)     # Ps = 1 1  -> Report xterm window state. If the xterm window is non-iconified, it returns CSI 1 t . If the xterm window is iconified, it returns CSI 2 t .
    REPORT_POS                 = __seq(13, None, None)     # Ps = 1 3  -> Report xterm window position. Note: X Toolkit positions can be negative, but the reported values are unsigned, in the range 0-65535.  Negative values correspond to 32768-65535. Result is CSI 3 ; x ; y t
    REPORT_POS_TEXT_AREA       = __seq(13,    2, None)     # Ps = 1 3 ;  2  -> Report xterm text-area position. Result is CSI 3 ; x ; y t
    REPORT_SIZE_TEXT_AREA      = __seq(14, None, None)     # Ps = 1 4  -> Report xterm text area size in pixels. Result is CSI  4 ;  height ;  width t
    REPORT_SIZE_WINDOW         = __seq(14,    2, None)     # Ps = 1 4 ;  2  -> Report xterm window size in pixels. Normally xterm's window is larger than its text area, since it includes the frame (or decoration) applied by the window manager, as well as the area used by a scroll-bar. Result is CSI  4 ;  height ;  width t
    REPORT_SIZE_SCREEN         = __seq(15, None, None)     # Ps = 1 5  -> Report size of the screen in pixels. Result is CSI  5 ;  height ;  width t
    REPORT_SIZE_CHAR_CELL      = __seq(16, None, None)     # Ps = 1 6  -> Report xterm character cell size in pixels. Result is CSI  6 ;  height ;  width t
    REPORT_CHAR_SIZE_TEXT_AREA = __seq(18, None, None)     # Ps = 1 8  -> Report the size of the text area in characters. Result is CSI  8 ;  height ;  width t
    REPORT_CHAR_SIZE_SCREEN    = __seq(19, None, None)     # Ps = 1 9  -> Report the size of the screen in characters. Result is CSI  9 ;  height ;  width t
    REPORT_ICON_LABEL          = __seq(20, None, None)     # Ps = 2 0  -> Report xterm window's icon label. Result is OSC  L  label ST
    REPORT_WINDOW_TITLE        = __seq(21, None, None)     # Ps = 2 1  -> Report xterm window's title. Result is OSC  l  label ST

    SAVE_ICON_AND_TITLE        = __seq(22,    0, None)     # Ps = 2 2 ; 0  -> Save xterm icon and window title on stack.
    SAVE_ICON                  = __seq(22,    1, None)     # Ps = 2 2 ; 1  -> Save xterm icon title on stack.
    SAVE_TITLE                 = __seq(22,    2, None)     # Ps = 2 2 ; 2  -> Save xterm window title on stack.
    RESTORE_ICON_AND_TITLE     = __seq(23,    0, None)     # Ps = 2 3 ; 0  -> Restore xterm icon and window title from stack.
    RESTORE_ICON               = __seq(23,    1, None)     # Ps = 2 3 ; 1  -> Restore xterm icon title from stack.
    RESTORE_TITLE              = __seq(23,    2, None)     # Ps = 2 3 ; 2  -> Restore xterm window title from stack.

    @staticmethod
    def resize_to_lines(h):                                # Ps >= 2 4  -> Resize to Ps lines (DECSLPP), VT340 and VT420. xterm adapts this by resizing its window.
        assert int(h) >= 24
        return _wm.__seq(h, None, None)


# CSI > Ps ; Ps t
class _tmfs(metaclass=ParamMeta):
    """This xterm control sets one or more features of the title modes.  Each parameter enables a single feature."""
    __seq = CSI + '>' + Ps[0, 1, 2, 3] + ';' + Ps + 't'
    @staticmethod
    def set_label_hex(x):    return _tmfs.__seq(0, x)  # Ps = 0  -> Set window/icon labels using hexadecimal.
    @staticmethod
    def query_label_hex(x):  return _tmfs.__seq(1, x)  # Ps = 1  -> Query window/icon labels using hexadecimal.
    @staticmethod
    def set_label_utf8(x):   return _tmfs.__seq(2, x)  # Ps = 2  -> Set window/icon labels using UTF-8.
    @staticmethod
    def query_label_utf8(x): return _tmfs.__seq(3, x)  # Ps = 3  -> Query window/icon labels using UTF-8.  (See discussion of Title Modes)


# CSI Ps SP t
class decswbv(metaclass=ParamMeta):
    """Set warning-bell volume (DECSWBV), VT520."""
    __seq = CSI + Ps[0, 1, 2, 3, 4, 5, 6, 7, 8] + ' t'
    V0_OFF  = __seq(0)  # Ps = 0  or 1  -> off.
    V1_OFF  = __seq(1)  # Ps = 0  or 1  -> off.
    V2_LOW  = __seq(2)  # Ps = 2 , 3  or 4  -> low.
    V3_LOW  = __seq(3)  # Ps = 2 , 3  or 4  -> low.
    V4_LOW  = __seq(4)  # Ps = 2 , 3  or 4  -> low.
    V5_HIGH = __seq(5)  # Ps = 5 , 6 , 7 , or 8  -> high.
    V6_HIGH = __seq(6)  # Ps = 5 , 6 , 7 , or 8  -> high.
    V7_HIGH = __seq(7)  # Ps = 5 , 6 , 7 , or 8  -> high.
    V8_HIGH = __seq(8)  # Ps = 5 , 6 , 7 , or 8  -> high.


decrara = CSI +Ps+';'+Ps+';'+Ps+';'+Ps+';'+Ps[1, 4, 5, 7]+'$t'  # CSI Pt ; Pl ; Pb ; Pr ; Ps $ t   | Reverse Attributes in Rectangular Area (DECRARA), VT400 and up. Pt ; Pl ; Pb ; Pr denotes the rectangle. Ps denotes the attributes to reverse, i.e.,  1, 4, 5, 7.
scorc   = CSI + 'u'                                             # CSI u                            | Restore cursor (SCORC, also ANSI.SYS).


# CSI Ps SP u
class decsmbv(metaclass=ParamMeta):
    """Set margin-bell volume (DECSMBV), VT520."""
    __seq = CSI + Ps[0, 1, 2, 3, 4, 5, 6, 7, 8] + ' u'
    V0_HIGH = __seq(0)  # Ps = 0 , 5 , 6 , 7 , or 8  -> high.
    V1_OFF  = __seq(1)  # Ps = 1  -> off.
    V2_LOW  = __seq(2)  # Ps = 2 , 3  or 4  -> low.
    V3_LOW  = __seq(3)  # Ps = 2 , 3  or 4  -> low.
    V4_LOW  = __seq(4)  # Ps = 2 , 3  or 4  -> low.
    V5_HIGH = __seq(5)  # Ps = 0 , 5 , 6 , 7 , or 8  -> high.
    V6_HIGH = __seq(6)  # Ps = 0 , 5 , 6 , 7 , or 8  -> high.
    V7_HIGH = __seq(7)  # Ps = 0 , 5 , 6 , 7 , or 8  -> high.
    V8_HIGH = __seq(8)  # Ps = 0 , 5 , 6 , 7 , or 8  -> high.


deccra = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '$v'   # CSI Pt ; Pl ; Pb ; Pr ; Pp ; Pt ; Pl ; Pp $ v     Copy Rectangular Area (DECCRA), VT400 and up. Pt ; Pl ; Pb ; Pr denotes the rectangle. Pp denotes the source page. Pt ; Pl denotes the target location. Pp denotes the target page.
decefr = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + "'w"   # CSI Pt ; Pl ; Pb ; Pr ' w     Enable Filter Rectangle (DECEFR), VT420 and up. Parameters are [top;left;bottom;right]. Defines the coordinates of a filter rectangle and activates it.  Anytime the locator is detected outside of the filter rectangle, an outside rectangle event is generated and the rectangle is disabled.  Filter rectangles are always treated as "one-shot" events.  Any parameters that are omitted default to the current locator position.  If all parameters are omitted, any locator motion will be reported.  DECELR always cancels any prevous rectangle definition.


# CSI Ps * x
class decsace(metaclass=ParamMeta):
    """Select Attribute Change Extent (DECSACE), VT420 and up."""
    __seq = CSI + Ps[0, 1, 2] + '*x'
    START_TO_END_0 = __seq(0)  # Ps = 0  -> from start to end position, wrapped.
    START_TO_END_1 = __seq(1)  # Ps = 1  -> from start to end position, wrapped.
    EXACT_RECT     = __seq(2)  # Ps = 2  -> rectangle (exact).


decfra = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '$x'    # CSI Pc ; Pt ; Pl ; Pb ; Pr $ x   | Fill Rectangular Area (DECFRA), VT420 and up. Pc is the character to use. Pt ; Pl ; Pb ; Pr denotes the rectangle.


# CSI Ps # y
class xtchecksum(metaclass=ParamMeta):
    """Select checksum extension (XTCHECKSUM), xterm.  The bits of Ps modify the calculation of the checksum returned by DECRQCRA:"""
    __seq = CSI + Ps[0, 1, 2, 3, 4, 5] + '#y'
    NO_NEGATE           = __seq(0)  # 0  -> do not negate the result.
    EXCLUDE_VIDEO_ATTRS = __seq(1)  # 1  -> do not report the VT100 video attributes.
    INCLUDE_BLANKS      = __seq(2)  # 2  -> do not omit checksum for blanks.
    OMIT_UNINITIALISED  = __seq(3)  # 3  -> omit checksum for cells not explicitly initialized.
    NO_8_BIT_MASK       = __seq(4)  # 4  -> do not mask cell value to 8 bits or ignore combining characters.
    NO_7_BIT_MASK       = __seq(5)  # 5  -> do not mask cell value to 7 bits.


decera = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '$z'   # CSI Pt ; Pl ; Pb ; Pr $ z   | Erase Rectangular Area (DECERA), VT400 and up. Pt ; Pl ; Pb ; Pr denotes the rectangle.
xtpushsgr = CSI + '#{'                                      # CSI # {                     |


# CSI Ps ; Ps # {
class xtpushsgr_xx(metaclass=ParamMeta):
    """
    Push video attributes onto stack (XTPUSHSGR), xterm.
    The optional parameters correspond to the SGR encoding for video attributes,
    except for colors (which do not have a unique SGR code):
    """
    __seq = CSI + Ps + ';' + Ps + '#{'
    BOLD             = __seq(1, None)   # Ps = 1  -> Bold.
    FAINT            = __seq(2, None)   # Ps = 2  -> Faint.
    ITALIC           = __seq(3, None)   # Ps = 3  -> Italicized.
    UNDERLINE        = __seq(4, None)   # Ps = 4  -> Underlined.
    BLINK            = __seq(5, None)   # Ps = 5  -> Blink.
    INVERSE          = __seq(7, None)   # Ps = 7  -> Inverse.
    INVISIBLE        = __seq(8, None)   # Ps = 8  -> Invisible.
    STRIKETHROUGH    = __seq(9, None)   # Ps = 9  -> Crossed-out characters.
    FG               = __seq(10, None)  # Ps = 1 0  -> Foreground color.
    BG               = __seq(11, None)  # Ps = 1 1  -> Background color.
    DOUBLE_UNDERLINE = __seq(21, None)  # Ps = 2 1  -> Doubly-underlined.
    # If no parameters are given, all of the video attributes are
    # saved.  The stack is limited to 10 levels.


decsera = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '${'  # CSI Pt ; Pl ; Pb ; Pr $ {   | Selective Erase Rectangular Area (DECSERA), VT400 and up. Pt ; Pl ; Pb ; Pr denotes the rectangle.


# CSI Ps $ |
class decscpp(metaclass=ParamMeta):
    """Select columns per page (DECSCPP), VT340."""
    __seq = CSI + Ps[0, 80, 132] + '$|'
    C0   = __seq(0)    # Ps = 0  -> 80 columns, default if Ps omitted.
    C80  = __seq(80)   # Ps = 8 0  -> 80 columns.
    C132 = __seq(132)  # Ps = 1 3 2  -> 132 columns.


decsnls  = CSI + Ps + '*|'   # CSI Ps * |   | Select number of lines per screen (DECSNLS), VT420 and up.
xtpopsgr = CSI + '#}'        # CSI # }      | Pop video attributes from stack (XTPOPSGR), xterm.  Popping restores the video-attributes which were saved using XTPUSHSGR to their previous state.
decic    = CSI + Pm + "'}"   # CSI Pm ' }   | Insert Ps Column(s) (default = 1) (DECIC), VT420 and up.
decdc    = CSI + Pm + "'~"   # CSI Pm ' ~   | Delete Ps Column(s) (default = 1) (DECDC), VT420 and up.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - -REQUEST- - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# CSI ? Pi ; Pa ; Pv S
#           If configured to support either Sixel Graphics or ReGIS Graphics, xterm accepts a three-parameter control sequence, where Pi, Pa and Pv are the item, action and value:
#
#             Pi = 1  -> item is number of color registers.
#             Pi = 2  -> item is Sixel graphics geometry (in pixels).
#             Pi = 3  -> item is ReGIS graphics geometry (in pixels).
#
#             Pa = 1  -> read
#             Pa = 2  -> reset to default
#             Pa = 3  -> set to value in Pv
#             Pa = 4  -> read the maximum allowed value
#
#             Pv can be omitted except when setting (Pa == 3 ).
#             Pv = n <- A single integer is used for color registers.
#             Pv = width ; height <- Two integers for graphics geometry.
#
#           xterm replies with a control sequence of the same form:
#                CSI ? Pi ; Ps ; Pv S
#
#           where Ps is the status:
#             Ps = 0  -> success.
#             Ps = 1  -> error in Pi.
#             Ps = 2  -> error in Pa.
#             Ps = 3  -> failure.
#
#           On success, Pv represents the value read or set.
#
#           Notes:
#           o   The current implementation allows reading the graphics
#               sizes, but disallows modifying those sizes because that is
#               done once, using resource-values.
#           o   Graphics geometry is not necessarily the same as "window
#               size" (see the dtterm window manipulation extensions).
#               For example, xterm limits the maximum graphics geometry at
#               compile time (1000x1000 as of version 328) although the
#               window size can be larger.
#           o   While resizing a window will always change the current
#               graphics geometry, the reverse is not true.  Setting
#               graphics geometry does not affect the window size.

_graphics_item_action_value = CSI + '?' + Ps[1, 2, 3] + ';' + Ps[1, 2, 3, 4] + ';' + Pm + 'S'

# CSI Ps c  Send Device Attributes (Primary DA).
#             Ps = 0  or omitted -> request attributes from terminal.  The response depends on the decTerminalID resource setting.
#             -> CSI ? 1 ; 2 c  ("VT100 with Advanced Video Option")
#             -> CSI ? 1 ; 0 c  ("VT101 with No Options")
#             -> CSI ? 6 c  ("VT102")
#             -> CSI ? 6 2 ; Psc  ("VT220")
#             -> CSI ? 6 3 ; Psc  ("VT320")
#             -> CSI ? 6 4 ; Psc  ("VT420")
#
#           The VT100-style response parameters do not mean anything by
#           themselves.  VT220 (and higher) parameters do, telling the
#           host what features the terminal supports:
#             Ps = 1  -> 132-columns.
#             Ps = 2  -> Printer.
#             Ps = 3  -> ReGIS graphics.
#             Ps = 4  -> Sixel graphics.
#             Ps = 6  -> Selective erase.
#             Ps = 8  -> User-defined keys.
#             Ps = 9  -> National Replacement Character sets.
#             Ps = 1 5  -> Technical characters.
#             Ps = 1 6  -> Locator port.
#             Ps = 1 7  -> Terminal state interrogation.
#             Ps = 1 8  -> User windows.
#             Ps = 2 1  -> Horizontal scrolling.
#             Ps = 2 2  -> ANSI color, e.g., VT525.
#             Ps = 2 8  -> Rectangular editing.
#             Ps = 2 9  -> ANSI text locator (i.e., DEC Locator mode).
#
#           XTerm supports part of the User windows feature, providing a
#           single page (which corresponds to its visible window).  Rather
#           than resizing the font to change the number of lines/columns
#           in a fixed-size display, xterm uses the window extension con-
#           trols (DECSNLS, DECSCPP, DECSLPP) to adjust its visible win-
#           dow's size.  The "cursor coupling" controls (DECHCCM, DECPCCM,
#           DECVCCM) are ignored.

request__pda = CSI + Ps[0, 1, 2, 3, 4, 6, 8, 9, 15, 16, 17, 18, 21, 22, 28, 29] + 'c'

# CSI = Ps c
#           Send Device Attributes (Tertiary DA).
#             Ps = 0  -> report Terminal Unit ID (default), VT400.  XTerm uses zeros for the site code and serial number in its DECRPTUI response.

request__tda = CSI + '=' + Ps[0,] + 'c'

# CSI > Ps c
#           Send Device Attributes (Secondary DA).
#             Ps = 0  or omitted -> request the terminal's identification
#           code.  The response depends on the decTerminalID resource set-
#           ting.  It should apply only to VT220 and up, but xterm extends
#           this to VT100.
#             -> CSI  > Pp ; Pv ; Pc c      where Pp denotes the terminal type
#             Pp = 0  -> "VT100".
#             Pp = 1  -> "VT220".
#             Pp = 2  -> "VT240".
#             Pp = 1 8 -> "VT330".
#             Pp = 1 9 -> "VT340".
#             Pp = 2 4 -> "VT320".
#             Pp = 4 1 -> "VT420".
#             Pp = 6 1 -> "VT510".
#             Pp = 6 4 -> "VT520".
#             Pp = 6 5 -> "VT525".
#           and Pv is the firmware version (for xterm, this was originally
#           the XFree86 patch number, starting with 95).  In a DEC termi-
#           nal, Pc indicates the ROM cartridge registration number and is
#           always zero.

request__sda = CSI + '>' + Ps[0,] + 'c'

# CSI Ps n  Device Status Report (DSR).
#             Ps = 5  -> Status Report. Result ("OK") is CSI 0 n
#             Ps = 6  -> Report Cursor Position (CPR) [row;column]. Result is CSI r ; c R
#
#           Note: it is possible for this sequence to be sent by a func-
#           tion key.  For example, with the default keyboard configura-
#           tion the shifted F1 key may send (with shift-, control-, alt-
#           modifiers)
#
#             CSI 1 ; 2  R , or
#             CSI 1 ; 5  R , or
#             CSI 1 ; 6  R , etc.
#
#           The second parameter encodes the modifiers; values range from
#           2 to 16.  See the section PC-Style Function Keys for the
#           codes.  The modifyFunctionKeys and modifyKeyboard resources
#           can change the form of the string sent from the modified F1
#           key.

request__dsr = CSI + Ps[5, 6] + 'n'

# CSI ? Ps n
#           Device Status Report (DSR, DEC-specific).
#             Ps = 6  -> Report Cursor Position (DECXCPR) [row;column] as CSI ? r ; c R (assumes the default page, i.e., "1").
#             Ps = 1 5  -> Report Printer status as CSI ? 1 0 n  (ready). or CSI ? 1 1 n  (not ready).
#             Ps = 2 5  -> Report UDK status as CSI ? 2 0 n  (unlocked) or CSI ? 2 1 n  (locked).
#             Ps = 2 6  -> Report Keyboard status as CSI ? 2 7 ; 1 ; 0 ; 0 n  (North American).
#
#           The last two parameters apply to VT300 & up (keyboard ready)
#           and VT400 & up (LK01) respectively.
#
#             Ps = 5 3  -> Report Locator status as CSI ? 5 3 n  Locator available, if compiled-in, or CSI ? 5 0 n  No Locator, if not.
#             Ps = 5 5  -> Report Locator status as CSI ? 5 3 n  Locator available, if compiled-in, or CSI ? 5 0 n  No Locator, if not.
#             Ps = 5 6  -> Report Locator type as CSI ? 5 7 ; 1 n  Mouse, if compiled-in, or CSI ? 5 7 ; 0 n  Cannot identify, if not.
#             Ps = 6 2  -> Report macro space (DECMSR) as CSI Pn *  { .
#             Ps = 6 3  -> Report memory checksum (DECCKSR) as DCS Pt ! x x x x ST . Pt is the request id (from an optional parameter to the request). The x's are hexadecimal digits 0-9 and A-F.
#             Ps = 7 5  -> Report data integrity as CSI ? 7 0 n  (ready, no errors).
#             Ps = 8 5  -> Report multi-session configuration as CSI ? 8 3 n  (not configured for multiple-session operation).

request__dsr_ds = CSI + '?' + Ps[6, 15, 25, 26, 53, 55, 56, 62, 63, 75, 85] + 'n'

# CSI Ps $ p
#           Request ANSI mode (DECRQM).  For VT300 and up, reply DECRPM is
#             CSI Ps; Pm$ y
#           where Ps is the mode number as in SM/RM, and Pm is the mode value:
#             0 - not recognized
#             1 - set
#             2 - reset
#             3 - permanently set
#             4 - permanently reset

request__decrqm = CSI + Ps + '$p'

# CSI ? Ps $ p
#           Request DEC private mode (DECRQM).  For VT300 and up, reply DECRPM is
#             CSI ? Ps; Pm$ y
#           where Ps is the mode number as in DECSET/DECSET, Pm is the
#           mode value as in the ANSI DECRQM.
#           Two private modes are read-only (i.e., 1 3  and 1 4 ), pro-
#           vided only for reporting their values using this control
#           sequence.  They correspond to the resources cursorBlink and
#           cursorBlinkXOR.

request__decrqm_p = CSI + '?' + Ps + '$p'

# CSI Ps $ w
#           Request presentation state report (DECRQPSR), VT320 and up.
#             Ps = 0  -> error.
#             Ps = 1  -> cursor information report (DECCIR). Response is DCS 1 $ u Pt ST . Refer to the VT420 programming manual, which requires six pages to document the data string Pt,
#             Ps = 2  -> tab stop report (DECTABSR). Response is DCS 2 $ u Pt ST . The data string Pt is a list of the tab-stops, separated by "/" characters.

request__decrqpsr = CSI + Ps[0, 1, 2] + '$w'

# CSI Ps x  Request Terminal Parameters (DECREQTPARM).
#           if Ps is a "0" (default) or "1", and xterm is emulating VT100,
#           the control sequence elicits a response of the same form whose
#           parameters describe the terminal:
#             Ps -> the given Ps incremented by 2.
#             Pn = 1  <- no parity.
#             Pn = 1  <- eight bits.
#             Pn = 1  <- 2 8  transmit 38.4k baud.
#             Pn = 1  <- 2 8  receive 38.4k baud.
#             Pn = 1  <- clock multiplier.
#             Pn = 0  <- STP flags.

request__decreqtparm = CSI + Ps[0, 1] + 'x'

# CSI Pi ; Pg ; Pt ; Pl ; Pb ; Pr * y
#           Request Checksum of Rectangular Area (DECRQCRA), VT420 and up.
#           Response is
#           DCS Pi ! ~ x x x x ST
#             Pi is the request id.
#             Pg is the page number.
#             Pt ; Pl ; Pb ; Pr denotes the rectangle.
#             The x's are hexadecimal digits 0-9 and A-F.

request__decrqcra = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '*y'

# CSI Ps ; Pu ' z
#           Enable Locator Reporting (DECELR).
#           Valid values for the first parameter:
#             Ps = 0  -> Locator disabled (default).
#             Ps = 1  -> Locator enabled.
#             Ps = 2  -> Locator enabled for one report, then disabled. The second parameter specifies the coordinate unit for locator reports. Valid values for the second parameter:
#             Pu = 0  <- or omitted -> default to character cells.
#             Pu = 1  <- device physical pixels.
#             Pu = 2  <- character cells.

request__decelr = CSI + Ps[0, 1, 2] + ';' + Ps[0, 1, 2] + "'z"

# CSI Pm ' {
#           Select Locator Events (DECSLE).
#           Valid values for the first (and any additional parameters) are:
#             Ps = 0  -> only respond to explicit host requests (DECRQLP). This is default.  It also cancels any filter rectangle.
#             Ps = 1  -> report button down transitions.
#             Ps = 2  -> do not report button down transitions.
#             Ps = 3  -> report button up transitions.
#             Ps = 4  -> do not report button up transitions.

request__decsle = CSI + Ps[0,1,2,3,4] + "'{"

# CSI Pt ; Pl ; Pb ; Pr # |
#           Report selected graphic rendition (XTREPORTSGR), xterm.  The
#           response is an SGR sequence which contains the attributes
#           which are common to all cells in a rectangle.
#             Pt ; Pl ; Pb ; Pr denotes the rectangle.

request__xtreportsgr = CSI + Ps + ';' + Ps + ';' + Ps + ';' + Ps + '#|'

# CSI Ps ' |
#           Request Locator Position (DECRQLP).
#           Valid values for the parameter are:
#             Ps = 0 , 1 or omitted -> transmit a single DECLRP locator report.
#
#           If Locator Reporting has been enabled by a DECELR, xterm will
#           respond with a DECLRP Locator Report.  This report is also
#           generated on button up and down events if they have been
#           enabled with a DECSLE, or when the locator is detected outside
#           of a filter rectangle, if filter rectangles have been enabled
#           with a DECEFR.
#
#             -> CSI Pe ; Pb ; Pr ; Pc ; Pp &  w
#
#           Parameters are [event;button;row;column;page].
#           Valid values for the event:
#             Pe = 0  -> locator unavailable - no other parameters sent.
#             Pe = 1  -> request - xterm received a DECRQLP.
#             Pe = 2  -> left button down.
#             Pe = 3  -> left button up.
#             Pe = 4  -> middle button down.
#             Pe = 5  -> middle button up.
#             Pe = 6  -> right button down.
#             Pe = 7  -> right button up.
#             Pe = 8  -> M4 button down.
#             Pe = 9  -> M4 button up.
#             Pe = 1 0  -> locator outside filter rectangle. The "button" parameter is a bitmask indicating which buttons are pressed:
#             Pb = 0  <- no buttons down.
#             Pb & 1  <- right button down.
#             Pb & 2  <- middle button down.
#             Pb & 4  <- left button down.
#             Pb & 8  <- M4 button down.
#           The "row" and "column" parameters are the coordinates of the
#           locator position in the xterm window, encoded as ASCII decimal.
#           The "page" parameter is not used by xterm.

request__decrqlp = CSI + Ps[0, 1] + "'|"


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
