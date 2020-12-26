"""
Converter functions convert the type of input into another type of output based on dictionary mappings
"""
from dictionaries import intervals, flat_roots, sharp_roots, quality_templates, reverse_notes, reverse_intervals, \
    scales, double_sharps, fb_bb_roots, double_flats, sharps_and_flats


def semitones_to_strings(final_semitone_revision, multi=True):
    interval_strings = []

    list_of_interval_jumps = [intervals().get(i) for i in intervals().keys()]
    list_of_interval_strings = [i for i in intervals().keys()]

    for i in final_semitone_revision:
        if i in list_of_interval_jumps:
            index_interval_string_found = list_of_interval_jumps.index(i)
            interval_strings.append(list_of_interval_strings[index_interval_string_found])

    if multi is False:
        interval_strings.insert(0, "R")
        return interval_strings
    elif multi is True:
        return interval_strings


def semitones_to_indices(final_semitone_revision, root_position):
    """Actions the desired semitone jumps to find correct interval indices from chord root

    Args:
        final_semitone_revision: a list of the final revision of all required semitone jumps (integers)
        root_position: the index where the root note will be found

    Returns:
        list of indices where the final chord intervals will be found (integers)

    """

    interval_indices = [root_position + i for i in final_semitone_revision]

    for i in interval_indices:
        if i > 23:
            interval_indices[interval_indices.index(i)] = i - 24
        elif i > 11:
            interval_indices[interval_indices.index(i)] = i - 12
        else:
            continue

    interval_indices.insert(0, root_position)

    return interval_indices


def indices_to_notes(interval_indices, root=None):
    """Uses interval indices to search appropriate scale dictionary for corresponding note string

    Args:
        interval_indices: list of indices where the final interval notes will be found
        root: root: root note of the chord (string)

    Returns:
        list of the final notes corresponding to the initial user input (strings)

    """

    if "b" in root:
        root_scale = flat_roots()
    elif "#" in root:
        root_scale = sharp_roots()
    else:
        root_scale = flat_roots()

    final_intervals = [root_scale[i] for i in interval_indices]

    return final_intervals


def interval_to_int(single_interval_string):

    if single_interval_string[0] == "#" or single_interval_string[0] == "b":
        interval_int = int(single_interval_string[1:])
        return interval_int
    else:
        return int(single_interval_string)


def quality_to_semitones(quality):
    """Assigns quality intervals to their semitone distances from root

    Args:
        quality: user input chord quality (string)

    Returns:
        list of semitones jumps (integers)

    """

    quality_intervals = quality_templates().get(quality)
    # print(quality_intervals)

    quality_semitones = [intervals().get(i) for i in quality_intervals if i in intervals()]
    # print(quality_semitones)

    return quality_semitones


def notes_to_semitones(string_of_notes):

    list_of_notes = string_of_notes.split()
    capital_notes = [note.capitalize() for note in list_of_notes]
    root = capital_notes[0]

    list_of_note_values = []

    for note in capital_notes:
        if note in reverse_notes():
            list_of_note_values.append(reverse_notes().get(note))

    root_reference_value = list_of_note_values[0]
    corrected_values =\
        [j + 12 if j < root_reference_value else j for i, j in zip(list_of_note_values[:-1], list_of_note_values[1:])]

    corrected_values.insert(0, root_reference_value)

    normalized_values = [j + 12 if j < i else j for i, j in zip(corrected_values[:-1], corrected_values[1:])]
    semitones = [i - root_reference_value for i in normalized_values]
    semitones.sort()

    semitones = list(dict.fromkeys(semitones))

    # print(list_of_note_values)
    # print(corrected_values)
    # print(semitones)

    return root, semitones


def semitones_to_intervals(semitones):

    interval_from_semitones = [reverse_intervals().get(i) for i in semitones if i in reverse_intervals()]
    return interval_from_semitones

