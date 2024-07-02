import random

print("Tossing a coin...")

results = []
for i in range(3):
    result = "Heads" if random.randint(0, 1) == 0 else "Tails"
    results.append(result)
    print(f"Round {i + 1}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")
