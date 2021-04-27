# 1. Input read data
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
# 2. Calculate length and height
length = abs(x1 - x2)
width = abs(y1 - y2)
# 3. Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)
# 4. Print and format
print(f'{area:.2f}')
print(f'{perimeter:.2f}')