from freq_note_converter import converter_code

__str__ = ''
__repr__ = ''
values = dict(freq=0,
              note_number=0,
              note='',
              octave=0,
              offset_from_note=0)


# def convert(freq=None, note_number=None, note=None, octave=None):
def convert(freq=None, note_number=None):
    if freq is not None:
        freq = freq
        note, octave, offset_from_note, note_number = converter_code.freq_to_note(freq)
    # elif note is not None and octave is not None:
    #     print('not implemented')
    elif note_number is not None:
        note_number = note_number
        note, octave, freq = converter_code.note_number_to_freq(note_number)
        offset_from_note = 0
    else:
        print('no valid input')
    values['freq'] = freq
    values['note_number'] = note_number
    values['note'] = note
    values['octave'] = octave
    values['offset_from_note'] = offset_from_note
    update_str()
    return values


def update_str():
    global __str__, __repr__
    __str__ = "\n".join(["{: >16} : {}".format(k, v) for k, v in values.items()])
    __str__ += '\n' + '-' * 50 + '\n'
    __repr__ = __str__


def print_me():
    print(__str__, end='')
