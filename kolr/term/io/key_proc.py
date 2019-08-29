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


import sys
from kolr.term.escape_codes.esc import ESC
from kolr.term.io.keys import MouseKey, Key


# ========================================================================= #
# BASE                                                                      #
# ========================================================================= #


class IKeyProc(object):
    def push_chars(self, string): raise NotImplementedError()


# ========================================================================= #
# UNIX                                                                      #
# ========================================================================= #


def _create_unix():
    import re

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

    char_name_map = {
        '\x01': 'ctrl-a',
        '\x02': 'ctrl-b',
        '\x03': 'ctrl-c',
        '\x04': 'ctrl-d',
        '\x05': 'ctrl-e',
        '\x06': 'ctrl-f',
        '\x07': 'ctrl-g',
        '\x08': 'ctrl-h',
        '\x09': 'ctrl-i',
        '\x10': 'ctrl-j',
        '\x11': 'ctrl-k',
        '\x12': 'ctrl-l',
        '\x13': 'ctrl-m',
        '\x14': 'ctrl-n',
        '\x15': 'ctrl-o',
        '\x16': 'ctrl-p',
        '\x17': 'ctrl-q',
        '\x18': 'ctrl-r',
        '\x19': 'ctrl-s',
        '\x20': 'ctrl-t',
        '\x21': 'ctrl-u',
        '\x22': 'ctrl-v',
        '\x23': 'ctrl-w',
        '\x24': 'ctrl-x',
        '\x25': 'ctrl-y',
        '\x26': 'ctrl-z',
        '\x1b': 'escape'
    }

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

    _mouse_event_regex = re.compile('^' + re.escape('\x1b[') + r'<?([\d]+?);([\d]+?);([\d]+?)([mM])')

    def _mouse_event_proc(data):
        t, x, y, m = data
        # TODO: this is super inefficient
        m = {'M': 'down', 'm': 'up'}[m]
        t = {0: 'mouse-' + m, 64: 'mouse-wheel-down', 65: 'mouse-wheel-up'}.get(int(t), 'unknown-' + t)
        return MouseKey(t, (int(x)-1, int(y)-1))

    special_chars = [
        (_mouse_event_regex, _mouse_event_proc)
    ]

    def search(string):
        for (regex, proc) in special_chars:
            match = regex.search(string)
            if match:
                return proc(match.groups()), match.group()
        return None, None

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

    class _Unix(IKeyProc):
        def __init__(self):
            self._chars_buf = []

        def push_chars(self, chars):
            self._chars_buf.append(chars)

        def pop_keys(self):
            string = ''.join(self._chars_buf)
            keys, self._chars_buf = [], []
            while string:
                char, strip = string[0], 1
                if char == ESC:
                    key, substr = search(string)
                    if substr:
                        strip = len(substr)
                        keys.append(key)
                    else:
                        keys.append(Key(char_name_map.get(char, char), ESC))
                else:
                    keys.append(Key(char_name_map.get(char, char), char))
                string = string[strip:]
            return keys

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

    return _Unix

# ========================================================================= #
# WINDOWS                                                                   #
# ========================================================================= #


def _create_windows():
    class _Windows(IKeyProc):
        pass

    raise NotImplementedError('Windows is unsupported')

    return _Windows


# ========================================================================= #
# INTERFACE                                                                 #
# ========================================================================= #


if sys.platform in ('win32', 'cygwin'):
    KeyProc = _create_windows()
else:
    KeyProc = _create_unix()


# ========================================================================= #
# END                                                                       #
# ========================================================================= #


