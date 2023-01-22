loss_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_counter = 0
sword_counter = 0
shield_counter = 0
armor_counter = 0

for fight in range(1, loss_fights + 1):
    if fight % 2 == 0:
        helmet_counter += 1
    if fight % 3 == 0:
        sword_counter += 1
    if fight % 6 == 0:
        shield_counter += 1
    if fight % 12 == 0:
        armor_counter += 1

output = (helmet_price * helmet_counter) + (sword_price * sword_counter) + \
             (shield_price * shield_counter) + \
             (armor_price * armor_counter)

print(f'Gladiator expenses: {output:.2f} aureus')
