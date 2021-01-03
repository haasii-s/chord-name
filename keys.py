def key_correction(key_root, key_formula):
    unique_roots = ["A", "B", "C", "D", "E", "F", "G"]
    unique_roots_dict = {"A": 2, "B": 2, "C": 1, "D": 2, "E": 2, "F": 1, "G": 2}

    if len(key_root) == 1 and key_root in unique_roots:
        pass

    elif len(key_root) == 1 and key_root not in unique_roots:
        print("key_correction")
        print("unrecognized root")
        return

    elif len(set(key_root[1:])) != 1:
        print("key_correction")
        print("unrecognized accidental")
        return

    for accidental in key_root[1:]:
        if accidental == "#" or "b":
            pass

        else:
            print("key_correction")
            print("unrecognized accidentals")
            return

    if key_root[0] not in unique_roots:
        print("key_correction")
        print("key root not recognised")
        return

    root_order_index = unique_roots.index(key_root[0])

    ordered_roots = unique_roots[root_order_index:] + unique_roots[:root_order_index]
    ordered_roots = [key_root] + ordered_roots[1:]

    corrected_roots = [key_root]

    for i, note in enumerate(ordered_roots[1:]):
        print(ordered_roots)
        print(note_fundamental_value(corrected_roots[i]))
        note_distance = unique_roots_dict[note] - note_fundamental_value(corrected_roots[i])
        required_note_distance = key_formula[i] - note_distance
        if required_note_distance == 0:
            print("==0")
            corrected_roots.append(note)

        elif required_note_distance > 0:
            print(">0")
            corrected_roots.append(note + required_note_distance*"#")

        elif required_note_distance < 0:
            print("<0")
            corrected_roots.append(note + -1*required_note_distance*"b")
        print("end")
        print(corrected_roots)


def note_fundamental_value(note):

    key_root_fundamental_value = 0

    for accidental in note:
        if accidental == "#":
            key_root_fundamental_value += 1
        elif accidental == "b":
            key_root_fundamental_value -= 1

    return key_root_fundamental_value









