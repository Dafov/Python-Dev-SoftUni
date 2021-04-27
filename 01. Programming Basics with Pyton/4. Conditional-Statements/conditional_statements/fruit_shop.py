fruit = input()
day_of_week = input()
quantity = float(input())

price = 0
if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday":
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.20
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
else:
    print("unknown")