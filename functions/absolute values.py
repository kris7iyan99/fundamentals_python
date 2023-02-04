numbers = input().split()
number = []

for num in numbers:
    number.append(abs(float(num)))

print(number)