team_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_a_count = 11
team_b_count = 11
is_terminated = False

cards = input().split()

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    number = int(tokens[1])
    index = number - 1

    if team == "A":
        if team_a[index] == 0:
            continue
        team_a[index] = 0
        team_a_count -= 1
    else:
        if team_b[index] == 0:
            continue
        team_b[index] = 0
        team_b_count -= 1

    if team_a_count < 7 or team_b_count < 7:
        is_terminated = True
        break
print(f"Team A - {team_a_count}; Team B - {team_b_count}")

if is_terminated:
    print("Game was terminated")
