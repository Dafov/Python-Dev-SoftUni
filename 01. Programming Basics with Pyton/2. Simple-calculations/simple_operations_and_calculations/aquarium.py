# 1. Read input data and convert data type
lenght = int(input())
width = int(input())
height = int(input())
percent_stuff = float(input())

# 2. Calculate aquarium volume
total_volume = lenght * width * height

# 3. Convert volume cm3 -> liters
volume_liters = total_volume * 0.001

# 4. Calculate liters taken from stuff
volume_stuff = (volume_liters * percent_stuff) / 100

# 5. Calculate volume left
final_volume = volume_liters - volume_stuff

# 6. Print and format
print(f'{final_volume:.3f}')