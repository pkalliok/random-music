
def transposer(amount):
    return (lambda tune: [None if x is None else x + amount for x in tune])

all_transforms = [transposer(5), transposer(-5), transposer(7), transposer(-7)]

