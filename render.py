
notes = ["D", "^D", "E", "=F", "F", "G", "^G", "A", "^A", "B", "c", "^c",
        "d", "^d", "e", "=f", "f", "g", "^g", "a", "^a", "b", "c'", "^c'"]

def interpret_note(note):
    if note is None: return ('z', 1)
    return (notes[note + 12], 1)

def reconcile_halves(start, end):
    note, length = end[0]
    if note != 'z': return start + end
    lastnote, oldlength = start[-1]
    if lastnote == '|': return start + end
    return start[:-1] + [(lastnote, oldlength + length)] + end[1:]

def maybe_bar(tune):
    if len(tune) != 8: return []
    return [('|', 0)]

def interpret_tune(tune):
    if not tune: return []
    if len(tune) == 1: return [interpret_note(tune[0])]
    half = len(tune)/2
    start = interpret_tune(tune[:half])
    end = interpret_tune(tune[half:])
    return reconcile_halves(start, end) + maybe_bar(tune)

def render_note(pitch, length):
    if pitch == '|' or length == 1: return pitch
    return pitch + str(length)

def render_tune(tune):
    return ' '.join(render_note(pitch, length)
            for pitch, length in interpret_tune(tune))

