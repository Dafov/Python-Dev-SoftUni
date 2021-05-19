n = int(input())

plants = {}

for i in range(n):

    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])

    plants["name"] = plant
    plants["rarity"] = rarity


while True:
    input_command = input()
    if input_command == "Exhibition":
        break

    args = input_command.split(":")
    command = args[0]
    plant = args[1]

    if command == "Rate":
         if plant in plants:
             continue
         rarity[plant] = rarity

    elif command == "Update":
        pass
    elif command == "Reset":
        pass
    else:
        print("error")


print("Plants for the exhibition:")
# print(f"- {plants[plant]}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}")

