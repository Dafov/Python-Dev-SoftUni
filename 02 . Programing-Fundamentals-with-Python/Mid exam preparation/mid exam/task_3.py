def get_elements_index_value_first(number):
    return elements[first_index]


def get_elements_index_value_second(number):
    return elements[second_index]


elements = input().split()

input_command = input()

moves = 0

while input_command != "end":
    args = input_command.split()
    first_index = int(args[0])
    second_index = int(args[1])
    index_in_the_middle = int((len(elements) // 2))

    first_match = int(get_elements_index_value_first(first_index))
    second_match = int(get_elements_index_value_second(second_index))
    moves += 1

    if first_index == second_index or first_index < 0:
        print("Invalid input! Adding additional elements to the board")
        elements.insert(index_in_the_middle, f"-{moves}a")
        elements.insert(index_in_the_middle, f"-{moves}a")

    if first_match == second_match:
        print(f"Congrats! You have found matching elements - {first_match}!")
        elements.pop(first_match)
        elements.pop(second_match)

    elif first_match != second_match:
        print("Try again!")

    if len(elements) < 2:
        print(f"You have won in {moves} turns!")
        break


    input_command = input()

if input_command == "end":
    print("Sorry you lose :(")
    print(" ".join(elements))
