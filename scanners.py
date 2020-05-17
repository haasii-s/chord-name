"""
Scanner functions alter the input given to them and return the altered inputs based on logic and dictionaries
"""
from converters import quality_to_semitones, interval_to_int
from dictionaries import extensions, keyboard_roots, scan_roots
from filters import quality_semitone_strings_filter, keyboard_note_filter, slash_keyboard_note_filter, \
    slash_chord_filter



def suspension_scanner(remaining_extensions, quality_semitones):
    """Searches remaining extensions for chord suspensions and inserts them into the semitone jumps list.
    Also removes the b3 (3) or 3 (4) semitone indices if present.

    Args:
        remaining_extensions: concatenated extension component of original user input (string)
        quality_semitones:

    Returns:
        Tuple of revised list of required quality semitone jumps and adjusted remaining extensions (integers, string)

    """

    if 3 in quality_semitones:
        interval_to_replace = 3
        replacement_index = 0
    elif 4 in quality_semitones:
        interval_to_replace = 4
        replacement_index = 0
    else:
        return quality_semitones, remaining_extensions

    if "sus2sus4" in remaining_extensions:
        quality_semitones.remove(interval_to_replace)
        quality_semitones.insert(replacement_index, 5)
        quality_semitones.insert(replacement_index, 2)
        remaining_extensions = remaining_extensions.replace("sus2sus4", "")

    elif "sus4sus2" in remaining_extensions:
        return quality_semitones, remaining_extensions

    elif "sus2" in remaining_extensions:
        quality_semitones.remove(interval_to_replace)
        quality_semitones.insert(replacement_index, 2)
        remaining_extensions = remaining_extensions.replace("sus2", "")

    elif "sus4" in remaining_extensions:
        quality_semitones.remove(interval_to_replace)
        quality_semitones.insert(replacement_index, 5)
        remaining_extensions = remaining_extensions.replace("sus4", "")

    else:
        return quality_semitones, remaining_extensions

    return quality_semitones, remaining_extensions


def extension_scanner(remaining_extensions, first_semitone_revision, quality, multi_scan=True):
    """Scans remaining chord string for extensions and adds / replaces them in the final semitone list

    Args:
        remaining_extensions: a string of all unused elements of original user input (string)
        first_semitone_revision: a list of all required semitone jumps after the suspension scan (integers)
        quality: user input chord quality (string)
        multi_scan:

    Returns:
        final list of required quality semitone jumps (integers)


    """
    quality_semitones = quality_to_semitones(quality)
    final_semitone_revision = first_semitone_revision

    if remaining_extensions == "":
        return final_semitone_revision

    extension_semitones = [extensions().get(i) for i in extensions() if i in remaining_extensions]

    for i in extensions():
        if i in remaining_extensions:
            remaining_extensions = remaining_extensions.replace(i, "")

    tail_extensions = []

    if remaining_extensions != "":
        print("These chord extensions not recognized: " + remaining_extensions)
        return None

    elif remaining_extensions == "":
        for i in extension_semitones:
            tail_extensions.append(i)

    tail_extensions.sort()

    final_semitone_revision += tail_extensions

    final_semitone_revision.sort()

    if multi_scan is False:
        final_semitone_revision = list(dict.fromkeys(final_semitone_revision))

        return final_semitone_revision

    elif multi_scan is True:
        if len(list(dict.fromkeys(final_semitone_revision))) != len(final_semitone_revision):
            return None

        else:
            return final_semitone_revision


def remove_element_by_index_scan(semitones, indices_to_remove):

    for i in sorted(indices_to_remove, reverse=True):
        del semitones[i]

    return semitones


def post_fifth_scan():
    return


