record = float(input())
distance = float(input())
time = float(input())

total_time = distance * time

delay = distance // 15 * 12.5

total_time += delay

if total_time < record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")