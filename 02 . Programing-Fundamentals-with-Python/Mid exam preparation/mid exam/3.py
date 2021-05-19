num_pieces = int(input())

coll = {}

for n in range(num_pieces):
    pieces = input().split("|")
    album = pieces[0]
    composer = pieces[1]
    note = pieces[2]

    coll[album] = {}
    coll[album]["composer"] = composer
    coll[album]["note"] = note


pieces = input()
while pieces != "Stop":
    args = pieces.split("|")
    cmd = args[0]
    album_input = args[1]

    if cmd == "Add":
        composer_input = args[2]
        note_input = args[3]

        if album_input not in coll:
            coll[album]["composer"] += composer_input
            coll[album]["note"] += note_input
            print(f"{album_input} by {composer_input} in {note_input} added to the collection!")
        else:
            print(f"{album_input} is already in the collection!")


    elif cmd == "Remove":

        if album_input not in coll:
            print(f"Invalid operation! {album_input} does not exist in the collection.")
        else:
            print(f"Successfully removed {album_input}!")

    elif cmd == "ChangeKey":
        note_input = args[2]

        if album_input in coll:

            temp = coll[album]["note"]
            coll[album]["note"] = note_input
            print(f"Changed the key of {temp} to {note_input}!")

        else:
            print(f"Invalid operation! {album_input} does not exist in the collection.")

    pieces = input()

sorted_albums = sorted(coll.keys(), key=lambda c: (coll[c]["composer"], c))

for x in sorted_albums:
    print(f"{coll} -> Composer: {x}, Key: {note}")