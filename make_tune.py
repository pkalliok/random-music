
import render, generate

def make_tune():
    print('X:1\nM:8/8\nK:D')
    print(render.render_tune(generate.extend(3, 7, [0, None])))

if __name__ == '__main__':
    make_tune()

