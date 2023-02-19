people = int(input())
lift_state = list(map(int, input().split()))

for i in range(len(lift_state)):
    while lift_state[i] < 4 and people > 0:
        lift_state[i] += 1
        people -= 1
        if people == 0:
            break

if people == 0 and 0 < sum(lift_state) < len(lift_state)*4:
    print("The lift has empty spots!")
    print(" ".join(str(x) for x in lift_state))
elif people > 0 and sum(lift_state) == len(lift_state)*4:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(str(x) for x in lift_state))
elif people == 0 and sum(lift_state) == len(lift_state)*4:
    print(" ".join(str(x) for x in lift_state))
