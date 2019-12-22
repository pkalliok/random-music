
from random import choice, randint
from transform import all_transforms

def maybe(n): return 1 == randint(1, n)

def pick_transform(transforms, blocklength):
    possible = [transform
            for min_len, max_len, transform in transforms
            if min_len is None or min_len <= blocklength
            if max_len is None or max_len >= blocklength]
    return choice(possible)

def generate_range(chaos, start, end):
    if end - start <= 1 or maybe(chaos): return (start, end)
    middle = int((start+end)/2)
    if maybe(2): return generate_range(chaos, start, middle)
    return generate_range(chaos, middle, end)

def apply_random_transform(chaos, tune):
    start, end = generate_range(chaos, 0, len(tune))
    transform = pick_transform(all_transforms, end - start)
    return tune[:start] + transform(tune[start:end]) + tune[end:]

def transform(selection_chaos, iteration_chaos, tune):
    if maybe(iteration_chaos):
        return apply_random_transform(selection_chaos, tune)
    transformed = transform(selection_chaos, iteration_chaos, tune)
    return apply_random_transform(selection_chaos, transformed)

def extend(selection_chaos, iteration_chaos, times, tune):
    if times == 0: return tune
    return extend(selection_chaos, iteration_chaos, times - 1,
            tune + transform(selection_chaos, iteration_chaos, tune))

