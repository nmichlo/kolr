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
from collections import defaultdict


# ========================================================================= #
# Events                                                                    #
# ========================================================================= #


class Observable(object):

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        assert callable(observer)
        self._observers.add(observer)
        return observer

    def detach(self, observer):
        self._observers.remove(observer)
        return observer

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            try:
                observer(*args, **kwargs)
            except:
                import traceback
                traceback.print_exc()


class Emitter(object):
    # VUE: https://vuejs.org/v2/api/#vm-off
    #   -  $on() : Listen to events
    #   -  $notify() : Trigger events on self
    #   -  $dispatch() : Dispatch an event that propagates upward along the parent chain
    #   -  $broadcast() : Broadcast an event that propagates downward to all descendants

    def __init__(self, allowed=None):
        self._allowed = set(allowed) if allowed else False
        self._observables = defaultdict(Observable)

    def __getitem__(self, key):
        if self._allowed:
            assert key in self._allowed
        return self._observables[key]

    def on(self, key, observer=None):
        if observer is None:
            return self[key].attach
        return self[key].attach(observer)

    def off(self, key, observer):
        return self[key].detach(observer)

    def emit(self, key, *args, **kwargs):
        return self[key].notify(*args, **kwargs)
    
    def emit_func(self, key):
        return self[key].notify


# ========================================================================= #
# END                                                                       #
# ========================================================================= #

