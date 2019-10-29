
notes = ["D", "^D", "E", "=F", "F", "G", "^G", "A", "^A", "B", "c", "^c",
        "d", "^d", "e", "=f", "f", "g", "^g", "a", "^a", "b", "c'", "^c'"]

def is_bar(note): return note in '|\n'

def interpret_note(note):
    if note is None: return ('z', 1)
    return (notes[note + 12], 1)

def reconcile_halves(start, end):
    pitch, length = end[0]
    if pitch != 'z': return start + end
    lastpitch, oldlength = start[-1]
    if is_bar(lastpitch): return start + end
    return start[:-1] + [(lastpitch, oldlength + length)] + end[1:]

def maybe_bar(tune):
    if len(tune) == 8: return [('|', 0)]
    if len(tune) == 32: return [('\n', 0)]
    return []

def interpret_tune(tune):
    if not tune: return []
    if len(tune) == 1: return [interpret_note(tune[0])]
    half = int(len(tune)/2)
    start = interpret_tune(tune[:half])
    end = interpret_tune(tune[half:])
    return reconcile_halves(start, end) + maybe_bar(tune)

def render_note(pitch, length):
    if is_bar(pitch) or length == 1: return pitch
    return pitch + str(length)

def render_tune(tune):
    return ' '.join(render_note(pitch, length)
            for pitch, length in interpret_tune(tune))

