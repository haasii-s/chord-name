"""
Filter functions pick out single elements from their inputs and return them
"""
from converters import quality_to_semitones, semitones_to_strings
from dictionaries import quality_templates, flat_roots, sharp_roots, scan_roots, keyboard_roots

def root_filter(chord, web=False):

    if len(chord) > 1:
        flats_sharps_scan = chord[0] + chord[1]
        natural_scan = chord[0]
    elif len(chord) == 1:
        flats_sharps_scan = "none"
        natural_scan = chord[0]
    else:
        print("No chord entered")
        return

    if flats_sharps_scan in scan_roots():
        root = chord[0] + chord[1]
    elif natural_scan in scan_roots():
        root = chord[0]
    else:
        print("Chord root not recognized")
        return

    if web:
        root_end_index = len(root)
        rootless_chord = chord[root_end_index:]
        return root, rootless_chord
    else:
        return root


def quality_filter(chord, root=None):

    quality = None

    for i in quality_templates():

        if i in chord and i == "":
            quality = i
            return quality

        elif i in chord and root is not None and chord.index(i) == len(root):
            quality = i
            return quality

        elif i in chord and root is None and chord.index(i) == 0:
            quality = i
            return quality

        else:
            quality = None

    if quality is None:
        print("Chord quality not recognized")
        return None


def remaining_extension_filter(chord, quality, root=None):

    extension_beginning = 0

    if root is not None:
        extension_beginning = len(root + quality)
    elif quality != "" and root is None:
        extension_beginning = len(quality)
    elif quality == "" and root is None:
        extension_beginning = 0

    remaining_extensions = chord[extension_beginning:]

    return remaining_extensions


def root_position_filter(root):
    """Actions the desired semitone jumps to find correct interval indices from chord root

    Args:
        root: root note of the chord (string)

    Returns:
        index where the root note will be found (integer)

    """

    if "b" in root:
        root_position = flat_roots().index(root)
    elif "#" in root:
        root_position = sharp_roots().index(root)
    else:
        root_position = flat_roots().index(root)

    return root_position


def repeated_interval_filter(semitone_list):

    octave_down_comparison_list = []
    for i in semitone_list:
        octave_shifted_down = i - 12
        octave_down_comparison_list.append(octave_shifted_down)

    for i in octave_down_comparison_list:
        if i in semitone_list:
            return True

        else:
            pass

    return False


def quality_semitones_filter(chord):

    quality = quality_filter(chord)
    quality_semitones = quality_to_semitones(quality)

    return quality_semitones


def quality_semitone_strings_filter(chord):

    quality_semitones = quality_semitones_filter(chord)
    semitone_strings = semitones_to_strings(quality_semitones)

    return semitone_strings


def no3_filter(chord):
    if "no3" in chord:
        chord = chord.replace("no3", "")
        return chord, True
    else:
        return chord, False


def space_bracket_comma_filter(chord):
    unacceptable = " (),"

    for i in unacceptable:
        if i in chord:
            chord = chord.replace(i, "")
    return chord


def slash_chord_filter(chord):

    if "/" in chord:
        slash_index = chord.index("/")
        primary_chord = chord[:slash_index]

        slash_content_index = slash_index + 1
        slash_content = chord[slash_content_index:]

        slash_found = True
        return primary_chord, slash_content, slash_found
    else:
        slash_content = None
        slash_found = False
        return chord, slash_content, slash_found


def keyboard_note_filter(root):

    keyboard_start_value = 51

    for i in keyboard_roots():
        if i == root:
            keyboard_start_value = keyboard_roots().get(i)

    return keyboard_start_value


def slash_keyboard_note_filter(default_keyboard_values, slash_content=None, recursion=False, slash_keyboard_value=0):

    if recursion is False:

        slash_keyboard_value = keyboard_note_filter(slash_content)

        while slash_keyboard_value > default_keyboard_values[0]:
            slash_keyboard_value -= 12

    else:
        default_reference_value = default_keyboard_values[0]
        while (slash_keyboard_value + 12) < default_reference_value:
            slash_keyboard_value += 12

        while slash_keyboard_value > default_reference_value:
            slash_keyboard_value -= 12

    return slash_keyboard_value


def polychord_filter(user_input):

    polychord_found = False

    if "|" in user_input:
        polychord_found = True
        chords_found = [chord for chord in user_input.split("|")]
        return chords_found, polychord_found

    else:
        return user_input, polychord_found


def scale_reference_scanner(scale_formula, reference_index, roots):
    scale_notes = []

    for step in scale_formula:
        reference_index += step

        if reference_index > 11:
            reference_index -= 12

        scale_notes.append(roots[reference_index])

    return scale_notes
