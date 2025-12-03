import random

def simulate_one_game():
    count = 0
    streak = 0
    last_flip = None
    flips = []

    while streak < 3:
        flip = random.choice(['О', 'Р'])
        flips.append(flip)
        count += 1

        if flip == last_flip:
            streak += 1
        else:
            streak = 1
            last_flip = flip

    print(''.join(flips), f"(попыток: {count})")
    return count

total_attempts = 0
num_simulations = 10

for _ in range(num_simulations):
    total_attempts += simulate_one_game()

average_attempts = total_attempts / num_simulations
print(f"Среднее количество попыток: {average_attempts:.1f}")