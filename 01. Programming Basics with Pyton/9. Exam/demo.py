food_in_kg = int(input())
command = input()

we_have_enough_food = True
food_total_in_gr = food_in_kg * 1000
eaten_food_total = 0

while command != "Adopted":
    food_for_current_day = int(command)
    eaten_food_total += food_for_current_day
    if food_total_in_gr < eaten_food_total:
        we_have_enough_food = False
    command = input()

if we_have_enough_food:
    print(f"Food is enough! Leftovers: {abs(food_total_in_gr - eaten_food_total)} grams.")
else:
    print(f"Food is not enough. You need {abs(food_total_in_gr - eaten_food_total)} grams more.")