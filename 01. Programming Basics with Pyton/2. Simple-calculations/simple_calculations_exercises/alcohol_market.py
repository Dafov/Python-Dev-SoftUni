# 1. Read input data
whiskey_price = float(input())
beer_in_liters = float(input())
wine_in_liters = float(input())
rakia_in_liters = float(input())
whiskey_in_liters = float(input())

# 2. Calculate alcohol price
rakia_price_for_liter = whiskey_price / 2

wine_price_for_liter = rakia_price_for_liter * 0.60

beer_price_for_liter = rakia_price_for_liter * 0.20

money_for_whiskey = whiskey_price * whiskey_in_liters
money_for_wine = wine_price_for_liter * wine_in_liters
money_for_beer = beer_in_liters * beer_price_for_liter
money_for_rakia = rakia_in_liters * rakia_price_for_liter

# 3. Calculate needed money
needed_money = money_for_beer + money_for_rakia + money_for_whiskey + money_for_wine

# 4. Print and format
print(f'{needed_money:.2f}')
