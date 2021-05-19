input_command = input()
total_price = 0
total_price_with_taxes = 0
discount = total_price_with_taxes * 0.1
taxes = 0

while True:
    if "." in input_command or input_command.isdigit() or input_command.lstrip("-").isdigit():
        price = float(input_command)

        if price < 0:
            print("Invalid price!")
            continue
        else:
            total_price += price
            taxes_aplied = price * 0.2
            taxes += taxes_aplied

    else:
        if input_command == "regular":
            total_price_with_taxes = total_price + taxes

            if total_price_with_taxes == 0:
                print("Invalid order!")
                break

            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {total_price:.2f}$")
            break

        if input_command == "special":
            total_price_with_taxes = (total_price + taxes)
            after_discount = total_price_with_taxes - discount

            if total_price_with_taxes == 0:
                print("Invalid order!")
                break

            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {after_discount:.2f}$")
            break

    input_command = input()
