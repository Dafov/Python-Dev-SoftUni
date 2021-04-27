num = map(int, input().split(", "))
print([index for index, number in enumerate(num) if number % 2 == 0])