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
import atexit
import datetime
import sys
from cachier import cachier


# ========================================================================= #
# File Util                                                                 #
# ========================================================================= #
from kolr.util.events import Observable


def overwrite_file(file, string):
    with open(file, 'w') as file:
        file.write(string)
    return string


# TODO: remove cachier dependency
@cachier(stale_after=datetime.timedelta(days=7))
def fetch_url(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    return response.read().decode()


# ========================================================================= #
# Iterators                                                                 #
# ========================================================================= #


def is_iterable(val):
    try:
        for i in val:
            break
        return True
    except:
        return False


# ========================================================================= #
# Decorators                                                                #
# ========================================================================= #


class cached_property(object):
    """
    A property that is only computed once per object instance, it
    then replaces itself with an ordinary attribute value.
    Deleting the attribute forces it to recompute.

    Based on: https://www.pydanny.com/cached-property.html
    """

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.func.__name__] = value
        return value


# ========================================================================= #
# Singleton                                                                 #
# ========================================================================= #


_NONE = object()


class Singleton(object):
    """
    Baseclass version of a singleton.
    - This can easily be overridden by a base class so not recommended
    """
    __instance = _NONE
    def __new__(cls, *args, **kwargs):
        if cls.__instance is _NONE:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


class SingletonMeta(type):
    """
    Metaclass version of a singleton.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        instance = cls._instances.get(cls, _NONE)
        if instance is _NONE:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance


def singleton(cls):
    """
    Singleton decorator wrapping the class with SingletonMeta
    """
    class Inner(cls, metaclass=SingletonMeta):
        pass
    return Inner


# ========================================================================= #
# END                                                                       #
# ========================================================================= #
