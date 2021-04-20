player1_eggs = int(input())
player2_eggs = int(input())

winner = input()
p1_left_eggs = player1_eggs
p2_left_eggs = player2_eggs

while winner != "End of battle":

    if winner == "one":
        p2_left_eggs -= 1
        if p2_left_eggs == 0:
            print(f"Player two is out of eggs. Player one has {p1_left_eggs} eggs left.")
            break
        winner = input()

    elif winner == "two":
        p1_left_eggs -= 1
        if p1_left_eggs == 0:
            print(f"Player one is out of eggs. Player two has {p2_left_eggs} eggs left.")
            break
        winner = input()

if winner == "End of battle":
    print(f"Player one has {p1_left_eggs} eggs left.\nPlayer two has {p2_left_eggs} eggs left.")
