def get_odd_even_sums(number):
    for n in number:

        if number % 2 == 0:
            odd_sum = number
            return odd_sum
        else:
            even_sum = number
            return even_sum


output = get_odd_even_sums(12345)
print(output)
f"Odd sum = {odd_sum}, Even sum = {even_sum}"
