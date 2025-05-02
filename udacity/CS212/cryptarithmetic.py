# pyright: basic
import itertools
import re


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula: str):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = "".join(x for x in filter(lambda x: "A" <= x <= "Z", formula))
    for digits in itertools.permutations("1234567890", len(letters)):
        table = str.maketrans(letters, "".join(digits))
        yield formula.translate(table)


def valid(f) -> bool:
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true"""
    try:
        return not re.search(r"\b0[0-9]", f) and eval(f) is True
    except ArithmeticError:
        return False


def compile_word(word: str) -> str:
    """Compile a word of uppercase letters as numeric digits.
    e.g., compile_word('YOU') => '(1*U+10*0+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [("%s*%s" % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return f"({'+'.join(terms)})"
    else:
        return word


def faster_solve(formula: str) -> str | None:
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the forumla; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, "".join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as params of function. For example, 'YOU == ME**2' returns
    (lambda Y, M, E, U, O: (U+10*0+100*Y) == (E+10*M)**2), 'YMEUO'"""
    letters = "".join(set(x for x in filter(lambda x: "A" <= x <= "Z", formula)))
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z]+)", formula))
    body = "".join(tokens)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
X / X == X
A**N + B**N == C**N and N > 1
""".splitlines()

for e in examples:
    print(solve(e))
