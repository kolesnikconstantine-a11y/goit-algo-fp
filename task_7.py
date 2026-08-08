import random
import matplotlib.pyplot as plt


NUM_SIDES = 6
MIN_SUM = 2
MAX_SUM = 12


def simulate_dice_rolls(num_rolls):
    """Simulate rolling two dice and calculate probabilities for each sum."""

    if num_rolls <= 0:
        raise ValueError("Number of rolls must be greater than zero.")

    counts = {dice_sum: 0 for dice_sum in range(MIN_SUM, MAX_SUM + 1)}

    # Generate random dice rolls and count each possible sum.
    for _ in range(num_rolls):
        die1 = random.randint(1, NUM_SIDES)
        die2 = random.randint(1, NUM_SIDES)

        dice_sum = die1 + die2
        counts[dice_sum] += 1

    # Convert occurrence counts into probabilities.
    return {
        dice_sum: count / num_rolls
        for dice_sum, count in counts.items()
    }


def print_results(probabilities, num_rolls):
    """Print simulation results as a formatted table."""

    print(f"\n--- Simulation for {num_rolls:,} rolls ---")
    print(f"{'Sum':<6} | {'Monte Carlo (%)':<18}")
    print("-" * 27)

    for dice_sum, probability in probabilities.items():
        print(f"{dice_sum:<6} | {probability * 100:.2f}%")


def plot_probabilities(probabilities, num_rolls):
    """Display probabilities of dice sums as a bar chart."""

    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        sums,
        probabilities_values,
        edgecolor="black"
    )

    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.title(
        f"Probability of Dice Sums "
        f"(Monte Carlo, {num_rolls:,} rolls)"
    )

    # Display probability values above each bar.
    for bar, probability in zip(bars, probabilities_values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.002,
            f"{probability * 100:.2f}%",
            ha="center",
            fontsize=9
        )

    plt.xticks(sums)
    plt.ylim(0, max(probabilities_values) + 0.03)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


def run_simulations():
    """Run simulations with different numbers of dice rolls."""

    roll_counts = [100, 1_000, 10_000, 100_000]

    for num_rolls in roll_counts:
        probabilities = simulate_dice_rolls(num_rolls)

        print_results(probabilities, num_rolls)
        plot_probabilities(probabilities, num_rolls)


if __name__ == "__main__":
    run_simulations()
