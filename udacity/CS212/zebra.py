"""
 Zebra Puzzle

1   There are five houses.
2   The Englishman lives in the red house.
3   The Spaniard owns the dog.
4   Coffee is drunk in the green house.
5   The Ukrainian drinks tea.
6   The green house is immediately to the right of the ivory house.
7   The Old Gold smoker owns snails.
8   Kools are smoked in the yellow house.
9   Milk is drunk in the middle house.
10  The Norwegian lives in the first house.
11  The man who smokes Chesterfields lives in the house next to the man with the fox.
12  Kools are smoked in a house next to the house where the horse is kept.
13  The Lucky Strike smoker drinks orange juice.
14  The Japanese smokes Parliaments.
15  The Norwegian lives next to the blue house.

Who drinks water? Who owns the zebra?
"""

# pyright: basic
from configparser import InterpolationMissingOptionError
import itertools
import time

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def imright(h1: int, h2: int) -> bool:
    "House h1 is immediately right of h2 if h1-h2 == 1"
    return h1 - h2 == 1


def nextto(h1: int, h2: int) -> bool:
    return abs(h1 - h2) == 1


def timedcall(fn, *args):
    t0 = time.clock_gettime(time.CLOCK_MONOTONIC)
    result = fn(*args)
    t1 = time.clock_gettime(time.CLOCK_MONOTONIC)
    return t1 - t0, result


def average(numbers):
    """Return the average (arithmetic mean) of a sequence of numbers."""
    return sum(numbers) / float(len(numbers))


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time."""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)


def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print(
        "%s got %s with %5d iters over %7d items"
        % (fn.__name__, result, c.starts, c.times)
    )


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i = 0
    while True:
        yield +i
        yield -i
        i = i + 1


def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the
    number of sequences started; c.items is numbers of items generated"""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
