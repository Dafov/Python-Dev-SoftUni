import re

regex = r"(=|(\/))([A-Z][a-z]{3,})\1"

data = input()
mirror_words = []

match = re.findall(regex, data)

for m in match:
    first_match = m[1]
    second_match = m[2]
    if first_match == second_match[::-1]:
        mirror_words.append(first_match + " <=> " + second_match)

if len(match) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(match)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
