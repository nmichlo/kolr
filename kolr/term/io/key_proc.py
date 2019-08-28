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

    _mouse_event_regex = re.compile('^' + re.escape('\x1b[') + r'<?([\d]+?);([\d]+?);([\d]+?)([mM])')

    def _mouse_event_proc(data):
        t, x, y, m = data
        # TODO: this is super inefficient
        m = {'M': 'down', 'm': 'up'}[m]
        t = {0: 'mouse-' + m, 64: 'mouse-wheel-down', 65: 'mouse-wheel-up'}.get(int(t), 'unknown-' + t)
        return t, (x, y)

    special_chars = [
        (_mouse_event_regex, _mouse_event_proc)
    ]

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
                    match = None
                    for (regex, proc) in special_chars:
                        match = regex.search(string)
                        if match:
                            strip = len(match.group())
                            keys.append(proc(match.groups()))
                            break
                    if match:
                        char = None
                if char:
                    keys.append(('key', char))
                string = string[strip:]
            return keys
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


