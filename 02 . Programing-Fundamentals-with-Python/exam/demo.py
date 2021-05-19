n = int(input())

plants = {}
rariry = {}

for i in range(n):

    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])

    plants[plant] = plant
    plants[rarity] = rarity

print(plants)
print(rarity)
