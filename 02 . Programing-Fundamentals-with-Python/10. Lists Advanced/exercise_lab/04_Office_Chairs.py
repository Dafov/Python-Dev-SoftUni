meeting_rooms = int(input())

empty_chairs = 0
has_enough_chairs = True

for meeting_room in range(1, meeting_rooms + 1):
    room_data = input().split()
    chairs_count = len(room_data[0])
    number_of_people = int(room_data[1])

    if chairs_count >= number_of_people:
        empty_chairs += chairs_count - number_of_people
    else:
        has_enough_chairs = False
        print(f"{number_of_people - chairs_count} more chairs needed in room {meeting_room}")

if has_enough_chairs:
    print(f"Game On, {empty_chairs} free chairs left") 
