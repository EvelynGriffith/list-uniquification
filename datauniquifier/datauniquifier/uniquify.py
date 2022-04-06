"""Perform uniquification on the provided input of a list of strings."""

from typing import List

from functools import wraps
from time import time


def timing(function):
    """Define a profiling function for execution time."""
    # Reference:
    # https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap


# Read the reference for a description of the functions:
#
# https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6
#
# Note that this module does not contain all of the functions in the post

# If you would like to do so, add and then experimentally evaluate more methods

# Make sure that you understand the purpose of the timing annotation for these functions
# Add the timing annotation to each of the following functions


@timing
def unique_set(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # Add the source code for method f7
    # You may need to add type hints or statements to support mypy checking
    # Not order preserving
    return list(set(data))


@timing
def unique_setcomprehension(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # Add the source code for method f8
    # You may need to add type hints or statements to support mypy checking
    # Order preserving
    seen = set()
    return [x for x in data if x not in seen and not seen.add(x)]


@timing
def unique_dictionary(data: List[str]) -> List[str]:
    """Perform uniquification of the input list of strings and return results in a list of strings."""
    # Add the source code for method f12
    # You may need to add type hints or statements to support mypy checking
    return list(dict.fromkeys(data))
