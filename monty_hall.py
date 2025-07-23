import random

def monty_hall_simulate(switch: bool, num_trials: int) -> float:
    wins = 0
    for _ in range(num_trials):
        doors = [0, 0, 0]
        car_position = random.randint(0, 2)
        doors[car_position] = 1

        player_choice = random.randint(0, 2)
        possible_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        door_opened_by_host = random.choice(possible_doors)

        if switch:
            remaining_doors = [i for i in range(3) if i != player_choice and i != door_opened_by_host]
            player_choice = remaining_doors[0]

        if doors[player_choice] == 1:
            wins += 1

    return wins / num_trials

# --- Get input from user ---
try:
    num_trials = int(input("Enter number of simulations to run: "))
    switch_input = input("Do you want to switch doors? (yes/no): ").strip().lower()
    switch = switch_input == "yes"

    win_rate = monty_hall_simulate(switch, num_trials)
    print(f"\nWin rate with{' switching' if switch else 'out switching'}: {win_rate:.2%}")

except ValueError:
    print("Invalid input. Please enter a number for trials and 'yes' or 'no' to switch.")
