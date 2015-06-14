import random


def shuffle1(deck):
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)

def shuffle(deck):
    "Knuth's algorithm P"
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i, N))

def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]
