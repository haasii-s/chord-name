"""
Used for cProfile time testing
"""
from post_logic import chord_organiser
from retrievers import get_chord_web, get_chord_in_line
from scanners import semitones_to_keyboard_inputs


def main():

    # Test all proper combinations
    """
    chords = open("database.txt", "r")
    for line in chords:
        converted_list = eval(line)
        for name in converted_list[0]:
            full_chord = "C#" + name + "/F/D/A/B"
            print(full_chord)
            print(get_chord_web(full_chord))
    """
    # Test in line input
    # print(get_chord_in_line())

    # Test semitones to keys mapping
    # print(semitones_to_keyboard_inputs("C#", [4, 5, 6, 10, 13, 14, 20, 21]))

    full_chord = input("Enter chord: ")
    print(get_chord_web(full_chord))

    post_logic_chord = chord_organiser(full_chord)
    print(post_logic_chord)

    """
    full_chord = "C#" + name
    print(full_chord)
    print(get_chord_web(full_chord))
    """
    """Test in line input
    print(get_chord_in_line())
    """


if __name__ == "__main__":

    #main()

    """# Test loop for in line inputs (add while True de-indented prior
    try:
        main()
    except TypeError:
        print("Chord quality not recognized")
    """

    #main()

    # Test loop for in line inputs (add while True de-indented prior
    try:
        main()
    except TypeError:
        print("chord not recognized")

    """
    import cProfile
    cProfile.run("main()", "output.dat")

    import pstats
    from pstats import SortKey

    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()

    with open("output_calls.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()


    """