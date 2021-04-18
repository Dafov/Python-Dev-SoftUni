# 1. Read input data
camaign_duration_in_days = int(input())
bakers_count = int(input())
cakes_count = int(input())
corrugations_count = int(input())
pankakes_count = int(input())

# 2. Calculate cake price
cake_price = 45
all_cakes = cakes_count * cake_price

# 3. Calculate cake corrugations price
corrugations_price = 5.80
all_corrugations = corrugations_count * corrugations_price

# 4. Calculate cake pancakes price
pankakes_price = 3.20
all_pankakes = pankakes_count * pankakes_price
# 5. Calculate cake bakers productivity/ money for one day
bakers_productivity = (all_cakes + all_corrugations + all_pankakes) * bakers_count
daily_profit = bakers_productivity

# 6. Calculate all  money raised
money_raised = daily_profit * camaign_duration_in_days

# 7. Calculate campaign money raised
money_for_campaign = money_raised - (money_raised / 8)

# 8. Print and format
print(f'{money_for_campaign:.2f}')