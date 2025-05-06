# pyright: basic
import itertools, re, string


def compile_formula(formula, verbose=False):
    """Compile formula into a function.
    Also return letters found, as a str,
    in same order as params of function.
    The first digit of a multi-digit number can't be 0.
    So if YOU is a word in the formula, and the function is called with Y equal to 0, the function should return False."""

    letters = "".join(set(re.findall("[A-Z]", formula)))
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z]+)", formula))
    body = "".join(tokens)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile"""
