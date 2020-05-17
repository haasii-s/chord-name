"""
Retriever functions utilise all other functions to return final outputs
"""
from converters import quality_to_semitones, semitones_to_indices, indices_to_notes, semitones_to_strings
from filters import root_position_filter, quality_filter, remaining_extension_filter, repeated_interval_filter, \
    root_filter, no3_filter, space_bracket_comma_filter, slash_chord_filter
from in_line_input import user_input
from scanners import suspension_scanner, extension_scanner, extension_replacement_scan, remove_element_by_index_scan, \
    no3_scanner, semitones_to_keyboard_inputs, slash_chord_scanner, slash_chord_recursion_scanner


def get_chord_in_line():
    final_input = user_input()

    if final_input is None:
        return

    root, quality, remaining_extensions = final_input

    root_position = root_position_filter(root)

    quality_semitones = quality_to_semitones(quality)

    first_semitone_revision, remaining_extensions = suspension_scanner(
        remaining_extensions, quality_semitones)

    final_semitone_revision = extension_scanner(
        remaining_extensions, first_semitone_revision, quality)

    if final_semitone_revision is None:
        return

    interval_indices = semitones_to_indices(
        final_semitone_revision, root_position)

    final_intervals = indices_to_notes(interval_indices, root)

    semitone_strings = semitones_to_strings(final_semitone_revision, False)

    print(final_intervals, " ", semitone_strings)


def get_chord_web(chord):

    chord = space_bracket_comma_filter(chord)

    chord = chord[0].upper() + chord[1:]

    chord, no3_flag = no3_filter(chord)

    chord, slash_content, slash_found = slash_chord_filter(chord)

    root, rootless_chord = root_filter(chord, True)

    quality = quality_filter(chord, root)

    root_position = root_position_filter(root)

    output_template = get_chord_single(rootless_chord, quality)

    try:
        all_extensions, semitone_jumps, interval_strings = output_template
    except TypeError:
        return

    if no3_flag:
        semitone_jumps, interval_strings = no3_scanner(
            semitone_jumps, interval_strings)
    else:
        pass

    default_keyboard_values = semitones_to_keyboard_inputs(root, semitone_jumps)

    interval_strings.insert(0, "R")

    interval_indices = semitones_to_indices(semitone_jumps, root_position)

    interval_notes = indices_to_notes(interval_indices, root)

    if slash_found is True:
        scan_interval_notes, scan_interval_strings, scan_keyboard_values = \
            slash_chord_scanner(slash_content, list(interval_notes), interval_strings, default_keyboard_values)

        return slash_chord_recursion_scanner(interval_notes, scan_interval_notes,
                                             scan_interval_strings, scan_keyboard_values)

    else:
        final_object_template = interval_notes, interval_strings, default_keyboard_values

    return final_object_template


def get_chord_single(chord, quality):

    remaining_extensions = remaining_extension_filter(chord, quality)

    quality_semitones = quality_to_semitones(quality)

    first_semitone_revision, remaining_extensions = suspension_scanner(
        remaining_extensions, quality_semitones)

    final_semitone_revision = extension_scanner(
        remaining_extensions, first_semitone_revision, quality)

    if final_semitone_revision is None:
        pass

    elif repeated_interval_filter(final_semitone_revision) is not True:

        final_semitone_strings, semitone_indices_to_replace = \
            extension_replacement_scan(
                semitones_to_strings(final_semitone_revision), chord)

        final_semitone_revision = remove_element_by_index_scan(
            final_semitone_revision, semitone_indices_to_replace)

        return chord, final_semitone_revision, final_semitone_strings


def get_chord_single_offline(chord):

    quality = quality_filter(chord)

    remaining_extensions = remaining_extension_filter(chord, quality)

    quality_semitones = quality_to_semitones(quality)

    first_semitone_revision, remaining_extensions = suspension_scanner(
        remaining_extensions, quality_semitones)

    final_semitone_revision = extension_scanner(
        remaining_extensions, first_semitone_revision, quality)

    if final_semitone_revision is None:
        pass

    elif repeated_interval_filter(final_semitone_revision) is not True:

        final_semitone_strings, semitone_indices_to_replace = \
            extension_replacement_scan(
                semitones_to_strings(final_semitone_revision), chord)

        final_semitone_revision = remove_element_by_index_scan(
            final_semitone_revision, semitone_indices_to_replace)

        return chord, final_semitone_revision, final_semitone_strings


def get_chord_multiple():
    chord_inputs = open("COMBINED_PRE_QUALS.txt", "r")

    for i in chord_inputs:

        stripped_chord = i.replace("\n", "")

        quality = quality_filter(stripped_chord)

        remaining_extensions = remaining_extension_filter(
            stripped_chord, quality)

        quality_semitones = quality_to_semitones(quality)

        first_semitone_revision, remaining_extensions = suspension_scanner(
            remaining_extensions, quality_semitones)

        final_semitone_revision = extension_scanner(
            remaining_extensions, first_semitone_revision, quality)

        final_output_template = []

        if final_semitone_revision is None:
            pass

        elif repeated_interval_filter(final_semitone_revision) is not True:

            final_semitone_strings, semitone_indices_to_replace = \
                extension_replacement_scan(semitones_to_strings(
                    final_semitone_revision), stripped_chord)

            final_semitone_revision = remove_element_by_index_scan(
                final_semitone_revision, semitone_indices_to_replace)

            final_output_template.insert(0, final_semitone_strings)

            final_output_template.insert(0, final_semitone_revision)

            final_output_template.insert(0, [stripped_chord])

            print(final_output_template, file=open("database.txt", "a"))
