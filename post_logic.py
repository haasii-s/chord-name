from retrievers import get_chord_web


def initial_polychord_test(chord_string, polychord_detected=False):

    if '|' in chord_string:
        polychord_detected = True

    return polychord_detected


def chord_organiser(user_input, chord=None):

    chords = []

    for input_chord in user_input:
        polychord = initial_polychord_test(input_chord)
        output = get_chord_web(input_chord)
        #print(output)
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
            }

            chords.append(chord_dict)

    return chords

