
# ========================================================================= #
# Kolrs                                                                     #
# ========================================================================= #

# TODO: replace with more robust methods in kolr.term.sgr_params
# TODO: remove duplicated effort and use kolr.term.sgr_params instead
black = "\033[30m"   ; grey = "\033[90m"     ; bblack = "\033[40m"   ; bgrey = "\033[100m"     ;
red = "\033[31m"     ; lred = "\033[91m"     ; bred = "\033[41m"     ; blred = "\033[101m"     ;
green = "\033[32m"   ; lgreen = "\033[92m"   ; bgreen = "\033[42m"   ; blgreen = "\033[102m"   ;
yellow = "\033[33m"  ; lyellow = "\033[93m"  ; byellow = "\033[43m"  ; blyellow = "\033[103m"  ;
blue = "\033[34m"    ; lblue = "\033[94m"    ; bblue = "\033[44m"    ; blblue = "\033[104m"    ;
magenta = "\033[35m" ; lmagenta = "\033[95m" ; bmagenta = "\033[45m" ; blmagenta = "\033[105m" ;
cyan = "\033[36m"    ; lcyan = "\033[96m"    ; bcyan = "\033[46m"    ; blcyan = "\033[106m"    ;
lgrey = "\033[37m"   ; white = "\033[97m"    ; blgrey = "\033[47m"   ; blwhite = "\033[107m"   ;

bold = "\033[1m"      ; reset_bold = "\033[21m"      ;
dim = "\033[2m"       ; reset_dim = "\033[22m"       ;
underline = "\033[4m" ; reset_underline = "\033[24m" ;
blink = "\033[5m"     ; reset_blink = "\033[25m"     ;
reverse = "\033[7m"   ; reset_reverse = "\033[27m"   ;
hidden = "\033[8m"    ; reset_hidden = "\033[28m"    ;

reset = "\033[0m"             ; # reset everything
reset_fg = "\033[39m"         ; # resets foreground color only
reset_bg = "\033[49m"         ; # resets background color only
reset_attributes = "\033[20m" ; # resets underline, etc only (not colors)


# ========================================================================= #
# Kolr Dictionary                                                           #
# ========================================================================= #


# TODO: replace with more robust methods in kolr.term.sgr_params
# TODO: remove duplicated effort and use kolr.term.sgr_params instead
COLORS = {
    "black": black,     "grey": grey,         "bblack": bblack,     "bgrey": bgrey,
    "red": red,         "lred": lred,         "bred": bred,         "blred": blred,
    "green": green,     "lgreen": lgreen,     "bgreen": bgreen,     "blgreen": blgreen,
    "yellow": yellow,   "lyellow": lyellow,   "byellow": byellow,   "blyellow": blyellow,
    "blue": blue,       "lblue": lblue,       "bblue": bblue,       "blblue": blblue,
    "magenta": magenta, "lmagenta": lmagenta, "bmagenta": bmagenta, "blmagenta": blmagenta,
    "cyan": cyan,       "lcyan": lcyan,       "bcyan": bcyan,       "blcyan": blcyan,
    "lgrey": lgrey,     "white": white,       "blgrey": blgrey,     "blwhite": blwhite,

    "bold": bold,          "reset_bold": reset_bold,
    "dim": dim,            "reset_dim": reset_dim,
    "underline": underline, "reset_underline": reset_underline,
    "blink": blink,         "reset_blink": reset_blink,
    "reverse": reverse,     "reset_reverse": reset_reverse,
    "hidden": hidden,       "reset_hidden": reset_hidden,

    "reset": reset, # reset everything
    "reset_fg": reset_fg, # resets foreground color only
    "reset_bg": reset_bg, # resets background color only
    "reset_attributes": reset_attributes, # resets underline, etc only (not colors)
}


# ========================================================================= #
# Kolr Builder                                                              #
# ========================================================================= #


class Kolr:

    def __init__(self, *vals, color=None):
        self._stack = []
        self._color(*vals, color=color)

    def __str__(self) -> str:
        return ''.join((f'{c}{s}\033[0m' if c else s) for c, s in self._stack)
    def __repr__(self) -> str:
        return str(self)

    def __add__(self, val): return self._color(val, is_left=False)
    def __radd__(self, val): return self._color(val, is_left=True)

    def __call__(self, *vals, color=None):
        return self._color(*vals, color=color)

    def _color(self, *vals, color=None, is_left=False):
        if vals:
            clr = COLORS[color] if color else ''
            append_stack = []
            for val in vals:
                typ = type(val)
                if typ == str:
                    append_stack.append((clr, val))
                elif typ == Kolr:
                    if clr:
                        for c, v in val._stack:
                            append_stack.append((clr+c, v))
                    else:
                        append_stack = val._stack
                else:
                    raise TypeError(f'Invalid Type: {typ}')
            # merge
            self._stack = (append_stack + self._stack) if is_left else (self._stack + append_stack)
        # chainable
        return self


# ========================================================================= #
# MAIN                                                                      #
# ========================================================================= #


if __name__ == '__main__':
    print(Kolr('left ' + ' right' + 'fdsa', color='lgreen'))
    print(str(Kolr('left ' + Kolr('inner', color='lred')('asdf', color='reset') + ' right', color='lgreen')))

