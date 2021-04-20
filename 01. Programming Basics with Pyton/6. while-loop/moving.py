# 1. Read input data
width = int(input())
lenght = int(input())
height = int(input())

free_space = width * lenght * height
boxes_count = 0
has_enough_space = True
# 2. Calculate boxes count until free > 0 or Done
command = input()
while command != "Done":
    # 2.1. read boxes count
    # 2.2. calculate boxes total volume
    boxes_count = int(command)
    # 2.3. check if free space is enough
    if free_space >= boxes_count:
        free_space -= boxes_count
    # 2.4. If not enough space -> print free space needed
    else:
        has_enough_space = False
        break
    command = input()

# 3. If Done -> Calculate left space
if has_enough_space:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {boxes_count - free_space} Cubic meters more.")