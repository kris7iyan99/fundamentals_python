card = input()
list = card.split()
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list2_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for el in list:
    element = el.split('-')
    team = element[0]
    player = int(element[1])
    if team == 'A':
        if player in list_A:
            list_A.remove(player)
    elif team == 'B':
        if player in list2_B:
            list2_B.remove(player)

    if len(list_A) < 7 or len(list2_B) < 7:
        print('Game was terminated')
        break
        

print(f'Team A - {len(list_A)}; Team B - {len(list2_B)}')