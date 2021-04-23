n = int(input())
CAPACITY = 255

total_liters = 0
for i in range(1, n + 1):
    liters = int(input())
    if total_liters + liters > CAPACITY:
        print("Insufficient capacity!")
    else:
        total_liters += liters

print(total_liters)
