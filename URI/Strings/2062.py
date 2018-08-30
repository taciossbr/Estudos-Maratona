def correct(word):
    if len(word) == 3 and word[:2] in ['OB', 'UR']:
        return word[:2]+'I'
    return word


input()

words = []
for word in input().split():
    words.append(correct(word))

print(" ".join(words))
