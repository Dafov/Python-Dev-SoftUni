# 1. Read input data
table_count = int(input())
table_length_in_m = float(input())
table_width_in_m = float(input())

# 2. Calculate tablecloth area in sq.m
table_cloth = table_count
table_cloth_area = table_cloth * (table_length_in_m + 2 * 0.30) * (table_width_in_m + 2 * 0.30)

# 3. Calculate table_cover area in sq.m
table_cover = table_count
table_cover_area = table_cover * (table_length_in_m / 2) * (table_length_in_m / 2)

# 4. Calculate price in USD
price_in_usd = table_cloth_area * 7 + table_cover_area * 9

# 5. Calculate price in BGN
price_in_bgn = price_in_usd * 1.85

# 6. Print and format
print(f'{price_in_usd:.2f} USD')
print(f'{price_in_bgn:.2f} BGN')