message = input()

data = input()
while data != "Reveal":
    tokens = data.split(":|:")
    command = tokens[0]
    if command == "InsertSpace":
        index = int(tokens[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = tokens[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring, replacement)
        print(message)

    data = input()

print(f"You have a new text message: {message}")
