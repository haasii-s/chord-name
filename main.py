"""
Used for cProfile time testing
"""
from retrievers import get_chord_web, get_chord_in_line


def main():

    # Test all proper combinations
    chords = open("database.txt", "r")
    for line in chords:
        converted_list = eval(line)
        for name in converted_list[0]:
            full_chord = "C#" + name
            print(full_chord)
            print(get_chord_web(full_chord))

    """Test in line input
    print(get_chord_in_line())
    """


if __name__ == "__main__":

    main()

    """# Test loop for in line inputs (add while True de-indented prior
    try:
        main()
    except TypeError:
        print("chord not recognized")
    """

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