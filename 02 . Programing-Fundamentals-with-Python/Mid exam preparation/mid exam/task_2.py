peoples = int(input())
lift_taken_seats = input().split()

lift = []

for i in range(len(lift_taken_seats)):
    seat = int(lift_taken_seats[i])

    if seat >= 4:
        i += 1

    elif seat < 4:
        empty_seat = 4 - seat
        peoples -= empty_seat
        lift.append(seat)


    if peoples == 0:
        print("The lift has empty spots!")
        print(lift)
    else:
        print(f"There isn't enough space! {peoples} people in a queue!")
        print(lift)
