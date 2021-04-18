hour = int(input())
minutes = int(input())
new_minutes = minutes + 15
if new_minutes < 60:
    print(str(hour) + ':' + str(new_minutes))

elif new_minutes >= 60 and hour + 1 < 24:
    hour = hour + 1
    new_minutes = new_minutes - 60
    print(str(hour) + ':' + str(format(new_minutes, '02d')))

elif new_minutes >= 60 and hour + 1 >= 24:
    hour = 0
    new_minutes = new_minutes - 60
    print(str(hour) + ':' + str(format(new_minutes, '02d')))