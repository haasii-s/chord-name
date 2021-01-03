def scales():
    s = {
        "Major": [2, 2, 1, 2, 2, 2, 1],
        "Minor": [2, 1, 2, 2, 1, 2, 2]
    }
    return s


def modes():
    m = {
        "Ionian": [2, 2, 1, 2, 2, 2, 1],
        "Dorian": [2, 1, 2, 2, 2, 1, 2],
        "Phrygian": [1, 2, 2, 2, 1, 2, 2],
        "Lydian": [2, 2, 2, 1, 2, 2, 1],
        "Mixolydian": [2, 2, 1, 2, 2, 1, 2],
        "Aeolian": [2, 1, 2, 2, 1, 2, 2],
        "Locrian": [1, 2, 2, 1, 2, 2, 2]
    }
    return m


def reverse_intervals():
    ri = {

        1: 'b2',
        2: '2',
        3: 'b3',
        4: '3',
        5: '4',
        6: 'b5',
        7: '5',
        8: '#5',
        9: '6',
        10: 'b7',
        11: '7',
        13: 'b9',
        14: '9',
        15: '#9',
        17: '11',
        18: '#11',
        20: 'b13',
        21: '13'
    }
    return ri


def reverse_notes():
    rr = {
        'C': 0,
        'C#': 1,
        'Db': 1,
        'D': 2,
        'D#': 3,
        'Eb': 3,
        'E': 4,
        'F': 5,
        'F#': 6,
        'Gb': 6,
        'G': 7,
        'G#': 8,
        'Ab': 8,
        'A': 9,
        'A#': 10,
        'Bb': 10,
        'B': 11
    }
    return rr


def keyboard_roots():
    kr = {
        'C': 51,
        'C#': 52,
        'Db': 52,
        'D': 53,
        'D#': 54,
        'Eb': 54,
        'E': 55,
        'F': 56,
        'F#': 57,
        'Gb': 57,
        'G': 58,
        'G#': 59,
        'Ab': 59,
        'A': 60,
        'A#': 61,
        'Bb': 61,
        'B': 62
    }
    return kr


def doubled_potential_quality_orders():
    qo = [
        '13',
        '11',
        '9',
        '6'
    ]
    return qo


def flat_roots():
    roots = [

        'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'

    ]
    return roots


def fb_bb_roots():
    roots = [
        'A', 'Bb', 'Cb', 'C', 'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'Ab'
    ]
    return roots


def sharp_roots():
    roots = [

        'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'

    ]
    return roots


def double_flats():
    df = {
        "A": "B♭♭",
        "B": "Cb",
        "C": "D♭♭",
        "D": "E♭♭",
        "E": "Fb",
        "F": "G♭♭",
        "G": "A♭♭"
    }
    return df


def double_sharps():
    ds = {
        "A": "G𝄪",
        "B": "A𝄪",
        "C": "B#",
        "D": "C𝄪",
        "E": "D𝄪",
        "F": "E#",
        "G": "F𝄪"
    }
    return ds


def sharps_and_flats():
    sf = {
        "A#": "Bb",
        "C#": "Db",
        "D#": "Eb",
        "F#": "Gb",
        "G#": "Ab",
        "Bb": "A#",
        "Db": "C#",
        "Eb": "D#",
        "Gb": "F#",
        "Ab": "G#"
    }
    return sf


def scan_roots():
    roots = [

        'Ab', 'A#', 'Bb', 'C#', 'Db', 'D#', 'Eb', 'Fb', 'F#', 'Gb', 'G#',
        'A', 'B', 'C', 'D', 'E', 'F', 'G'

    ]
    return roots


def intervals():
    interval_semi_dict = {

        'b2': 1,
        '2': 2,
        'b3': 3,
        '3': 4,
        '4': 5,
        'b5': 6,
        '5': 7,
        '#5': 8,
        '6': 9,
        'b7': 10,
        '7': 11,
        'b9': 13,
        '#9': 15,
        '9': 14,
        '#11': 18,
        '11': 17,
        'b13': 20,
        '13': 21

    }
    return interval_semi_dict


