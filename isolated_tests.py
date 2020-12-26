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

"""
def func2():
    l1 = [1,2,3,3,2,4]

    test = list(dict.fromkeys(l1))

    l3 = []
    for i in test:
        l3.append(i)
"""
"""
wissy = []

randomGameChars = []

Object[] sortedChars = new Object[gameCharCount]

for (int i = 0; i < gameCharCount; i++){
    for (int j = 0; j < gameCharCount; j++){
        if(wissy[i] == randomGameChars[j].wisdom){
            sortedChars[i] = randomGameChars[j].wisdom
        }
    }
}
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

user_input = thisdict.get("brand")

for chord in user_input:
    print("found")
