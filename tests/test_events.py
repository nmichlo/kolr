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


from kolr.util.events import Observable, Emitter


def test_observable():
    ob = Observable()
    call_count = 0

    @ob.attach
    def on_test():
        nonlocal call_count
        call_count += 1

    assert call_count == 0
    ob.notify()
    assert call_count == 1

    ob.detach(on_test)

    assert call_count == 1
    ob.notify()
    assert call_count == 1


def test_emitter():
    obs = Emitter()
    call_count_a = 0
    call_count_b = 0

    @obs.on('test_event_a')
    def on_test_a():
        nonlocal call_count_a
        call_count_a += 1

    @obs.on('test_event_b')
    def on_test_b():
        nonlocal call_count_b
        call_count_b += 1

    assert call_count_a == 0 and call_count_b == 0
    obs.emit('test_event_a')
    assert call_count_a == 1 and call_count_b == 0
    obs.emit('test_event_b')
    assert call_count_a == 1 and call_count_b == 1

    obs.off('test_event_b', on_test_b)

    assert call_count_a == 1 and call_count_b == 1
    obs.emit('test_event_a')
    assert call_count_a == 2 and call_count_b == 1
    obs.emit('test_event_b')
    assert call_count_a == 2 and call_count_b == 1

    obs.off('test_event_a', on_test_a)

