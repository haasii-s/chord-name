import itertools
from dictionaries import extensions


def extension_combo_gen(some_list):

    num_extension_voices = 12

    while num_extension_voices != 0:

        unjoined_combos = list(itertools.combinations(some_list, num_extension_voices))

        for combo in unjoined_combos:
            joined_combo = ''.join(combo)

            yield joined_combo

        num_extension_voices -= 1


def extension_combo_list():

    ecl = list(extension_combo_gen(extensions()))

    ##repeated extension altering Quality Order filter

    for single_joined_combo in ecl:
    
        print(single_joined_combo, file=open("ordered_extensions.txt", "a"))

    return ecl


