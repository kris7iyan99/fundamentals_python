input_el = input().split()
result = []

for el in input_el:
    result = [float(el) for element in el]
    result.append(element)
print(result)