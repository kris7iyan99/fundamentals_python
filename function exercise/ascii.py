def problem_1 (start, end):
    result = ''
    for num in range(ord(start) + 1, ord(end)):
        result += f'{chr(num)} '
    return result


num1 = input()
num2 = input()


res = (problem_1(num1,num2))
print(res)