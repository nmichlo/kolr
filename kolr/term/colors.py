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


from codegen.gen.ansi_escape_code import L_ansi_escape_code___colors___3_or_4_bit
from kolr.color import Color


# ========================================================================= #
# Colors                                                                    #
# https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit                    #
# ========================================================================= #


_TERM_COLORS = L_ansi_escape_code___colors___3_or_4_bit


# ========================================================================= #
# 8-BIT COLORS                                                              #
# ========================================================================= #

COLORS_8_BIT_WIKIPEDIA = [
    # https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
    # Standard colors
    ('c0_black', '#000000'), ('c1_red', '#800000'), ('c2_green', '#008000'), ('c3_yellow', '#808000'), ('c4_blue', '#000080'), ('c5_magenta', '#800080'), ('c6_cyan', '#008080'), ('c7_white', '#c0c0c0'),
    # High-intensity colors
    ('c8_bright_black', '#808080'), ('c9_bright_red', '#ff0000'), ('c10_bright_green', '#00ff00'), ('c11_bright_yellow', '#ffff00'), ('c12_bright_blue', '#0000ff'), ('c13_bright_magenta', '#ff00ff'), ('c14_bright_cyan', '#00ffff'), ('c15_bright_white', '#ffffff'),
    # COLORS:
    ('c16_cube', '#000000'), ('c17_cube', '#00005f'), ('c18_cube', '#000087'), ('c19_cube', '#0000af'), ('c20_cube', '#0000d7'), ('c21_cube', '#0000ff'), ('c22_cube', '#005f00'), ('c23_cube', '#005f5f'), ('c24_cube', '#005f87'), ('c25_cube', '#005faf'), ('c26_cube', '#005fd7'), ('c27_cube', '#005fff'), ('c28_cube', '#008700'), ('c29_cube', '#00875f'), ('c30_cube', '#008787'), ('c31_cube', '#0087af'), ('c32_cube', '#0087d7'), ('c33_cube', '#0087ff'), ('c34_cube', '#00af00'), ('c35_cube', '#00af5f'), ('c36_cube', '#00af87'), ('c37_cube', '#00afaf'), ('c38_cube', '#00afd7'), ('c39_cube', '#00afff'), ('c40_cube', '#00d700'), ('c41_cube', '#00d75f'), ('c42_cube', '#00d787'), ('c43_cube', '#00d7af'), ('c44_cube', '#00d7d7'), ('c45_cube', '#00d7ff'), ('c46_cube', '#00ff00'), ('c47_cube', '#00ff5f'), ('c48_cube', '#00ff87'), ('c49_cube', '#00ffaf'), ('c50_cube', '#00ffd7'), ('c51_cube', '#00ffff'),
    ('c52_cube', '#5f0000'), ('c53_cube', '#5f005f'), ('c54_cube', '#5f0087'), ('c55_cube', '#5f00af'), ('c56_cube', '#5f00d7'), ('c57_cube', '#5f00ff'), ('c58_cube', '#5f5f00'), ('c59_cube', '#5f5f5f'), ('c60_cube', '#5f5f87'), ('c61_cube', '#5f5faf'), ('c62_cube', '#5f5fd7'), ('c63_cube', '#5f5fff'), ('c64_cube', '#5f8700'), ('c65_cube', '#5f875f'), ('c66_cube', '#5f8787'), ('c67_cube', '#5f87af'), ('c68_cube', '#5f87d7'), ('c69_cube', '#5f87ff'), ('c70_cube', '#5faf00'), ('c71_cube', '#5faf5f'), ('c72_cube', '#5faf87'), ('c73_cube', '#5fafaf'), ('c74_cube', '#5fafd7'), ('c75_cube', '#5fafff'), ('c76_cube', '#5fd700'), ('c77_cube', '#5fd75f'), ('c78_cube', '#5fd787'), ('c79_cube', '#5fd7af'), ('c80_cube', '#5fd7d7'), ('c81_cube', '#5fd7ff'), ('c82_cube', '#5fff00'), ('c83_cube', '#5fff5f'), ('c84_cube', '#5fff87'), ('c85_cube', '#5fffaf'), ('c86_cube', '#5fffd7'), ('c87_cube', '#5fffff'),
    ('c88_cube', '#870000'), ('c89_cube', '#87005f'), ('c90_cube', '#870087'), ('c91_cube', '#8700af'), ('c92_cube', '#8700d7'), ('c93_cube', '#8700ff'), ('c94_cube', '#875f00'), ('c95_cube', '#875f5f'), ('c96_cube', '#875f87'), ('c97_cube', '#875faf'), ('c98_cube', '#875fd7'), ('c99_cube', '#875fff'), ('c100_cube', '#878700'), ('c101_cube', '#87875f'), ('c102_cube', '#878787'), ('c103_cube', '#8787af'), ('c104_cube', '#8787d7'), ('c105_cube', '#8787ff'), ('c106_cube', '#87af00'), ('c107_cube', '#87af5f'), ('c108_cube', '#87af87'), ('c109_cube', '#87afaf'), ('c110_cube', '#87afd7'), ('c111_cube', '#87afff'), ('c112_cube', '#87d700'), ('c113_cube', '#87d75f'), ('c114_cube', '#87d787'), ('c115_cube', '#87d7af'), ('c116_cube', '#87d7d7'), ('c117_cube', '#87d7ff'), ('c118_cube', '#87ff00'), ('c119_cube', '#87ff5f'), ('c120_cube', '#87ff87'), ('c121_cube', '#87ffaf'), ('c122_cube', '#87ffd7'), ('c123_cube', '#87ffff'),
    ('c124_cube', '#af0000'), ('c125_cube', '#af005f'), ('c126_cube', '#af0087'), ('c127_cube', '#af00af'), ('c128_cube', '#af00d7'), ('c129_cube', '#af00ff'), ('c130_cube', '#af5f00'), ('c131_cube', '#af5f5f'), ('c132_cube', '#af5f87'), ('c133_cube', '#af5faf'), ('c134_cube', '#af5fd7'), ('c135_cube', '#af5fff'), ('c136_cube', '#af8700'), ('c137_cube', '#af875f'), ('c138_cube', '#af8787'), ('c139_cube', '#af87af'), ('c140_cube', '#af87d7'), ('c141_cube', '#af87ff'), ('c142_cube', '#afaf00'), ('c143_cube', '#afaf5f'), ('c144_cube', '#afaf87'), ('c145_cube', '#afafaf'), ('c146_cube', '#afafd7'), ('c147_cube', '#afafff'), ('c148_cube', '#afd700'), ('c149_cube', '#afd75f'), ('c150_cube', '#afd787'), ('c151_cube', '#afd7af'), ('c152_cube', '#afd7d7'), ('c153_cube', '#afd7ff'), ('c154_cube', '#afff00'), ('c155_cube', '#afff5f'), ('c156_cube', '#afff87'), ('c157_cube', '#afffaf'), ('c158_cube', '#afffd7'), ('c159_cube', '#afffff'),
    ('c160_cube', '#d70000'), ('c161_cube', '#d7005f'), ('c162_cube', '#d70087'), ('c163_cube', '#d700af'), ('c164_cube', '#d700d7'), ('c165_cube', '#d700ff'), ('c166_cube', '#d75f00'), ('c167_cube', '#d75f5f'), ('c168_cube', '#d75f87'), ('c169_cube', '#d75faf'), ('c170_cube', '#d75fd7'), ('c171_cube', '#d75fff'), ('c172_cube', '#d78700'), ('c173_cube', '#d7875f'), ('c174_cube', '#d78787'), ('c175_cube', '#d787af'), ('c176_cube', '#d787d7'), ('c177_cube', '#d787ff'), ('c178_cube', '#d7af00'), ('c179_cube', '#d7af5f'), ('c180_cube', '#d7af87'), ('c181_cube', '#d7afaf'), ('c182_cube', '#d7afd7'), ('c183_cube', '#d7afff'), ('c184_cube', '#d7d700'), ('c185_cube', '#d7d75f'), ('c186_cube', '#d7d787'), ('c187_cube', '#d7d7af'), ('c188_cube', '#d7d7d7'), ('c189_cube', '#d7d7ff'), ('c190_cube', '#d7ff00'), ('c191_cube', '#d7ff5f'), ('c192_cube', '#d7ff87'), ('c193_cube', '#d7ffaf'), ('c194_cube', '#d7ffd7'), ('c195_cube', '#d7ffff'),
    ('c196_cube', '#ff0000'), ('c197_cube', '#ff005f'), ('c198_cube', '#ff0087'), ('c199_cube', '#ff00af'), ('c200_cube', '#ff00d7'), ('c201_cube', '#ff00ff'), ('c202_cube', '#ff5f00'), ('c203_cube', '#ff5f5f'), ('c204_cube', '#ff5f87'), ('c205_cube', '#ff5faf'), ('c206_cube', '#ff5fd7'), ('c207_cube', '#ff5fff'), ('c208_cube', '#ff8700'), ('c209_cube', '#ff875f'), ('c210_cube', '#ff8787'), ('c211_cube', '#ff87af'), ('c212_cube', '#ff87d7'), ('c213_cube', '#ff87ff'), ('c214_cube', '#ffaf00'), ('c215_cube', '#ffaf5f'), ('c216_cube', '#ffaf87'), ('c217_cube', '#ffafaf'), ('c218_cube', '#ffafd7'), ('c219_cube', '#ffafff'), ('c220_cube', '#ffd700'), ('c221_cube', '#ffd75f'), ('c222_cube', '#ffd787'), ('c223_cube', '#ffd7af'), ('c224_cube', '#ffd7d7'), ('c225_cube', '#ffd7ff'), ('c226_cube', '#ffff00'), ('c227_cube', '#ffff5f'), ('c228_cube', '#ffff87'), ('c229_cube', '#ffffaf'), ('c230_cube', '#ffffd7'), ('c231_cube', '#ffffff'),
    # Grayscale colors
    ('c232_grey', '#080808'), ('c233_grey', '#121212'), ('c234_grey', '#1c1c1c'), ('c235_grey', '#262626'), ('c236_grey', '#303030'), ('c237_grey', '#3a3a3a'), ('c238_grey', '#444444'), ('c239_grey', '#4e4e4e'), ('c240_grey', '#585858'), ('c241_grey', '#626262'), ('c242_grey', '#6c6c6c'), ('c243_grey', '#767676'), ('c244_grey', '#808080'), ('c245_grey', '#8a8a8a'), ('c246_grey', '#949494'), ('c247_grey', '#9e9e9e'), ('c248_grey', '#a8a8a8'), ('c249_grey', '#b2b2b2'), ('c250_grey', '#bcbcbc'), ('c251_grey', '#c6c6c6'), ('c252_grey', '#d0d0d0'), ('c253_grey', '#dadada'), ('c254_grey', '#e4e4e4'), ('c255_grey', '#eeeeee'),
]

