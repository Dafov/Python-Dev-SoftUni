def repeat_string(string_to_repeat: str, number_of_repetiotions: int):
    return string_to_repeat * number_of_repetiotions


string_to_repeat: str = input()
number_of_repetiotions: int = int(input())

print(repeat_string(string_to_repeat, number_of_repetiotions))
