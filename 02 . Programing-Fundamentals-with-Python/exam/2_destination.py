import re

regex = r"(/|=)([A-Za-z]{2,})\1"

data = input()
matched_destination = []
match = re.findall(regex, data)

for m in match:
    second_match = m[1]

    matched_destination.append(second_match)

print(f"Destinations: {', '.join(matched_destination)}")
print(f"Travel Points: {len(''.join(matched_destination))}")
