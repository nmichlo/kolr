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


from kolr.term.escape_codes.esc import CSI


# ========================================================================= #
# SGR PARAMETERS (Select Graphic Rendition)                                 #
# ∙ SGR = CSI ... m                                                         #
# ∙ https://stackoverflow.com/questions/4842424                             #
# ∙ https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters           #
# ========================================================================= #


def __sgr(*code):
    return f'{CSI}{";".join(str(c) for c in code)}m'


def _sel(n):
    def inner(idx_or_rgb):
        t = type(idx_or_rgb)
        if t == tuple:
            assert len(idx_or_rgb) == 3
            assert all(0 <= c <= 255 for c in idx_or_rgb)
            assert all(type(c) == int for c in idx_or_rgb)
            return __sgr(n, 2, *idx_or_rgb)
        elif t == int:
            assert 0 <= idx_or_rgb <= 255
            return __sgr(n, 5, idx_or_rgb)
        else:
            raise TypeError()
    return inner


# - - - - - - - - - - - - - - - - VARIABLES - - - - - - - - - - - - - - - - #


RESET                     = __sgr(0)     #   RESET  # Reset / Normal                        #  All attributes off.
BOLD                      = __sgr(1)     #   STYLE  # Bold or increased intensity           #
FAINT                     = __sgr(2)     #   STYLE  # Faint (decreased intensity)           #  Not widely supported.
ITALIC                    = __sgr(3)     #   STYLE  # Italic                                #  Not widely supported. Sometimes treated as inverse.
UNDERLINE                 = __sgr(4)     #   STYLE  # Underline                             nk                     = sgr(5)     #   STYLE      # Slow Blink                            #  Less than 150 blinks per minute
BLINK_RAPID               = __sgr(6)     #   STYLE  # Rapid Blink                           #  MS-DOS ANSI.SYS; 150+ blicks per minute. Not widely supported
INVERT                    = __sgr(7)     #   STYLE  # [[reverse video]]                     #  Swap foreground and background colors
CONCEAL                   = __sgr(8)     #   STYLE  # Conceal                               #  Not widely supported.
STRIKETHROUGH             = __sgr(9)     #   STYLE  # Crossed-out                           #  Characters legible, but marked for deletion.  Not widely supported.
FONT_PRIMARY              = __sgr(10)    #   STYLE  # Primary(default) font                 #
# ↓↓↓↓↓ 11-19 Alternate Font ↓↓↓↓↓
FONT_ALT_1                = __sgr(11)    #   STYLE  # Select alternate font: 1              #
FONT_ALT_2                = __sgr(12)    #   STYLE  # Select alternate font: 2              #
FONT_ALT_3                = __sgr(13)    #   STYLE  # Select alternate font: 3              #
FONT_ALT_4                = __sgr(14)    #   STYLE  # Select alternate font: 4              #
FONT_ALT_5                = __sgr(15)    #   STYLE  # Select alternate font: 5              #
FONT_ALT_6                = __sgr(16)    #   STYLE  # Select alternate font: 6              #
FONT_ALT_7                = __sgr(17)    #   STYLE  # Select alternate font: 7              #
FONT_ALT_8                = __sgr(18)    #   STYLE  # Select alternate font: 8              #
FONT_ALT_9                = __sgr(19)    #   STYLE  # Select alternate font: 9              #
# ↑↑↑↑↑ 11-19 Alternate Font ↑↑↑↑↑
FRANKTUR                  = __sgr(20)    #   STYLE  # Fraktur                               #  Latin calligraphic hand. Hardly ever supported. Might instead be reset_style (not color)
RESET_BOLD                = __sgr(21)    #   RESET  # Bold off or Double Underline          #  Bold off not widely supported; double underline hardly ever supported.
RESET_INTENSITY           = __sgr(22)    #   RESET  # Normal color or intensity             #  Neither bold nor faint.
RESET_ITALIC              = __sgr(23)    #   RESET  # Not italic, not Fraktur               #
RESET_UNDERLINE           = __sgr(24)    #   RESET  # Underline off                         #  Not singly or doubly underlined.
RESET_BLINK               = __sgr(25)    #   RESET  # Blink off                             #
# 26 <RESET BLINK FAST?>
RESET_INVERSE             = __sgr(27)    #   RESET  # Inverse off                           #
RESET_CONCEAL             = __sgr(28)    #   RESET  # Reveal                                #  Conceal off.
RESET_STRIKETHROUGH       = __sgr(29)    #   RESET  # Not crossed out                       #
# ↓↓↓↓↓ 30-37 Set Foreground Color ↓↓↓↓↓
FG_BLACK                  = __sgr(30)    #   COLOR  # Set foreground color: black           #
FG_RED                    = __sgr(31)    #   COLOR  # Set foreground color: red             #
FG_GREEN                  = __sgr(32)    #   COLOR  # Set foreground color: green           #
FG_YELLOW                 = __sgr(33)    #   COLOR  # Set foreground color: yellow          #
FG_BLUE                   = __sgr(34)    #   COLOR  # Set foreground color: blue            #
FG_MAGENTA                = __sgr(35)    #   COLOR  # Set foreground color: magenta         #
FG_CYAN                   = __sgr(36)    #   COLOR  # Set foreground color: cyan            #
FG_WHITE                  = __sgr(37)    #   COLOR  # Set foreground color: white           #
# ↑↑↑↑↑ 30-37 Set Foreground Color ↑↑↑↑↑
fg_select                 = _sel(38)     #  SELECT  # Set general foreground color          #  Next arguments are `5;n` or `2;r;g;b`, see below.
RESET_FG                  = __sgr(39)    #  RESET   # Default foreground color              #  Implementation defined (according to standard).
# ↓↓↓↓↓ 40-47 Set Background Color ↓↓↓↓↓
BG_BLACK                  = __sgr(40)    #   COLOR  # Set background color: black           #
BG_RED                    = __sgr(41)    #   COLOR  # Set background color: red             #
BG_GREEN                  = __sgr(42)    #   COLOR  # Set background color: green           #
BG_YELLOW                 = __sgr(43)    #   COLOR  # Set background color: yellow          #
BG_BLUE                   = __sgr(44)    #   COLOR  # Set background color: blue            #
BG_MAGENTA                = __sgr(45)    #   COLOR  # Set background color: magenta         #
BG_CYAN                   = __sgr(46)    #   COLOR  # Set background color: cyan            #
BG_WHITE                  = __sgr(47)    #   COLOR  # Set background color: white           #
# ↑↑↑↑↑ 40-47 Set Background Color ↑↑↑↑↑
bg_select                 = _sel(48)     #   SELECT # Set general background color          #  Next arguments are `5;n` or `2;r;g;b`, see 8bit and 24bit.
RESET_BG                  = __sgr(49)    #   RESET  # Default background color              #  Implementation defined (according to standard)
# 50 <UNUSED>
FRAME                     = __sgr(51)    #   STYLE  # Framed                                #
ENCIRCLE                  = __sgr(52)    #   STYLE  # Encircled                             #
OVERLINE                  = __sgr(53)    #   STYLE  # Overlined                             #
RESET_FRAME               = __sgr(54)    #   RESET  # Not framed or encircled               #
RESET_OVERLINE            = __sgr(55)    #   RESET  # Not overlined                         #
# 56-59 <UNUSED>
IDEOGRAM_UNDERLINE        = __sgr(60)    #   STYLE  # ideogram underline                    #  Hardly ever supported.
IDEOGRAM_DOUBLE_UNDERLINE = __sgr(61)    #   STYLE  # ideogram double underline             #  Hardly ever supported.
IDEOGRAM_OVERLINE         = __sgr(62)    #   STYLE  # ideogram overline                     #  Hardly ever supported.
IDEOGRAM_DOUBLE_OVERLINE  = __sgr(63)    #   STYLE  # ideogram double overline              #  Hardly ever supported.
IDEOGRAM_STRESS           = __sgr(64)    #   STYLE  # ideogram stress marking               #  Hardly ever supported.
RESET_IDEOGRAM            = __sgr(65)    #   RESET  # ideogram attributes off               #  Reset the effects of all of 60-64.
# 66-89 <UNUSED>
# ↓↓↓↓↓ 90-97 Set Bright Foreground Color ↓↓↓↓↓
FG_BRIGHT_BLACK           = __sgr(90)    #   COLOR  # Set bright foreground color: black    #
FG_BRIGHT_RED             = __sgr(91)    #   COLOR  # Set bright foreground color: red      #
FG_BRIGHT_GREEN           = __sgr(92)    #   COLOR  # Set bright foreground color: green    #
FG_BRIGHT_YELLOW          = __sgr(93)    #   COLOR  # Set bright foreground color: yellow   #
FG_BRIGHT_BLUE            = __sgr(94)    #   COLOR  # Set bright foreground color: blue     #
FG_BRIGHT_MAGENTA         = __sgr(95)    #   COLOR  # Set bright foreground color: magenta  #
FG_BRIGHT_CYAN            = __sgr(96)    #   COLOR  # Set bright foreground color: cyan     #
FG_BRIGHT_WHITE           = __sgr(97)    #   COLOR  # Set bright foreground color: white    #
# ↑↑↑↑↑ 90-97 Set Bright Foreground Color ↑↑↑↑↑ #
# 98-99 <UNUSED>
# ↓↓↓↓↓ 100-107 Set Bright Background Color ↓↓↓↓↓
BG_BRIGHT_BLACK           = __sgr(100)   #   COLOR  # Set bright background color: black    #
BG_BRIGHT_RED             = __sgr(101)   #   COLOR  # Set bright background color: red      #
BG_BRIGHT_GREEN           = __sgr(102)   #   COLOR  # Set bright background color: green    #
BG_BRIGHT_YELLOW          = __sgr(103)   #   COLOR  # Set bright background color: yellow   #
BG_BRIGHT_BLUE            = __sgr(104)   #   COLOR  # Set bright background color: blue     #
BG_BRIGHT_MAGENTA         = __sgr(105)   #   COLOR  # Set bright background color: magenta  #
BG_BRIGHT_CYAN            = __sgr(106)   #   COLOR  # Set bright background color: cyan     #
BG_BRIGHT_WHITE           = __sgr(107)   #   COLOR  # Set bright background color: white    #
# ↑↑↑↑↑ 100-107 Set Bright Background Color ↑↑↑↑↑


# ========================================================================= \#
# END                                                                       \#
# ========================================================================= \#
