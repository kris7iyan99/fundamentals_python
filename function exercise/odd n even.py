def sum (number_as_str):
    odd = 0
    even = 0

    for digit_as_str in number_as_str:
        digit = int(digit_as_str)

        if digit % 2 == 0:
            even += digit
        elif digit % 2 == 1:
            odd += digit

    result = f'Odd sum = {odd}, Even sum = {even}'
    return result


number_as_str = input()

res = sum(number_as_str)
print(res)