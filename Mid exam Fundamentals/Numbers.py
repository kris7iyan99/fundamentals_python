sequence = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == "Add":
        sequence.append(int(command[1]))
    elif command[0] == "Remove":
        if int(command[1]) in sequence:
            sequence.remove(int(command[1]))
    elif command[0] == "Replace":
        if int(command[1]) in sequence:
            index = sequence.index(int(command[1]))
            sequence[index] = int(command[2])
    elif command[0] == "Collapse":
        sequence = [x for x in sequence if x >= int(command[1])]
    elif command[0] == "Finish":
        print(" ".join([str(x) for x in sequence]))
        break