cards = input().split()
shuffle = int(input())

first_half = []
second_half = []

for idx in range(1, len(cards) - 1):
    card = cards[idx]
    if idx < len(cards) / 2:
        first_half.append(card)
    else:
        second_half.append(card)


shuffled = []
first_part = 0
second_part = 0

for idx in range(len(first_half) * 2):
    if idx % 2 == 0:
        shuffled.append(second_half[second_part])
        second_part += 1
    else:
        shuffled.append(first_half[first_part])
        first_part += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)