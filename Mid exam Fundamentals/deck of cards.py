cards = input().split(", ")
n = int(input())

for _ in range(n):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if card_name in cards:
            print("Card is already in the deck")
        else:
            cards.append(card_name)
            print("Card successfully added")
    elif action == "Remove":
        card_name = command[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(command[1])
        if index < 0 or index >= len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
    elif action == "Insert":
        index = int(command[1])
        card_name = command[2]
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif card_name in cards:
            print("Card is already added")
        else:
            cards.insert(index, card_name)
            print("Card successfully added")

print(", ".join(cards))