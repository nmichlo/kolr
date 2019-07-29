# Nathan Michlo

import datetime
from cachier import cachier


# ========================================================================= #
# File Util                                                                 #
# ========================================================================= #


def overwrite_file(file, string):
    with open(file, 'w') as file:
        file.write(string)
    return string


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
            return True
    except:
        return False
