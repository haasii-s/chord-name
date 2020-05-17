"""
Converter functions convert the type of input into another type of output based on dictionary mappings
"""
from dictionaries import intervals, flat_roots, sharp_roots, quality_templates


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
