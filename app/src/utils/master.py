import bisect


def flat_roots():
    roots = [

        "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"

    ]
    return roots


def sharp_roots():
    roots = [

        "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"

    ]
    return roots


def scan_roots():
    roots = [

        "Ab", "A#", "Bb", "C#", "Db", "D#", "Eb", "Fb", "F#", "Gb", "G#",
        "A", "B", "C", "D", "E", "F", "G"

    ]
    return roots


def intervals():
    interval_semi_dict = {

        "b2": 1,
        "2": 2,
        "b3": 3,
        "3": 4,
        "4": 5,
        "b5": 6,
        "5": 7,
        "#5": 8,
        "6": 9,
        "b7": 10,
        "7": 11,
        "b9": 1,
        "#9": 3,
        "9": 2,
        "#11": 6,
        "11": 5,
        "b13": 8,
        "13": 9

    }
    return interval_semi_dict


def extensions():
    extension_dict = {

        "add9": 2,
        "add2": 2,
        "b5": 6,
        "#5": 8,
        "b9": 1,
        "#9": 3,
        "#11": 6,
        "b13": 8,

    }
    return extension_dict


def suspensions():
    suspension_dict = {

        "sus2": 2,
        "sus4": 5,

    }
    return suspension_dict


def quality_templates():
    """Dictionary of chord qualities. Order importance: preceding quality must not appear in following qualities"""

    quality_dict = {

        "maj13": ["3", "5", "7", "9", "11", "13"],
        "maj11": ["3", "5", "7", "9", "11"],
        "maj9": ["3", "5", "7", "9"],
        "maj6/9": ["3", "5", "6", "9"],
        "maj7": ["3", "5", "7"],
        "maj6": ["3", "5", "6"],
        "maj": ["3", "5"],

        "min7b5": ["b3", "b5", "b7"],
        "m7b5": ["b3", "b5", "b7"],

        "minMaj13": ["b3", "5", "7", "9", "11", "13"],
        "minMaj11": ["b3", "5", "7", "9", "11"],
        "minMaj9": ["b3", "5", "7", "9"],
        "minMaj7": ["b3", "5", "7"],

        "mM13": ["b3", "5", "7", "9", "11", "13"],
        "mM11": ["b3", "5", "7", "9", "11"],
        "mM9": ["b3", "5", "7", "9"],
        "mM7": ["b3", "5", "7"],

        "min13": ["b3", "5", "b7", "9", "11", "13"],
        "min11": ["b3", "5", "b7", "9", "11"],
        "min9": ["b3", "5", "b7", "9"],
        "min6/9": ["b3", "5", "6", "9"],
        "min7": ["b3", "5", "b7"],
        "min6": ["b3", "5", "6"],
        "min": ["b3", "5"],

        "dom13": ["3", "5", "b7", "9", "11", "13"],
        "dom11": ["3", "5", "b7", "9", "11"],
        "dom9": ["3", "5", "b7", "9"],
        "dom7": ["3", "5", "b7"],

        "dim13": ["b3", "b5", "6", "9", "11", "13"],
        "dim11": ["b3", "b5", "6", "9", "11"],
        "dim9": ["b3", "b5", "6", "9"],
        "dim7": ["b3", "b5", "6"],
        "dim": ["b3", "b5"],

        "aug13": ["3", "#5", "7", "9", "11", "13"],
        "aug11": ["3", "#5", "7", "9", "11"],
        "aug9": ["3", "#5", "7", "9"],
        "aug7": ["3", "#5", "7"],
        "aug": ["3", "#5"],

        "M13": ["3", "5", "7", "9", "11", "13"],
        "M11": ["3", "5", "7", "9", "11"],
        "M9": ["3", "5", "7", "9"],
        "M6/9": ["3", "5", "6", "9"],
        "M7": ["3", "5", "7"],
        "M6": ["3", "5", "6"],
        "M": ["3", "5"],

        "m13": ["b3", "5", "b7", "9", "11", "13"],
        "m11": ["b3", "5", "b7", "9", "11"],
        "m9": ["b3", "5", "b7", "9"],
        "m6/9": ["b3", "5", "6", "9"],
        "m7": ["b3", "5", "b7"],
        "m6": ["b3", "5", "6"],
        "m": ["b3", "5"],

        "13": ["3", "5", "b7", "9", "11", "13"],
        "11": ["3", "5", "b7", "9", "11"],
        "9": ["3", "5", "b7", "9"],
        "7": ["3", "5", "b7"],
        "5": ["5"],
        "": ["3", "5"]

    }
    return quality_dict


