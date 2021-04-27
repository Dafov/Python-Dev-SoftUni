name = input()

grade = 1
sum_marks = 0
times_expelled = 0
while grade <= 12:
    mark = float(input())
    if mark >= 4:
        grade += 1
        sum_marks += mark
    else:
        times_expelled += 1
        if times_expelled == 2:
            print(f"{name} has been excluded at {grade} grade")
            break

average_mark = sum_marks / 12
if times_expelled != 2:
    print(f"{name} graduated. Average grade: {average_mark:.2f}")