def _make_colors_8_bit():
    # https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
    #   0->  7:  standard colors (as in ESC [ 30–37 m)
    # matches wikipedia table
    standard = [(f'c{i}_{_TERM_COLORS[i].name}', Color((128*(i%2), 128*((i//2)%2), 128*(i//4))).hex) for i in range(8)]
    standard[7] = (f'c{7}_{_TERM_COLORS[7].name}', '#c0c0c0')  # fix dark white
    #   8-> 15:  high intensity colors (as in ESC [ 90–97 m)
    # matches wikipedia table
    bright = [(f'c{i+8}_{_TERM_COLORS[i+8].name}', Color((255*(i%2), 255*((i//2)%2), 255*(i//4))).hex) for i in range(8)]
    bright[0] = (f'c{8}_{_TERM_COLORS[8].name}', '#808080')  # fix light black
    #  16->231:  6×6×6 cube (216 colors): 16 + 36×r + 6×g + b (0 ≤ r, g, b ≤ 5)
    # does not match wikipedia table
    cube = [(f'c{i+16}_cube', Color((int(255/5*(i//36)), int(255/5*((i//6)%6)), int(255/5*(i%6)))).hex) for i in range(216)]
    # 232->255:  grayscale from black to white in 24 steps
    # should be /25 for centering, does not match wikipedia table
    grays = [(f'c{i+232}_grey', Color(tuple([int(255/26*(i+1))]*3)).hex) for i in range(24)]
    # merge
    return [*standard, *bright, *cube, *grays]


# ========================================================================= #
# DETECT                                                                    #
# ========================================================================= #


COLORS_8_BIT_WIKIPEDIA = COLORS_8_BIT_WIKIPEDIA
COLORS_8_BIT = _make_colors_8_bit()

# TODO: Use _TERM_COLORS
COLORS_4_BIT = [COLORS_8_BIT[i] for i in range(2**4)]
COLORS_3_BIT = [COLORS_8_BIT[i] for i in range(2**3)]


# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    print(COLORS_8_BIT_WIKIPEDIA)
    print(COLORS_8_BIT)
    print(COLORS_4_BIT)
    print(COLORS_3_BIT)


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