def user_input():
    """Receives input from user. Scans and filters to segment chord into root, quality, and extensions

    Args:
        No arguments

    Returns:
        Tuple of root, quality and extensions (string, string, string)

    """

    chord = input("Enter chord: ")

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

    print(root)

    quality = None

    for i in quality_templates():
        if i in chord and i == "":
            quality = i
            break

        elif i in chord and chord.index(i) == len(root):
            quality = i
            break

        else:
            quality = None
            # print(i)

    if quality is None:
        print("Chord quality not recognized")
        return None

    extension_beginning = len(root+quality)
    print(extension_beginning)

    remaining_extensions = chord[extension_beginning:]

    print(remaining_extensions)

    final_input = root, quality, remaining_extensions

    print(final_input)

    return final_input


def root_position_finder(root):
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
        print("found")
    else:
        root_position = flat_roots().index(root)

    # root_position = flat_roots().index(root)
    # print(root_position)
    return root_position


def quality_to_semitones(quality):
    """Assigns quality intervals to their semitone distances from root

    Args:
        quality: user input chord quality (string)

    Returns:
        list of semitones jumps (integers)

    """

    quality_intervals = quality_templates().get(quality)
    print(quality_intervals)

    quality_semitones = [intervals().get(i)
                         for i in quality_intervals if i in intervals()]
    print(quality_semitones)

    return quality_semitones


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


def extension_scanner(remaining_extensions, first_semitone_revision):
    """Scans remaining chord string for extensions and adds / replaces them in the final semitone list

    Args:
        remaining_extensions: a string of all unused elements of original user input (string)
        first_semitone_revision: a list of all required semitone jumps after the suspension scan (integers)

    Returns:
        final list of required quality semitone jumps (integers)

    """

    final_semitone_revision = first_semitone_revision

    if remaining_extensions == "":
        return final_semitone_revision

    for i in extensions():
        if i in remaining_extensions:
            semitone_to_replace = i[1]
            print(semitone_to_replace)

            try:
                first_semitone_revision.remove(
                    intervals().get(semitone_to_replace))
            except ValueError:
                continue
        else:
            continue

    extension_semitones = [extensions().get(i)
                           for i in extensions() if i in remaining_extensions]

    for i in extensions():
        if i in remaining_extensions:
            remaining_extensions = remaining_extensions.replace(i, "")

    if remaining_extensions != "":
        print("These chord extensions not recognized: " + remaining_extensions)
        return None

    elif remaining_extensions == "":
        for i in extension_semitones:
            # Change so insort is exclusive to b5 and #5
            bisect.insort(final_semitone_revision, i)

    # add code to remove repeated semitone jumps

    print(final_semitone_revision)
    print(extension_semitones)
    return final_semitone_revision


def semitones_to_indices(final_semitone_revision, root_position):
    """Actions the desired semitone jumps to find correct interval indices from chord root

    Args:
        final_semitone_revision: a list of the final revision of all required semitone jumps (integers)
        root_position: the index where the root note will be found

    Returns:
        list of indices where the final chord intervals will be found (integers)

    """

    interval_indices = [root_position + i for i in final_semitone_revision]
    print(interval_indices)

    for i in interval_indices:
        if i > 11:
            interval_indices[interval_indices.index(i)] = i - 12
        else:
            continue

    interval_indices.insert(0, root_position)

    return interval_indices


def final_converter(interval_indices, root):
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
    print(final_intervals)


def main():
    final_input = user_input()

    if final_input is None:
        return

    root, quality, remaining_extensions = final_input

    root_position = root_position_finder(root)

    quality_semitones = quality_to_semitones(quality)

    first_semitone_revision, remaining_extensions = suspension_scanner(
        remaining_extensions, quality_semitones)

    final_semitone_revision = extension_scanner(
        remaining_extensions, first_semitone_revision)

    if final_semitone_revision is None:
        return

    interval_indices = semitones_to_indices(
        final_semitone_revision, root_position)

    final_converter(interval_indices, root)

    print(remaining_extensions)


while True:

    if __name__ == "__main__":
        #
        # break

        main()
