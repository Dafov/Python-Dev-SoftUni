count_numbers = int(input())

biggest_number = 0
smallest_number = 0

for position in range(count_numbers):
    current_number = int(input())
    if position == 0:
        biggest_number = current_number
        smallest_number = current_number
    else:
        if current_number > biggest_number:
            biggest_number = current_number
        elif current_number < smallest_number:
            smallest_number = current_number

print(f"Max number: {biggest_number}\nMin number: {smallest_number}")