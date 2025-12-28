import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_simulations=100000):
    counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1
        
    probabilities = {k: v / num_simulations * 100 for k, v in counts.items()}
    return probabilities

def analytical_probabilities():
    # Аналітичний розрахунок (всього 36 комбінацій)
    counts = {i: 0 for i in range(2, 13)}
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            counts[d1 + d2] += 1
    
    probabilities = {k: v / 36 * 100 for k, v in counts.items()}
    return probabilities

# Виконання
num_sims = 1000000
mc_probs = monte_carlo_dice(num_sims)
an_probs = analytical_probabilities()

print(f"{'Сума':<5} | {'Монте-Карло (%)':<15} | {'Аналітична (%)':<15} | {'Різниця (%)':<10}")
print("-" * 55)
for i in range(2, 13):
    print(f"{i:<5} | {mc_probs[i]:<15.2f} | {an_probs[i]:<15.2f} | {abs(mc_probs[i] - an_probs[i]):<10.2f}")

# Побудова графіка
sums = list(range(2, 13))
plt.figure(figsize=(10, 6))
plt.plot(sums, [mc_probs[s] for s in sums], label='Монте-Карло', marker='o')
plt.plot(sums, [an_probs[s] for s in sums], label='Аналітичні', marker='x', linestyle='--')
plt.xlabel('Сума кубиків')
plt.ylabel('Ймовірність (%)')
plt.title(f'Ймовірності суми двох кубиків (Симуляцій: {num_sims})')
plt.legend()
plt.grid(True)
plt.show()
