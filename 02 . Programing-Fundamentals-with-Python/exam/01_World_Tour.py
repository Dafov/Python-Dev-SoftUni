stops = input()
cmd_input = input()

while cmd_input != "Travel":
    args = cmd_input.split(":")
    command = args[0]

    if command == "Add Stop":
        index = int(args[1])
        str_cmd = args[2]

        stops = stops[:index] + f"{str_cmd}" + stops[index:]
        print(stops)

    elif command == "Remove Stop":
        start_index = int(args[1])
        end_index = int(args[2])
        length = int(len(stops))

        res = stops[start_index:end_index + 1]
        stops = stops.replace(res, "")
        print(stops)

    elif command == "Switch":
        old_string = args[1]
        new_string = args[2]

        stops = stops.replace(old_string, new_string)
        print(stops)

    cmd_input = input()

print(f"Ready for world tour! Planned stops: {stops}")