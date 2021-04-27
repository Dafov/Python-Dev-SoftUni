# 1. Read input data
days_stayed = int(input())
room_type = input()
feedback = input()

nights = days_stayed - 1
price_per_night = 1
discount = 0

# 2. Check room type
if room_type == "apartment":
    price_per_night = 25
    # 2.1. Check night staying -> discount
    if nights < 10:
        discount = 0.3
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.5
elif room_type == "president apartment":
    price_per_night = 35
    if nights < 10:
        discount = 0.1
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.2
elif room_type == "room for one person":
    price_per_night = 18
# 3. Calculate price with discount
total_price = nights * price_per_night
if discount != 0:
    total_price -= total_price * discount

# 4. Check feedback
if feedback == "positive":

# 4.1. + -> +25%

    total_price += total_price * 0.25

# 4.2. - -> -10%
else:
    total_price -= total_price * 0.1
# 5. Print and format
print(f"{total_price:.2f}")
