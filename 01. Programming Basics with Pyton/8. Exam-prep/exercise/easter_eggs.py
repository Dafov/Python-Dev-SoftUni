import sys
num_eggs = int(input())
type_of_egg = input()

count_red_eggs = 0
count_orange_eggs = 0
count_blue_eggs = 0
count_green_eggs = 0
all_eggs = 0
colour = ""

while all_eggs <= num_eggs:
    if type_of_egg == "red":
        count_red_eggs += 1
        all_eggs += 1
        if all_eggs == num_eggs:
            break
        type_of_egg = input()
    elif type_of_egg == "orange":
        count_orange_eggs += 1
        all_eggs += 1
        if all_eggs == num_eggs:
            break
        type_of_egg = input()

    elif type_of_egg == "blue":
        count_blue_eggs += 1
        all_eggs += 1
        if all_eggs == num_eggs:
            break
        type_of_egg = input()

    elif type_of_egg == "green":
        count_green_eggs += 1
        all_eggs += 1
        if all_eggs == num_eggs:
            break
        type_of_egg = input()


count_maximum_eggs = -sys.maxsize

if count_red_eggs > count_maximum_eggs:
    count_maximum_eggs = count_red_eggs
    colour = "red"
elif count_orange_eggs > count_red_eggs:
    count_maximum_eggs = count_orange_eggs
    colour = "orange"
elif count_blue_eggs > count_orange_eggs:
    count_maximum_eggs = count_blue_eggs
    colour = "blue"
elif count_green_eggs > count_blue_eggs:
    count_maximum_eggs = count_green_eggs
    colour = "green"

print(f"Red eggs: {count_red_eggs}")
print(f"Orange eggs: {count_orange_eggs}")
print(f"Blue eggs: {count_blue_eggs}")
print(f"Green eggs: {count_green_eggs}")
print(f"Max eggs: {count_maximum_eggs} -> {colour}")
