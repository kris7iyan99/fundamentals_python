def calculator(command, num1, num2):
    result = 0

    if command == 'multiply':
        result = num1 * num2
    elif command == 'divide':
        result = num1 // num2
    elif command == 'add':
        result = num1 + num2
    elif command == 'subtract':
        result = num1 - num2

    return result

command = input()
num1 = int(input())
num2 = int(input())

res = calculator(command, num1, num2)

print(res)