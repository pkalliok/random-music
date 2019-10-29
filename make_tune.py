
import render, generate, sys

def make_tune(initial):
    print('X:1\nM:8/16\nK:D')
    print(render.render_tune(generate.extend(3, 8, initial)))

def read_melody(argv):
    def maybe_int(x):
        try: return int(x)
        except ValueError: return None
    return [maybe_int(x) for x in argv]

if __name__ == '__main__':
    make_tune(read_melody(sys.argv[1:]))

