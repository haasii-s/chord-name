"""
def func_1(list_1):
    list_1.append("D")
    return list_1


list_1 = ["A", "B", "C"]
print(list_1)

list_2 = func_1(list_1)

print(list_2)
print(list_1)
"""

"""
def polychord_filter(user_input):
    polychord_found = False

    if "|" in user_input:
        polychord_found = True
        chords_found = [chord for chord in user_input.split("|")]
        return chords_found, polychord_found

    else:
        return user_input, polychord_found


print(polychord_filter("Amaj9|Dmin7|F"))
"""
