n = input().split(', ')
count_of_beggars = int(input())

beggars = [0] * count_of_beggars

for idx in range(len(n)):
    beggar_idx = idx % count_of_beggars
    num = int(n[idx])
    beggars[beggar_idx] += num

print(beggars)
