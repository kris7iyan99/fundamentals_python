sequence = input().split()
moves_count = 0

while True:
    command = input()

    if command == 'end':
        if len(sequence) == 0:
            print(f"You have won in {moves_count} turns!")
        else:
            print(f"Sorry you lose :(\n{' '.join(sequence)}")
        break

    indexes = [int(i) for i in command.split()]
    if indexes[0] == indexes[1] or indexes[0] < 0 or indexes[0] >= len(sequence) or indexes[1] < 0 or indexes[1] >= len(sequence):
        moves_count += 1
        additional_element = f"-{moves_count}a"
        index_to_add = len(sequence) // 2
        sequence.insert(index_to_add, additional_element)
        sequence.insert(index_to_add, additional_element)
        print("Invalid input! Adding additional elements to the board")
    elif sequence[indexes[0]] == sequence[indexes[1]]:
        element = sequence[indexes[0]]
        del sequence[indexes[1]]
        del sequence[indexes[0]]
        moves_count += 1
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        moves_count += 1
        print("Try again!")
