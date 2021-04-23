load_capacity = float(input())
suitcase_volume = input()

max_suitcase_volume = 0
suitcase_count = 0

while suitcase_volume != "End":
    suitcase_volume = float(suitcase_volume)
    calculated_suitcase_volume = (suitcase_volume * 0.1) + suitcase_volume
    max_suitcase_volume += calculated_suitcase_volume
    suitcase_count += 1
    
    if max_suitcase_volume <= load_capacity:
        suitcase_volume = float(suitcase_volume)
        break
    else:
        print(f"No more space!\nStatistic: {suitcase_count} suitcases loaded.")

if suitcase_volume == "End":
    print(f"Congratulations! All suitcases are loaded!\nStatistic: {suitcase_count} suitcases loaded.")