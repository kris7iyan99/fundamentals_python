n = int(input())

word = input()
list1 = []
list2 = []

for _ in range(n):
    current_string = input()
    list1.append(current_string)

    if word in current_string:
        list2.append(current_string)

print(list1)
print(list2)
