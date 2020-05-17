"""
Contains user input function for testing in python
"""
from dictionaries import scan_roots
from filters import quality_filter, remaining_extension_filter, root_filter


def user_input():
    """Receives input from user. Scans and filters to segment chord into root, quality, and extensions

    Args:
        No arguments

    Returns:
        Tuple of root, quality and extensions (string, string, string)

    """

    chord = input("Enter chord: ")

    chord = chord[0].upper() + chord[1:]

    root = root_filter(chord)

    quality = quality_filter(chord, root)

    remaining_extensions = remaining_extension_filter(chord, quality, root)

    final_input = root, quality, remaining_extensions

    return final_input
