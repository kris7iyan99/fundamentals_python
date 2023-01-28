n = int(input())

positive = []
negative = []
odd = []
even = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)


command = input()

if command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)
elif command == 'odd':
    print(odd)
else:
    print(even)