"""
def scales_to_notes(scale, key):

    scale_formula = scales().get(scale)

    if key == "Fb" or key == "Cb":
        roots = fb_bb_roots()

    elif "b" in key:
        roots = flat_roots()
    else:
        roots = sharp_roots()

    if key in roots:
        reference_index = roots.index(key)
    else:
        return None

    scale_notes = []

    for step in scale_formula:
        reference_index += step

        if reference_index > 11:
            reference_index -= 12

        scale_notes.append(roots[reference_index])

    scale_notes.insert(0, key)

    corrected_notes = scale_notes

    print(corrected_notes)

    correction_runs = 3

    while correction_runs != 0:

        if roots == sharp_roots():
            corrected_notes = \
                [j if len(j) == 1 else
                 double_sharps().get(j)
                 if j[0] == i[0] else j
                 for j, i in zip(corrected_notes[:-1], corrected_notes[1:])]

            print(corrected_notes)

            corrected_notes.append(key)
            correction_runs -= 1

        else:
            j = corrected_notes[-1:0:-1]
            i = corrected_notes[-2::-1]

            corrected_notes = \
                [double_flats().get(j)
                 if j[0] == i[0] else j
                 for j, i in zip(corrected_notes[-1:0:-1], corrected_notes[-2::-1])]

            corrected_notes.append(key)
            corrected_notes.reverse()
            correction_runs -= 1

    return corrected_notes

"""


def scales_to_notes2(scale, key, preference=False):

    scale_formula = scales().get(scale)

    flats = flat_roots()
    sharps = sharp_roots()
    theoretical = fb_bb_roots()

    if key in flats and key in sharps:
        flat_reference_index = flats.index(key)
        sharp_reference_index = sharps.index(key)

        flat_notes = reference_to_notes(scale_formula, flat_reference_index, flats)
        sharp_notes = reference_to_notes(scale_formula, sharp_reference_index, sharps)

        print(flat_notes, sharp_notes)

    elif key in flats and key not in sharps:

        sharp_equivalent_key = sharps_and_flats().get(key)

        flat_reference_index = flats.index(key)
        sharp_reference_index = sharps.index(sharp_equivalent_key)

        flat_notes = reference_to_notes(scale_formula, flat_reference_index, flats)
        sharp_notes = reference_to_notes(scale_formula, sharp_reference_index, sharps)

        print(flat_notes, sharp_notes)

    elif key in sharps and key not in flats:

        flat_equivalent_key = sharps_and_flats().get(key)

        flat_reference_index = flats.index(flat_equivalent_key)
        sharp_reference_index = sharps.index(key)

        flat_notes = reference_to_notes(scale_formula, flat_reference_index, flats)
        sharp_notes = reference_to_notes(scale_formula, sharp_reference_index, sharps)

        print(flat_notes, sharp_notes)

    elif key in theoretical:
        theoretical_reference_index = theoretical.index(key)

        theoretical_reference_index = reference_to_notes(scale_formula, theoretical_reference_index, theoretical)

        print(theoretical_reference_index)


def reference_to_notes(scale_formula, reference_index, roots):
    scale_notes = []

    for step in scale_formula:
        reference_index += step

        if reference_index > 11:
            reference_index -= 12

        scale_notes.append(roots[reference_index])

    return scale_notes


def notes_to_unique_notes(key, scale_notes):

    flat = False
    sharp = False

    scale_notes.insert(0, key)

    for note in scale_notes:
        if "#" in note:
            sharp = True
        elif "b" in note:
            flat = True

    print(flat)
    print(sharp)
    print(scale_notes)

    correction_runs = 3

    corrected_notes = []

    while correction_runs != 0:

        if sharp:
            j = scale_notes[-1:0:-1]
            i = scale_notes[-2::-1]

            print(j, "j")
            print(i, "i")

            corrected_notes = \
                [double_flats().get(j)
                 if j[0] == i[0] else j
                 for j, i in zip(scale_notes[-1:0:-1], scale_notes[-2::-1])]

            print(corrected_notes)

            corrected_notes.append(key)
            correction_runs -= 1

        elif flat:
            j = scale_notes[-1:0:-1]
            i = scale_notes[-2::-1]

            corrected_notes = \
                [double_flats().get(j)
                 if j[0] == i[0] else j
                 for j, i in zip(scale_notes[-1:0:-1], scale_notes[-2::-1])]

            corrected_notes.append(key)
            corrected_notes.reverse()
            correction_runs -= 1

    return corrected_notes


"""key = input("Enter key: ")
print(scales_to_notes2("Minor", key))"""

"""
print(notes_to_unique_notes('C', ['D', 'D#', 'F', 'G', 'G#', 'A#', 'C']))
"""