import re
import math

regex = r"(#|\|)([a-z(?<!\s)A-Z]+)\1((\d{2})\/(\d{2})\/(\d{2}))\1(\d+)\1"

data = input()

all_cal = 0
items_list = []

match = re.findall(regex, data)

for m in match:
    food = m[1]
    best_before = m[2]
    cal = int(m[6])

    all_cal += cal

    items_list.append(f"Item: {food}, Best before: {best_before}, Nutrition: {cal}")

print(f"You have food to last you for: {math.floor(all_cal / 2000)} days!")

for i in items_list:
    print(i)