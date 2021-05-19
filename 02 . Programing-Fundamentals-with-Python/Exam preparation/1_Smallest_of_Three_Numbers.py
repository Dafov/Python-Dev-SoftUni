# def get_smallest_num(a, b, c):
#     smallest = 0
#
#     if a < b and a < c:
#         smallest = a
#     elif b < a and b < c:
#         smallest = b
#     else:
#         smallest = c
#
#     return smallest


a = int(input())
b = int(input())
c = int(input())

res = min(a, b, c)
print(res)


