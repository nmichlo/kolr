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


from kolr.term.escape_codes.csi import sgr


# ========================================================================= #
# SGR PARAMETERS (Select Graphic Rendition)                                 #
# ∙ SGR = CSI ... m                                                         #
# ∙ https://stackoverflow.com/questions/4842424                             #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters           #
# ========================================================================= #


def _sel(n):
    def inner(idx_or_rgb):
        t = type(idx_or_rgb)
        if t == tuple:
            assert len(idx_or_rgb) == 3
            assert all(0 <= c <= 255 for c in idx_or_rgb)
            assert all(type(c) == int for c in idx_or_rgb)
            return sgr(n, 2, *idx_or_rgb)
        elif t == int:
            assert 0 <= idx_or_rgb <= 255
            return sgr(n, 5, idx_or_rgb)
        else:
            raise TypeError()
    return inner


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


RESET                     = sgr(0)     #   RESET  # Reset / Normal                        #  All attributes off.
BOLD                      = sgr(1)     #   STYLE  # Bold or increased intensity           #
FAINT                     = sgr(2)     #   STYLE  # Faint (decreased intensity)           #  Not widely supported.
ITALIC                    = sgr(3)     #   STYLE  # Italic                                #  Not widely supported. Sometimes treated as inverse.
UNDERLINE                 = sgr(4)     #   STYLE  # Underline                             nk                     = sgr(5)     #   STYLE      # Slow Blink                            #  Less than 150 blinks per minute
BLINK_RAPID               = sgr(6)     #   STYLE  # Rapid Blink                           #  MS-DOS ANSI.SYS; 150+ blicks per minute. Not widely supported
INVERT                    = sgr(7)     #   STYLE  # [[reverse video]]                     #  Swap foreground and background colors
CONCEAL                   = sgr(8)     #   STYLE  # Conceal                               #  Not widely supported.
STRIKETHROUGH             = sgr(9)     #   STYLE  # Crossed-out                           #  Characters legible, but marked for deletion.  Not widely supported.
FONT_PRIMARY              = sgr(10)    #   STYLE  # Primary(default) font                 #
# ↓↓↓↓↓ 11-19 Alternate Font ↓↓↓↓↓
FONT_ALT_1                = sgr(11)    #   STYLE  # Select alternate font: 1              #
FONT_ALT_2                = sgr(12)    #   STYLE  # Select alternate font: 2              #
FONT_ALT_3                = sgr(13)    #   STYLE  # Select alternate font: 3              #
FONT_ALT_4                = sgr(14)    #   STYLE  # Select alternate font: 4              #
FONT_ALT_5                = sgr(15)    #   STYLE  # Select alternate font: 5              #
FONT_ALT_6                = sgr(16)    #   STYLE  # Select alternate font: 6              #
FONT_ALT_7                = sgr(17)    #   STYLE  # Select alternate font: 7              #
FONT_ALT_8                = sgr(18)    #   STYLE  # Select alternate font: 8              #
FONT_ALT_9                = sgr(19)    #   STYLE  # Select alternate font: 9              #
# ↑↑↑↑↑ 11-19 Alternate Font ↑↑↑↑↑
FRANKTUR                  = sgr(20)    #   STYLE  # Fraktur                               #  Latin calligraphic hand. Hardly ever supported. Might instead be reset_style (not color)
RESET_BOLD                = sgr(21)    #   RESET  # Bold off or Double Underline          #  Bold off not widely supported; double underline hardly ever supported.
RESET_INTENSITY           = sgr(22)    #   RESET  # Normal color or intensity             #  Neither bold nor faint.
RESET_ITALIC              = sgr(23)    #   RESET  # Not italic, not Fraktur               #
RESET_UNDERLINE           = sgr(24)    #   RESET  # Underline off                         #  Not singly or doubly underlined.
RESET_BLINK               = sgr(25)    #   RESET  # Blink off                             #
# 26 <RESET BLINK FAST?>
RESET_INVERSE             = sgr(27)    #   RESET  # Inverse off                           #
RESET_CONCEAL             = sgr(28)    #   RESET  # Reveal                                #  Conceal off.
RESET_STRIKETHROUGH       = sgr(29)    #   RESET  # Not crossed out                       #
# ↓↓↓↓↓ 30-37 Set Foreground Color ↓↓↓↓↓
FG_BLACK                  = sgr(30)    #   COLOR  # Set foreground color: black           #
FG_RED                    = sgr(31)    #   COLOR  # Set foreground color: red             #
FG_GREEN                  = sgr(32)    #   COLOR  # Set foreground color: green           #
FG_YELLOW                 = sgr(33)    #   COLOR  # Set foreground color: yellow          #
FG_BLUE                   = sgr(34)    #   COLOR  # Set foreground color: blue            #
FG_MAGENTA                = sgr(35)    #   COLOR  # Set foreground color: magenta         #
FG_CYAN                   = sgr(36)    #   COLOR  # Set foreground color: cyan            #
FG_WHITE                  = sgr(37)    #   COLOR  # Set foreground color: white           #
# ↑↑↑↑↑ 30-37 Set Foreground Color ↑↑↑↑↑
fg_select                 = _sel(38)   #  SELECT  # Set general foreground color          #  Next arguments are `5;n` or `2;r;g;b`, see below.
RESET_FG                  = sgr(39)    #  RESET   # Default foreground color              #  Implementation defined (according to standard).
# ↓↓↓↓↓ 40-47 Set Background Color ↓↓↓↓↓
BG_BLACK                  = sgr(40)    #   COLOR  # Set background color: black           #
BG_RED                    = sgr(41)    #   COLOR  # Set background color: red             #
BG_GREEN                  = sgr(42)    #   COLOR  # Set background color: green           #
BG_YELLOW                 = sgr(43)    #   COLOR  # Set background color: yellow          #
BG_BLUE                   = sgr(44)    #   COLOR  # Set background color: blue            #
BG_MAGENTA                = sgr(45)    #   COLOR  # Set background color: magenta         #
BG_CYAN                   = sgr(46)    #   COLOR  # Set background color: cyan            #
BG_WHITE                  = sgr(47)    #   COLOR  # Set background color: white           #
# ↑↑↑↑↑ 40-47 Set Background Color ↑↑↑↑↑
bg_select                 = _sel(48)   #   SELECT # Set general background color          #  Next arguments are `5;n` or `2;r;g;b`, see 8bit and 24bit.
RESET_BG                  = sgr(49)    #   RESET  # Default background color              #  Implementation defined (according to standard)
# 50 <UNUSED>
FRAME                     = sgr(51)    #   STYLE  # Framed                                #
ENCIRCLE                  = sgr(52)    #   STYLE  # Encircled                             #
OVERLINE                  = sgr(53)    #   STYLE  # Overlined                             #
RESET_FRAME               = sgr(54)    #   RESET  # Not framed or encircled               #
RESET_OVERLINE            = sgr(55)    #   RESET  # Not overlined                         #
# 56-59 <UNUSED>
IDEOGRAM_UNDERLINE        = sgr(60)    #   STYLE  # ideogram underline                    #  Hardly ever supported.
IDEOGRAM_DOUBLE_UNDERLINE = sgr(61)    #   STYLE  # ideogram double underline             #  Hardly ever supported.
IDEOGRAM_OVERLINE         = sgr(62)    #   STYLE  # ideogram overline                     #  Hardly ever supported.
IDEOGRAM_DOUBLE_OVERLINE  = sgr(63)    #   STYLE  # ideogram double overline              #  Hardly ever supported.
IDEOGRAM_STRESS           = sgr(64)    #   STYLE  # ideogram stress marking               #  Hardly ever supported.
RESET_IDEOGRAM            = sgr(65)    #   RESET  # ideogram attributes off               #  Reset the effects of all of 60-64.
# 66-89 <UNUSED>
# ↓↓↓↓↓ 90-97 Set Bright Foreground Color ↓↓↓↓↓
FG_BRIGHT_BLACK           = sgr(90)    #   COLOR  # Set bright foreground color: black    #
FG_BRIGHT_RED             = sgr(91)    #   COLOR  # Set bright foreground color: red      #
FG_BRIGHT_GREEN           = sgr(92)    #   COLOR  # Set bright foreground color: green    #
FG_BRIGHT_YELLOW          = sgr(93)    #   COLOR  # Set bright foreground color: yellow   #
FG_BRIGHT_BLUE            = sgr(94)    #   COLOR  # Set bright foreground color: blue     #
FG_BRIGHT_MAGENTA         = sgr(95)    #   COLOR  # Set bright foreground color: magenta  #
FG_BRIGHT_CYAN            = sgr(96)    #   COLOR  # Set bright foreground color: cyan     #
FG_BRIGHT_WHITE           = sgr(97)    #   COLOR  # Set bright foreground color: white    #
# ↑↑↑↑↑ 90-97 Set Bright Foreground Color ↑↑↑↑↑ #
# 98-99 <UNUSED>
# ↓↓↓↓↓ 100-107 Set Bright Background Color ↓↓↓↓↓
BG_BRIGHT_BLACK           = sgr(100)   #   COLOR  # Set bright background color: black    #
BG_BRIGHT_RED             = sgr(101)   #   COLOR  # Set bright background color: red      #
BG_BRIGHT_GREEN           = sgr(102)   #   COLOR  # Set bright background color: green    #
BG_BRIGHT_YELLOW          = sgr(103)   #   COLOR  # Set bright background color: yellow   #
BG_BRIGHT_BLUE            = sgr(104)   #   COLOR  # Set bright background color: blue     #
BG_BRIGHT_MAGENTA         = sgr(105)   #   COLOR  # Set bright background color: magenta  #
BG_BRIGHT_CYAN            = sgr(106)   #   COLOR  # Set bright background color: cyan     #
BG_BRIGHT_WHITE           = sgr(107)   #   COLOR  # Set bright background color: white    #
# ↑↑↑↑↑ 100-107 Set Bright Background Color ↑↑↑↑↑


# ========================================================================= \#
# END                                                                       \#
# ========================================================================= \#