def extension_replacement_scan(list_of_interval_strings, chord):

    quality_semitone_strings = quality_semitone_strings_filter(chord)

    indices_to_check_adjacent_intervals = []
    indices_to_remove_from_semitones = []

    for i in quality_semitone_strings:
        if i in list_of_interval_strings:
            indices_to_check_adjacent_intervals.append(list_of_interval_strings.index(i))

    for i in sorted(indices_to_check_adjacent_intervals, reverse=True):

        if len(indices_to_check_adjacent_intervals) > 1:
            backward_check_index = i - 1
            forward_check_index = i + 1
        else:
            return list_of_interval_strings, indices_to_remove_from_semitones

        reference_check_value = interval_to_int(list_of_interval_strings[i])

        reference_check_string = list_of_interval_strings[i]

        if i == 0:
            forward_check_value = interval_to_int(list_of_interval_strings[forward_check_index])
            if forward_check_value == reference_check_value:
                list_of_interval_strings.remove(reference_check_string)
                indices_to_remove_from_semitones.append(i)

        elif i == len(list_of_interval_strings)-1:
            backward_check_value = interval_to_int(list_of_interval_strings[backward_check_index])
            if backward_check_value == reference_check_value:
                list_of_interval_strings.remove(reference_check_string)
                indices_to_remove_from_semitones.append(i)

        else:
            backward_check_value = interval_to_int(list_of_interval_strings[backward_check_index])
            forward_check_value = interval_to_int(list_of_interval_strings[forward_check_index])

            if forward_check_value == reference_check_value or backward_check_value == reference_check_value:
                list_of_interval_strings.remove(reference_check_string)
                indices_to_remove_from_semitones.append(i)
            else:
                pass

    return list_of_interval_strings, indices_to_remove_from_semitones


def no3_scanner(semitone_jumps, interval_strings):

    indices_of_interval_strings_to_replace = []

    index_correction_value = 0

    if 3 in semitone_jumps:
        indices_of_interval_strings_to_replace.append(semitone_jumps.index(3))
        semitone_jumps.remove(3)
        index_correction_value += 1

    if 4 in semitone_jumps:
        indices_of_interval_strings_to_replace.append(semitone_jumps.index(4)+index_correction_value)
        semitone_jumps.remove(4)
        index_correction_value += 1

    if 15 in semitone_jumps:
        indices_of_interval_strings_to_replace.append(semitone_jumps.index(15)+index_correction_value)
        semitone_jumps.remove(15)
        index_correction_value += 1

    if 16 in semitone_jumps:
        indices_of_interval_strings_to_replace.append(semitone_jumps.index(16)+index_correction_value)
        semitone_jumps.remove(16)
        index_correction_value += 1

    for i in sorted(indices_of_interval_strings_to_replace, reverse=True):
        del interval_strings[i]

    return semitone_jumps, interval_strings

def semitones_to_keyboard_inputs(root, semitone_jumps):

    default_keyboard_values = []
    keyboard_start_value = keyboard_note_filter(root)

    for i in semitone_jumps:
        next_default_keyboard_value = i + keyboard_start_value
        default_keyboard_values.append(next_default_keyboard_value)

    default_keyboard_values.insert(0, keyboard_start_value)

    return default_keyboard_values


def slash_chord_scanner(slash_content, interval_notes, interval_strings, default_keyboard_values):

    slash_content = slash_content[0].upper() + slash_content[1:]

    chord, multi_slash_content, multi_slash_found = slash_chord_filter(slash_content)

    if multi_slash_found:
        # potential method instead - accounts for '/' removed from multi_slash_content
        first_slash_end_index = len(slash_content) - (len(multi_slash_content) + 1)
        slash_content = slash_content[:first_slash_end_index]
        slash_chord_scanner(multi_slash_content, interval_notes, interval_strings, default_keyboard_values)

    if slash_content in scan_roots():

        interval_notes.insert(0, slash_content)
        interval_strings.insert(0, "/"+slash_content)
        slash_keyboard_value = slash_keyboard_note_filter(default_keyboard_values, slash_content)
        default_keyboard_values.insert(0, slash_keyboard_value)

        return interval_notes, interval_strings, default_keyboard_values

    else:
        return interval_notes, interval_strings, default_keyboard_values


def slash_chord_recursion_scanner(interval_notes, scan_interval_notes, scan_interval_strings, scan_keyboard_values):

    number_of_recursions = len(scan_interval_notes) - len(interval_notes)
    slash_note_elements = scan_interval_notes[:number_of_recursions]
    slash_note_elements.reverse()
    final_interval_notes = slash_note_elements + scan_interval_notes[number_of_recursions:]

    slash_string_elements = scan_interval_strings[:number_of_recursions]
    slash_string_elements.reverse()
    final_interval_strings = slash_string_elements + scan_interval_strings[number_of_recursions:]

    slash_keyboard_elements = scan_keyboard_values[:number_of_recursions]
    corrected_keyboard_values = scan_keyboard_values[number_of_recursions:]
    for i in slash_keyboard_elements:
        print(i)
        corrected_keyboard_note = \
            slash_keyboard_note_filter(corrected_keyboard_values, slash_keyboard_value=i, recursion=True)
        corrected_keyboard_values.insert(0, corrected_keyboard_note)
    final_keyboard_values = corrected_keyboard_values

    return final_interval_notes, final_interval_strings, final_keyboard_values
