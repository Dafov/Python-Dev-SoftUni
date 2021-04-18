budged = float(input())
people = int(input())
price_of_clothes_per_person = float(input())

decor_price = budged / 10

price_of_all_clothes = price_of_clothes_per_person * people

if people > 150:
    price_of_all_clothes *= 0.9

total_price = decor_price + price_of_all_clothes
left_money = abs(total_price - budged)

if total_price > budged:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")