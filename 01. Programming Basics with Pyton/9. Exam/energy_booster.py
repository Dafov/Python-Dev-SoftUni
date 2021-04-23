flavor = input()
size = input()
count = int(input())

total_price = 0
total_ordered = 0
price = 0
discount = 0

if flavor == "Watermelon":
    if size == "small":
        price = 56
        total_ordered = count * 2
        total_price = total_ordered * price
    elif size == "big":
        price = 28.70
        total_ordered = count * 5
        total_price = total_ordered * price
elif flavor == "Mango":
    if size == "small":
        price = 36.66
        total_ordered = count * 2
        total_price = total_ordered * price
    elif size == "big":
        price = 19.6
        total_ordered = count * 5
        total_price = total_ordered * price
elif flavor == "Pineapple":
    if size == "small":
        price = 42.10
        total_ordered = count * 2
        total_price = total_ordered * price
    elif size == "big":
        price = 24.80
        total_ordered = count * 5
        total_price = total_ordered * price
elif flavor == "Raspberry":
    if size == "small":
        price = 20
        total_ordered = count * 2
        total_price = total_ordered * price
    elif size == "big":
        price = 15.20
        total_ordered = count * 5
        total_price = total_ordered * price

if 400 <= total_price <= 1000:
   discount = total_price * 0.15
   total_price = total_price - discount

elif total_price > 1000:
    discount = total_price / 2
    total_price = total_price - discount

print(f"{total_price:.2f} lv.")