food_in_kg = int(input())
command = input()

food_in_gr = food_in_kg * 1000
all_food_consumed = 0
we_have_food = True

while command != "Adopted":
    food_consumed = int(command)
    all_food_consumed += food_consumed
    if all_food_consumed < food_in_gr:
        we_have_food = False
        command = input()

if command == "Adopted":
    left_food = food_in_gr - all_food_consumed
    print(f"Food is enough! Leftovers: {left_food} grams.")

elif all_food_consumed > food_in_gr:
    needed_food = abs(food_in_gr - all_food_consumed)
    print(f"Food is not enough. You need {needed_food} grams more.")

