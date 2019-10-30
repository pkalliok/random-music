
import render, generate, sys

def meter(beats):
    if beats > 4: return beats
    return meter(2*beats)

def make_tune(initial):
    print('X:1\nM:%d/16\nK:D' % meter(len(initial)))
    print(render.render_tune(generate.extend(5, 9, initial)))

def read_melody(argv):
    def maybe_int(x):
        try: return int(x)
        except ValueError: return None
    return [maybe_int(x) for x in argv]

if __name__ == '__main__':
    make_tune(read_melody(sys.argv[1:]))

