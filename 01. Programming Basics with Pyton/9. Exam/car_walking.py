minutes_walking = int(input())
counts_of_walking = int(input())
kal_consumed = int(input())

total_walking_minutes = minutes_walking * counts_of_walking
kal_burned = total_walking_minutes * 5

if kal_burned >= (kal_consumed / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {kal_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {kal_burned}.")