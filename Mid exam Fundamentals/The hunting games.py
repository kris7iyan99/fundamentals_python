days = int(input())
players = int(input())
group_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())

total_water = water_per_person_per_day * players * days
total_food = food_per_person_per_day * players * days

for day in range(1, days + 1):
    energy_loss = float(input())

    group_energy -= energy_loss

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        water_to_drink = 0.3 * total_water / players
        total_water -= water_to_drink
        group_energy *= 1.05

    if day % 3 == 0:
        food_to_eat = total_food / players
        total_food -= food_to_eat
        group_energy *= 1.1

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with {group_energy:.2f} energy!")