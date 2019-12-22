
def transposer(amount):
    return (lambda tune: [None if x is None else x + amount for x in tune])

def one_note(tune):
    return [tune[0]] + [None] * (len(tune) - 1)

def repeat(tune):
    if len(tune) < 2: return tune
    if len(tune) % 2: return repeat(tune[:-1]) + tune[-1:]
    half = int(len(tune)/2)
    start = tune[:half]
    return start + start # or choice(all_transforms)(start)

def nudger(shift):
    return (lambda tune: tune[-shift:] + tune[:-shift])

def reverser(blocksize):
    return (lambda tune: [note
        for start in reversed(range(0, len(tune), blocksize))
        for note in tune[start:start+blocksize]])

# weight, min_tune_len, max_tune_len, transformation_function
all_transforms = [
        (None, None, transposer(5)),
        (None, None, transposer(-5)),
        (None, None, transposer(7)),
        (None, None, transposer(-7)),
        (None, None, transposer(2)),
        (None, None, transposer(-2)),
        (2, 16, repeat),
        (4, 24, repeat),
        (8, 32, repeat),
        (2, 4, one_note),
        (2, 8, one_note),
        (2, 12, one_note),
        (2, 16, one_note),
        (4, 16, reverser(2)),
        (8, 32, reverser(4)),
        (16, 128, reverser(8)),
        (32, None, reverser(16)),
        (2, 4, nudger(1)),
        (2, 6, nudger(1)),
        (4, 8, nudger(2)),
        (4, 12, nudger(2)),
        (8, 24, nudger(4)),
    ]

