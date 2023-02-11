num1 = int(input())
num2 = int(input())

result = 0
for el in range(num1 + 1):
    if el != 0:
        result *= el
print(f'{result / num2:.2f}')
