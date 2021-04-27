# 1. Read input data
groups_count = int(input())

all_people = 0
musala = 0
montblanc = 0
klimanjaro = 0
k2 = 0
everest = 0

for num in range(groups_count):
    peoples_count = int(input())
    all_people += peoples_count
    if peoples_count <= 5:
        musala += peoples_count
    elif 6 <= peoples_count <= 12:
        montblanc += peoples_count
    elif 13 <= peoples_count <= 25:
        klimanjaro += peoples_count
    elif 26 <= peoples_count <= 40:
        k2 += peoples_count
    elif peoples_count >= 41:
        everest += peoples_count

musala_pers = (musala / all_people) * 100
mont_pers = (montblanc / all_people) * 100
kili_pers = (klimanjaro / all_people) * 100
k2_pers = (k2 / all_people) * 100
everest_pers = (everest / all_people) * 100

print(f"{musala_pers:.2f}%")
print(f"{mont_pers:.2f}%")
print(f"{kili_pers:.2f}%")
print(f"{k2_pers:.2f}%")
print(f"{everest_pers:.2f}%")