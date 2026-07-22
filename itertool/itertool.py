#!/usr/bin/env python3
# -*- coding: utf8 -*-


from __future__ import annotations

from itertools import zip_longest
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

from asserttool import ic

signal(SIGPIPE, SIG_DFL)


def true_items_in_iterator(
    iterator,
    verbose: bool = False,
):
    if verbose:
        ic(iterator)
    answer = sum(x for x in iterator if x is True)
    return answer


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(
    iterable,
    n,
    fillvalue=None,
):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def compact(items):
    return [item for item in items if item]
