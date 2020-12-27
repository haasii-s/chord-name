from retrievers import get_chord_web
from filters import space_bracket_comma_filter


def initial_polychord_test(chord_string, polychord_detected=False):

    if '|' in chord_string:
        polychord_detected = True

    return polychord_detected


def poly_and_slash_capitalization_filter(input_chord):
    input_chord = space_bracket_comma_filter(input_chord)
    input_chord = input_chord[0].upper() + input_chord[1:]
    capital_indicators = "|/"
    for i, char in enumerate(input_chord):
        if char in capital_indicators:
            input_chord = input_chord[:i+1] + input_chord[i+1].upper() + input_chord[i+2:]

    return input_chord


def chord_organiser(user_input, chord=None):

    chords = []

    for input_chord in user_input:
        polychord = initial_polychord_test(input_chord)
        output = get_chord_web(input_chord)
        corrected_input = poly_and_slash_capitalization_filter(input_chord)

        if polychord:
            polychords = []
            for tup in output:
                root, interval_notes, interval_strings, keyboard_values = tup

                chord = {
                    "root": root,
                    "notes": interval_notes,
                    "strings": interval_strings,
                    "keyboard_values": keyboard_values,
                }

                polychords.append(chord)

            chord_dict = {
                "polychord" : polychord,
                "chords" : polychords,
                "original_input": corrected_input
            }

            chords.append(chord_dict)

        elif not polychord:
            for tup in output:
                root, interval_notes, interval_strings, keyboard_values = tup

                chord = {
                    "root": root,
                    "notes": interval_notes,
                    "strings": interval_strings,
                    "keyboard_values": keyboard_values,
                }

            chord_dict = {
                "polychord" : polychord,
                "chords" : [chord],
                "original_input": corrected_input
            }

            chords.append(chord_dict)

    return chords

