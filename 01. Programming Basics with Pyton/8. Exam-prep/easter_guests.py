import math

guests_count = int(input())
budged = int(input())

easter_bread_price = 4
egg_price = 0.45
eggs_per_person = 2

easter_bread_total = 0
easter_bread_price_total = 0
egg_total = 0
egg_price_total = 0
total_price = 0
left_money = 0
needed_money = 0

for i in range(1, guests_count + 1):
    easter_bread_total = guests_count / 3
    easter_bread_price_total = (math.ceil(easter_bread_total) * easter_bread_price)
    break

for i in range(1, guests_count + 1):
    egg_total = guests_count * 2
    egg_price_total = egg_total * egg_price
    break

total_price = easter_bread_price_total + egg_price_total

if total_price <= budged:
    left_money = budged - total_price
    print(f"Lyubo bought {math.ceil(easter_bread_total)} Easter bread and {egg_total} eggs.\nHe has {left_money:.2f} lv. left.")
else:
    needed_money = total_price - budged
    print(f"Lyubo doesn't have enough money.\nHe needs {needed_money:.2f} lv. more.")



