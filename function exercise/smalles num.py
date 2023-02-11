def smallest (num1, num2, num3):

    if num1 <= num2 and num1 <= num3:
        result = num1
    elif num2 <= num3 and num2 <= num1:
        result = num2
    else:
        result = num3
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())

res = smallest(num1, num2, num3)
print(res)