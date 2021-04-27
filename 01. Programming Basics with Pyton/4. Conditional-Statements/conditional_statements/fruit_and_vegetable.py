product = input()

is_fruit = product == "banana" or "apple" or "kiwi" or "cherry" or "lemon" or "grapes"
is_vegetable = product == "tomato" or "cucumber" or "pepper" or "carrot"
if is_fruit:
    print("fruit")

elif is_vegetable:
    print("vegetable")
else:
    print("unknown")
