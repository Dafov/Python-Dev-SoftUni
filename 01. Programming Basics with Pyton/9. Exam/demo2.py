load_capacity = float(input())
command = input()
volume_total = 0
suitcase_counter = 0

while command != "End":
    volume = float(command)
    volume_total += volume

    if volume_total >= load_capacity:
        print("No more space!")
        break

    command = input()
    suitcase_counter += 1

if command == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_counter} suitcases loaded.")