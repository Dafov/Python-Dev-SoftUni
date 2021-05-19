string_input = input()
command = input()

while command != "Decode":
    args = command.split("|")
    cmd = args[0]

    if cmd == "Move":
        num_of_letters = int(args[1])
        index = num_of_letters - 1
        string_input = string_input[index + 1:] + string_input[:index + 1]

    elif cmd == "Insert":
        index = int(args[1])
        value_to_insert = args[2]
        string_input = string_input[:index] + value_to_insert + string_input[index:]

    elif cmd == "ChangeAll":
        substring = args[1]
        replacement = args[2]
        string_input = string_input.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {string_input}")
