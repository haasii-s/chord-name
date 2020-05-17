import dictionaries

import itertools

from filters import quality_filter


def there_is_quality_overlap(chord):

    quality_order_search_index = len(quality_filter(chord))

    for i in dictionaries.doubled_potential_quality_orders():
        if i in chord[:quality_order_search_index] and i in chord[quality_order_search_index:]:
            return True

    return False


def extension_combo_gen(some_list):
    num_extension_voices = 12

    while num_extension_voices != 0:

        unjoined_combos = list(itertools.combinations(some_list, num_extension_voices))

        for combo in unjoined_combos:
            joined_combo = ''.join(combo)

            yield joined_combo

        num_extension_voices -= 1


def extension_combo_list():
    ecl = list(extension_combo_gen(extensions_list()))

    for single_joined_combo in ecl:
        print(single_joined_combo, file=open("ordered_extensions.txt", "a"))

    return ecl


def to_string(some_list):
    string_output = ''.join(some_list)
    return string_output


def repeat_filter(chord):
    final_list = []
    for extension in chord:
        if extension not in final_list:
            final_list.append(extension)
        else:
            continue

    return final_list


def quality_templates_list():
    qtl = [q for q in dictionaries.quality_templates()]
    return qtl


def suspension_strings_list():
    ssl = [s for s in dictionaries.suspension_strings()]
    return ssl


def extensions_list():
    el = [e for e in dictionaries.extensions()]
    return el


def cartesian_product(list_of_lists):
    product = [to_string(repeat_filter(chord)) for chord in itertools.product(*list_of_lists)]
    return product


def quality_and_sus_list():

    initial_quality_and_sus_list = [quality_templates_list(), suspension_strings_list()]

    chord_list = cartesian_product(initial_quality_and_sus_list)

    final_quality_and_sus_list = []
    for i in chord_list:
        final_quality_and_sus_list.append(i)

    return final_quality_and_sus_list


def quality_and_extensions_list(extension_list):

    initial_quality_and_extensions_list = [quality_templates_list(), extension_list]

    chord_list = cartesian_product(initial_quality_and_extensions_list)

    total_loops = 0
    num_removed = 0
    for chord in chord_list:
        if there_is_quality_overlap(chord):
            chord_list.remove(chord)
            num_removed += 1
            total_loops += 1
            print(num_removed)
            print(chord, file=open("removed_chords2.txt", "a"))
        else:
            print(chord, file=open("QUAL_PASSED.txt", "a"))
            total_loops += 1
            pass

    print(total_loops)
    print(num_removed)


def quality_and_sus_and_extensions_list(extension_list):

    initial_quality_and_sus_and_extensions_list = [quality_and_sus_list(), extension_list]

    chord_list = cartesian_product(initial_quality_and_sus_and_extensions_list)

    total_loops = 0
    num_removed = 0
    for chord in chord_list:
        if there_is_quality_overlap(chord):
            chord_list.remove(chord)
            num_removed += 1
            total_loops += 1
            print(num_removed)
            print(chord, file=open("removed_chords_sus.txt", "a"))
        else:
            print(chord, file=open("QUAL_AND_SUS_PASSED.txt", "a"))
            total_loops += 1
            pass

    print(total_loops)
    print(num_removed)


def ultimate_list(extension_list):

    ul = quality_and_extensions_list(extension_list) + quality_and_sus_and_extensions_list(extension_list)

    return ul


#quality_and_sus_and_extensions_list(extension_combo_list())


"""
for quality_extension_combo in quality_and_extensions_list(extension_combo_list()):

    print(quality_extension_combo, file=open("quality_extension_combos.txt", "a"))
    print(quality_extension_combo)

for quality_and_sus_and_extension_combo in quality_and_sus_and_extensions_list(extension_combo_list()):

    print(quality_and_sus_and_extension_combo, file=open("quality_and_sus_and_extension_combos.txt", "a"))
    print(quality_and_sus_and_extension_combo)
"""


