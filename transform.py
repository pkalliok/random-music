
from random import choice

def transposer(amount):
    return (lambda tune: [None if x is None else x + amount for x in tune])

def one_note(tune):
    if len(tune) < 1: return tune
    return [tune[0]] + [None] * (len(tune) - 1)

def repeat(tune):
    if len(tune) < 2: return tune
    half = int(len(tune)/2)
    start = tune[:half]
    return start + choice(all_transforms)(start)

def nudger(shift):
    return (lambda tune: tune[shift:] + tune[:shift])

def reverser(blocksize):
    return (lambda tune: [note
        for start in reversed(range(0, len(tune), blocksize))
        for note in tune[start:start+blocksize]])

all_transforms = [transposer(5), transposer(-5), transposer(7), transposer(-7),
    transposer(2), transposer(-2), repeat, repeat, repeat, one_note, one_note,
    reverser(2), reverser(4), reverser(8), reverser(16),
    nudger(1), nudger(2), nudger(4)]

