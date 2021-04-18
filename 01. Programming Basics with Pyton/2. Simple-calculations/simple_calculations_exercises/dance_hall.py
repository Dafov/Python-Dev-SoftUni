# 1. Read input data
import math
l = float(input())
w = float(input())
a = float(input())

# 2. Calculate place area
area = (l * 100) * (w * 100)

# 3. Calculate taken area
wardrobe = (a * 100) * (a * 100)
bench = area / 10

# 4. Calculate free area
free_area = area - wardrobe - bench

# 5. Calculate dancers count
space_taken = 40
sprace_needed = 7000
dancers_count = free_area / (space_taken + sprace_needed)

# 6. Print and format
print(f'{math.floor(dancers_count)}')