def tail_intervals():
    tail_intervals_dict = {

        'b2': 'b9',
        '2': '9',
        'b3': '#9',
        '4': '11',
        'b5': '#11',
        '#5': 'b13',
        '6': '13',

        'b9': 'b2',
        '9': '2',
        '#9': 'b3',
        '11': '4',
        '#11': 'b5',
        'b13': '#5',
        '13': '6'

    }
    return tail_intervals_dict


def extensions():
    extension_dict = {

        'add2': 2,
        'add4': 5,
        'add6': 9,
        'add9': 14,
        'add11': 17,
        'add13': 21,
        'b5': 6,
        '#5': 8,
        'b9': 13,
        '#9': 15,
        '#11': 18,
        'b13': 20,

    }
    return extension_dict


def suspension_strings():
    suspension_strings_dict = [

        'sus2sus4',
        'sus2',
        'sus4',

    ]
    return suspension_strings_dict


def suspensions():
    suspension_dict = {

        'sus2': 2,
        'sus4': 5,

    }
    return suspension_dict


def reverse_qualities():
    rq = {
        ['b3', '5', '7', '9', '11', '13']: 'minMaj13',
        ['b3', '5', '7', '9', '11']: 'minMaj11',
        ['b3', '5', '7', '9']: 'minMaj9',
        ['b3', '5', '7']: 'minMaj7',

        ['3', '5', '7', '9', '11', '13']: 'maj13',
        ['3', '5', '7', '9', '11']: 'maj11',
        ['3', '5', '7', '9']: 'maj9',
        ['3', '5', '6', '9']: 'maj6/9',
        ['3', '5', '7']: 'maj7',
        ['3', '5', '6']: 'maj6',
        ['3', '5']: '',

        ['b3', '5', 'b7', '9', '11', '13']: 'min13',
        ['b3', '5', 'b7', '9', '11']: 'min11',
        ['b3', '5', 'b7', '9']: 'min9',
        ['b3', '5', '6', '9']: 'min6/9',
        ['b3', '5', 'b7']: 'min7',
        ['b3', '5', '6']: 'min6',
        ['b3', '5']: 'min',

        ['3', '5', 'b7', '9', '11', '13']: '13',
        ['3', '5', 'b7', '9', '11']: '11',
        ['3', '5', 'b7', '9']: '9',
        ['3', '5', 'b7']: '7',
        ['5']: '5',

        ['b3', 'b5', '6', '9', '11']: 'dim11',
        ['b3', 'b5', '6', '9']: 'dim9',
        ['b3', 'b5', '6']: 'dim7',
        ['b3', 'b5']: 'dim',

        ['3', '#5', 'b7', '9', '11', '13']: 'aug13',
        ['3', '#5', 'b7', '9', '11']: 'aug11',
        ['3', '#5', 'b7', '9']: 'aug9',
        ['3', '#5', 'b7']: 'aug7',
        ['3', '#5']: 'aug',

        ['b3', 'b5', 'b7', '9', '11', '13']: 'ø13',
        ['b3', 'b5', 'b7', '9', '11']: 'ø11',
        ['b3', 'b5', 'b7', '9']: 'ø9',
        ['b3', 'b5', 'b7']: 'ø7'

    }
    return rq


