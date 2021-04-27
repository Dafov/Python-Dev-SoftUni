destination = input()
date_range = input()
nights = int(input())

price_per_night = 0
money_needed = 0

if destination == "France" and date_range == "21-23":
    price_per_night = 30

elif destination == "France" and date_range == "24-27":
    price_per_night = 35

elif destination == "France" and date_range == "28-31":
    price_per_night = 40

elif destination == "Germany" and date_range == "21-23":
    price_per_night = 32

elif destination == "Germany" and date_range == "24-27":
    price_per_night = 37

elif destination == "Germany" and date_range == "28-31":
    price_per_night = 43

elif destination == "Italy" and date_range == "21-23":
    price_per_night = 28

elif destination == "Italy" and date_range == "24-27":
    price_per_night = 32

elif destination == "Italy" and date_range == "28-31":
    price_per_night = 39

money_needed = price_per_night * nights

print(f"Easter trip to {destination} : {money_needed:.2f} leva.")

