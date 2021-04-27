factor = int(input())
count = int(input())
l = []
number = 0

for i in range(count):
    number += factor
    l.append(number)

print(l)