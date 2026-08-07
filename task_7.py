import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Словник для підрахунку кількості випадань кожної суми від 2 до 12
    counts = {s: 0 for s in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        counts[dice_sum] += 1

    # Обрахування ймовірності випаду кожної суми
    probabilities = {s: counts[s] / num_rolls for s in counts}

    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, tick_label=sums, color='skyblue', edgecolor='black')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках (Метод Монте-Карло)')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob + 0.002, f"{prob*100:.2f}%", ha='center', fontsize=9)

    plt.ylim(0, max(probs) + 0.03)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\n--- Симуляція для {accuracy:,} кидків ---")
        probabilities = simulate_dice_rolls(accuracy)

        # Вивід результатів у консоль у вигляді таблиці
        print(f"{'Сума':<6} | {'Монте-Карло (%)':<18}")
        print("-" * 27)
        for s, p in probabilities.items():
            print(f"{s:<6} | {p * 100:.2f}%")

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)