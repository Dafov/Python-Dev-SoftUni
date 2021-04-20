input_num = input()

first_multiplicator = int(input_num[2])
second_multiplicator = int(input_num[1])
third_multiplicator = int(input_num[0])

for num in range(1, first_multiplicator + 1):
    for num2 in range(1, second_multiplicator + 1):
        for num3 in range(1, third_multiplicator + 1):
            result = num * num2 * num3
            print(f"{num} * {num2} * {num3} = {result}")
