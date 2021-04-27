# 1. Read input data
age = int(input())
washing_mashin_price = float(input())
single_toy_price = int(input())

toys_count = 0
savings = 0
money_to_receive = 0
for year in range (1, age + 1):
    if year % 2 == 1:
        toys_count += 1
    else:
        money_to_receive += 10
        savings += money_to_receive
        savings -= 1
# 3. Sell toys -> add to savings
total_sum_sold_toys = toys_count * single_toy_price
savings += total_sum_sold_toys
# 4. Check if savings are enough
if savings >= washing_mashin_price:
    print(f"Yes! {savings - washing_mashin_price:.2f}")
else:
    print(f"No! {washing_mashin_price - savings:.2f}")