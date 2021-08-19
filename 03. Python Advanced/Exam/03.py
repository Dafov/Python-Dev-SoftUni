def fill_the_box(height, length, width, *args):
    free_space = height * length * width
    boxes = 0

    for i in range(len(args)):
        if args[i] == "Finish":
            if free_space > boxes:
                return f"There is free space in the box. You could put {free_space - boxes} more cubes."
            else:
                return f"No more free space! You have {boxes - free_space} more cubes."
        else:
            boxes += args[i]


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))