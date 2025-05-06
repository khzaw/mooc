# pyright: basic

null = frozenset()


def lit(x):
    # return ("lit", string)
    return lambda text: set([text[len(x) :]]) if text.startswith(x) else null


def seq(x, y):
    return lambda text: set().union(*map(y, x(text)))


def alt(x, y):
    return lambda text: x(text) | y(text)


def star(x):
    return lambda t: (
        set([t]) | set(t2 for t1 in x(t) if t1 != t for t2 in star(x)(t1))
    )


def plus(x):
    # return ("plus", x)
    return seq(x, star(x))


def opt(x):
    # return ("opt", x)
    return alt(lit(""), x)


def oneof(chars):
    # return ("oneof", tuple(chars))
    return lambda t: set([t[1:]]) if (t and t[0] in chars) else null


# dot = ("dot",)
# eol = ("eol",)

dot = lambda t: set([t[1:]]) if t else null
eol = lambda t: set([""]) if t == "" else null


def search(pattern, text):
    """Match patterns anywhere in text, return longest earliest match or None"""
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m


def match(pattern, text):
    """Match pattern against start of text; return longest match found or None."""
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[: len(text) - len(shortest)]


def components(pattern):
    """Return the op, x, and y arguments; x and y are None if missing."""
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y


# def matchset(pattern, text: str):
#     """match pattern at start of text; return a set of remainders of text."""
#     op, x, y = components(pattern)
#     if op == "lit":
#         return set([text[len(x) :]]) if text.startswith(x) else null
#     elif op == "seq":
#         return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
#     elif op == "alt":
#         return matchset(x, text) | matchset(y, text)
#     elif op == "dot":
#         return set([text[1:]]) if text else null
#     elif op == "oneof":
#         return set([text[1:]]) if text.startswith(x) else null
#     elif op == "eol":
#         return set([""]) if text == "" else null
#     elif op == "star":
#         return set([text]) | set(
#             t2 for t1 in matchset(x, text) for t2 in matchset(pattern, t1) if t1 != text
#         )
#     else:
#         raise ValueError("unknown pattern: %s" % pattern)


def test_search():
    a, b, c = lit("a"), lit("b"), lit("c")
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar = star(dot)
    assert search(lit("def"), "abcdefgh") == "def"
    assert search(seq(lit("def"), eol), "abcdef") == "def"
    assert search(seq(lit("def"), eol), "abcdefg") == None
    assert search(a, "not the start") == "a"
    assert match(a, "not the start") == None
    assert match(abcstars, "aaabbbccccccccccdef") == "aaabbbcccccccccc"
    assert match(abcstars, "junk") == ""
    assert all(
        match(seq(abcstars, eol), s) == s for s in "abc aaabbccc aaaabcccc".split()
    )
    return "test_search passes"
