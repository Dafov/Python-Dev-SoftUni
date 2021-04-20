transactions_count = int(input())

transactions_made = 0
acc_balance = 0
while transactions_made < transactions_count:
    transaction_balance = float(input())
    if transaction_balance < 0:
        print("Invalid operation!")
        break

    acc_balance += transaction_balance
    transactions_made +=1
    print(f"Increase: {transaction_balance:.2f}")

print(f"Total: {acc_balance:.2f}")