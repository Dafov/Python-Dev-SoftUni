total_electrons = int(input())

res = []
index_shell = 1

while total_electrons > 0:
    value = 2 * index_shell ** 2
    if total_electrons < value:
        res.append(total_electrons)
    else:
        res.append(value)

    total_electrons -= value
    index_shell += 1

print(res)