username = input()

cmd_input = input()

while cmd_input != "Sign up":
    args = cmd_input.split()
    cmd = args[0]

    if cmd == "Case":
        type = args[1]

        if type == "lower":
            username = username.lower()
        elif type == "upper":
            username = username.upper()

        print(username)

    elif cmd == "Reverse":
        start_index = int(args[1])
        end_index = int(args[2])

        res = username[start_index:end_index + 1]
        reversed_res = res[::-1]
        # reversed_res = "".join(list(res[::-1]))
        print(reversed_res)

    elif cmd == "Cut":
        pass

    elif cmd == "Replace":
        pass
    elif cmd == "Chek":
        pass

    cmd_input = input()

print(username)
