
def transposer(amount):
    return (lambda tune: [None if x is None else x + amount for x in tune])

def one_note(tune):
    return tune[0] + [None] * len(tune - 1)

all_transforms = [transposer(5), transposer(-5), transposer(7), transposer(-7),
        one_note]

