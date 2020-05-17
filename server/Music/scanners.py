"""
Scanner functions alter the input given to them and return the altered inputs based on logic and dictionaries
"""
from converters import quality_to_semitones, interval_to_int
from dictionaries import extensions
from filters import quality_semitone_strings_filter


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
