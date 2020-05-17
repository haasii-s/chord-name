"""
Mothball functions are no longer used but may be useful later
"""


"""
def tail_extension_converter(tail_extension):
    return tail_intervals().get(tail_extension)
"""

"""
def tail_interval_conversion_threshold(interval_strings):
    # print(interval_strings)

    interval_integer_list = []

    for i in interval_strings:
        if len(i) > 1:
            interval_integer_list.append(int(i[1:]))
        else:
            interval_integer_list.append(int(i))

    threshold_value = 0
    index_of_threshold = 0
    position_of_search_start = 0

    for i in interval_integer_list:
        if i < threshold_value:
            index_of_threshold = interval_integer_list.index(i, position_of_search_start)
            break
        else:
            threshold_value = i
            position_of_search_start += 1

    # print(interval_integer_list)
    # print(index_of_threshold)

    return index_of_threshold
"""

"""
<Part of semitones_to_strings>

if index_of_threshold == 0:
    interval_strings.insert(0, "R")
    return interval_strings
else:

    tail_intervals_to_convert = interval_strings[index_of_threshold:]
    interval_strings = interval_strings[:index_of_threshold]
    converted_tail_intervals = []

    for i in tail_intervals_to_convert:
        converted_tail_intervals.append(tail_extension_converter(i))

    interval_strings += converted_tail_intervals
    interval_strings.insert(0, "R")

    return interval_strings
"""