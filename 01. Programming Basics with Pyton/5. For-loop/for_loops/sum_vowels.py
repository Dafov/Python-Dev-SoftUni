input_text = input()
text_lenght = len(input_text)
vowels_sum = 0

for char_pos in range(text_lenght):
    current_char = input_text[char_pos]
    if current_char == "a":
        vowels_sum += 1
    elif current_char == "e":
        vowels_sum += 2
    elif current_char == "i":
        vowels_sum += 3
    elif current_char == "o":
        vowels_sum += 4
    elif current_char == "u":
        vowels_sum += 5

print(vowels_sum)
