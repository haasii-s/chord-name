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


def available_keyboard_values(original_keyboard_values):

    lower_values = []
    higher_values = []
    lower_bound = 0
    upper_bound = 87

    for value in original_keyboard_values:
        low_value = value
        while low_value >= lower_bound + 12:
            low_value -= 12
            lower_values.append(low_value)

    for value in original_keyboard_values:
        high_value = value
        while high_value <= upper_bound - 12:
            high_value += 12
            higher_values.append(high_value)

    available_values = lower_values + original_keyboard_values + higher_values
    available_values.sort()

    return available_values


def chord_organiser(user_input, chord=None):

    chords = []

    for input_chord in user_input:
        polychord = initial_polychord_test(input_chord)
        output = get_chord_web(input_chord)
        corrected_input = poly_and_slash_capitalization_filter(input_chord)

        if polychord:
            polychords = []
            available_values = []
            for tup in output:
                root, interval_notes, interval_strings, keyboard_values = tup

                available_values += available_keyboard_values(keyboard_values)
                available_values.sort()

                chord = {
                    "root": root,
                    "notes": interval_notes,
                    "strings": interval_strings,
                    "keyboard_values": keyboard_values
                }

                polychords.append(chord)

            available_values = list(dict.fromkeys(available_values))

            chord_dict = {
                "polychord" : polychord,
                "chords" : polychords,
                "original_input": corrected_input,
                "available_values": available_values
            }

            chords.append(chord_dict)

        elif not polychord:
            available_values = []
            for tup in output:
                root, interval_notes, interval_strings, keyboard_values = tup

                available_values = list(dict.fromkeys(available_keyboard_values(keyboard_values)))

                chord = {
                    "root": root,
                    "notes": interval_notes,
                    "strings": interval_strings,
                    "keyboard_values": keyboard_values
                }

            chord_dict = {
                "polychord" : polychord,
                "chords" : [chord],
                "original_input": corrected_input,
                "available_values": available_values
            }

            chords.append(chord_dict)

    return chords

