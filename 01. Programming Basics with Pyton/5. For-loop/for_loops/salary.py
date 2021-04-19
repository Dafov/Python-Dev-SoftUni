tabs = int(input())
salary = float(input())

for i in range(tabs):
    current_tap = input()

    if current_tap == "Facebook":
        salary -= 150
    elif current_tap == "Instagram":
        salary -= 100
    elif current_tap == "Reddit":
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")
