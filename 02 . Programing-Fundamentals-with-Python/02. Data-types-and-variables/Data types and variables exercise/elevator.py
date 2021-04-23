import math

people_count = int(input())
capacity = int(input())

# all_courses = math.ceil(people_count / capacity)
# print(all_courses)

if people_count % capacity == 0:
    result = people_count // capacity
else:
    result = people_count // capacity + 1

print(result)
