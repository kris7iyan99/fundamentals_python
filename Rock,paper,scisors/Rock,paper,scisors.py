import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper, [s]cissors:')

if player_move == 'r':
    player_move = 'Rock'
elif player_move == 'p':
    player_move = 'Paper'
elif player_move == 's':
    player_move = 'Scissors'
else:
    raise SystemExit('Invalid input.Try again...')
print(player_move)

computer_random_number = random.randint(1, 3)
computer_move = ''

if computer_random_number == 1:
    computer_move = 'Rock'
elif computer_random_number == 2:
    computer_move = 'Paper'
elif computer_random_number == 3:
    computer_move = 'Scissors'

print(f'The computer choose {computer_move}.')

if (player_move == 'Paper' and computer_move == 'Rock') or \
    (player_move == 'Rock' and computer_move == 'Scissors') or \
        (player_move == 'Scissors' and computer_move =='Paper'):
    print('You win!')
elif player_move == computer_move:
    print('Draw!')
else:
    print('You lose!')