def quality_templates():
    # Dictionary of chord qualities. Order importance: preceding quality must not appear in following qualities'

    quality_dict = {

        'minMaj13': ['b3', '5', '7', '9', '11', '13'],
        'minMaj11': ['b3', '5', '7', '9', '11'],
        'minMaj9': ['b3', '5', '7', '9'],
        'minMaj7': ['b3', '5', '7'],

        'maj13': ['3', '5', '7', '9', '11', '13'],
        'maj11': ['3', '5', '7', '9', '11'],
        'maj9': ['3', '5', '7', '9'],
        'maj6/9': ['3', '5', '6', '9'],
        'maj7': ['3', '5', '7'],
        'maj6': ['3', '5', '6'],
        'maj': ['3', '5'],

        'Maj13': ['3', '5', '7', '9', '11', '13'],
        'Maj11': ['3', '5', '7', '9', '11'],
        'Maj9': ['3', '5', '7', '9'],
        'Maj6/9': ['3', '5', '6', '9'],
        'Maj7': ['3', '5', '7'],
        'Maj6': ['3', '5', '6'],
        'Maj': ['3', '5'],

        'min7b5': ['b3', 'b5', 'b7'],
        'm7b5': ['b3', 'b5', 'b7'],

        'mM13': ['b3', '5', '7', '9', '11', '13'],
        'mM11': ['b3', '5', '7', '9', '11'],
        'mM9': ['b3', '5', '7', '9'],
        'mM7': ['b3', '5', '7'],

        'min13': ['b3', '5', 'b7', '9', '11', '13'],
        'min11': ['b3', '5', 'b7', '9', '11'],
        'min9': ['b3', '5', 'b7', '9'],
        'min6/9': ['b3', '5', '6', '9'],
        'min7': ['b3', '5', 'b7'],
        'min6': ['b3', '5', '6'],
        'min': ['b3', '5'],

        'dom13': ['3', '5', 'b7', '9', '11', '13'],
        'dom11': ['3', '5', 'b7', '9', '11'],
        'dom9': ['3', '5', 'b7', '9'],
        'dom7': ['3', '5', 'b7'],

        'dim13': ['b3', 'b5', '6', '9', '11', '13'],
        'dim11': ['b3', 'b5', '6', '9', '11'],
        'dim9': ['b3', 'b5', '6', '9'],
        'dim7': ['b3', 'b5', '6'],
        'dim': ['b3', 'b5'],

        'aug13': ['3', '#5', 'b7', '9', '11', '13'],
        'aug11': ['3', '#5', 'b7', '9', '11'],
        'aug9': ['3', '#5', 'b7', '9'],
        'aug7': ['3', '#5', 'b7'],
        'aug': ['3', '#5'],

        'M13': ['3', '5', '7', '9', '11', '13'],
        'M11': ['3', '5', '7', '9', '11'],
        'M9': ['3', '5', '7', '9'],
        'M6/9': ['3', '5', '6', '9'],
        'M7': ['3', '5', '7'],
        'M6': ['3', '5', '6'],
        'M': ['3', '5'],

        'm13': ['b3', '5', 'b7', '9', '11', '13'],
        'm11': ['b3', '5', 'b7', '9', '11'],
        'm9': ['b3', '5', 'b7', '9'],
        'm6/9': ['b3', '5', '6', '9'],
        'm7': ['b3', '5', 'b7'],
        'm6': ['b3', '5', '6'],
        'm': ['b3', '5'],

        '13': ['3', '5', 'b7', '9', '11', '13'],
        '11': ['3', '5', 'b7', '9', '11'],
        '9': ['3', '5', 'b7', '9'],
        '7': ['3', '5', 'b7'],
        '5': ['5'],
        '': ['3', '5']

    }
    return quality_dict


# user_input

# quality_filter

# remaining_extension_filter

# root_position_filter

# quality_to_semitones

# suspension_scanner

# extension_scanner

# tail_extension_converter(mothball)

# semitones_to_strings

# semitones_to_indices

# get_chord_in_line

# get_chord_single

# get_chord_multiple

# remove_element_by_index_scan

# repeated_interval_filter

# post_fifth_scan

# quality_semitones_filter

# quality_semitone_strings_filter

# interval_to_int


# print(interval_to_int('#3'))

# print(extension_replacement(['3', '4', '5', '#5', 'b7', '9', '13'], 'dom7add4add9add13#5'))

# print(remove_element_by_index([1, 4, 7, 11, 3], [2, 3]))

# print(get_quality_semitone_strings('M11#5b9'))

# get_chord_multiple()

# print(get_chord())

# print(repeated_interval_filter([1, 2, 5, 7, 11 , 13]))

index = [1, 2, 3]

index_even = index
