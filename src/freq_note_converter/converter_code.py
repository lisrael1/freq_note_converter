import math


def note_number_to_note_octave(note_number):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note = (note_number - 1) % len(notes)
    note = notes[note]

    octave = (note_number + 8) // len(notes)

    return note, octave


def freq_to_note_number(freq):
    if not freq:  # no log value for 0
        freq += 1e-15
    # formula taken from https://en.wikipedia.org/wiki/Piano_key_frequencies
    note_number = 12 * math.log2(freq / 440) + 49
    error = note_number
    note_number = round(note_number)
    error -= note_number
    return note_number, error


def freq_to_note(freq):
    note_number, error = freq_to_note_number(freq)
    note, octave = note_number_to_note_octave(note_number)

    return note, octave, error, note_number


def note_number_to_freq(note_number):
    note, octave = note_number_to_note_octave(note_number)
    freq = 2 ** ((note_number - 49) / 12) * 440
    return note, octave, freq


