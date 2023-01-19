year = int(input())
year_str = str(year)

while len(year_str) != len(set(year_str)):
    year += 1
    year_str = str(year)

print(year)