# Menu items with their cost and calorie values

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """
    Selects items using a greedy approach.

    Items are sorted by calories-to-cost ratio.
    The item with the highest ratio is selected first.
    """

    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items = []
    total_calories = 0
    total_cost = 0

    for name, details in sorted_items:
        cost = details["cost"]
        calories = details["calories"]

        # Select the item if it fits within the remaining budget
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories

    return total_calories, total_cost, selected_items


def dynamic_programming(items, budget):
    """
    Finds the optimal combination of items using dynamic programming.

    Each item can be selected at most once.
    The goal is to maximize the total number of calories
    without exceeding the given budget.
    """

    item_names = list(items.keys())
    item_count = len(item_names)

    # Create a DP table:
    # rows represent items, columns represent available budgets
    dp = [
        [0] * (budget + 1)
        for _ in range(item_count + 1)
    ]

    # Fill the DP table
    for i in range(1, item_count + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for current_budget in range(budget + 1):
            # Do not select the current item
            dp[i][current_budget] = dp[i - 1][current_budget]

            # Select the current item if it fits
            if cost <= current_budget:
                dp[i][current_budget] = max(
                    dp[i][current_budget],
                    dp[i - 1][current_budget - cost] + calories,
                )

    # Restore the selected items from the DP table
    selected_items = []
    current_budget = budget

    for i in range(item_count, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            name = item_names[i - 1]
            selected_items.append(name)
            current_budget -= items[name]["cost"]

    selected_items.reverse()

    total_calories = dp[item_count][budget]
    total_cost = budget - current_budget

    return total_calories, total_cost, selected_items


def print_result(title, calories, cost, selected_items):
    """Prints the algorithm result in a consistent format."""

    print(f"\n=== {title} ===")
    print(f"Calories: {calories}")
    print(f"Spent: {cost}")
    print(f"Selected items: {selected_items}")


def main():
    budget = 100

    greedy_calories, greedy_cost, greedy_items = greedy_algorithm(
        items, budget
    )

    dp_calories, dp_cost, dp_items = dynamic_programming(
        items, budget
    )

    print_result(
        "Greedy Algorithm",
        greedy_calories,
        greedy_cost,
        greedy_items,
    )

    print_result(
        "Dynamic Programming",
        dp_calories,
        dp_cost,
        dp_items,
    )


if __name__ == "__main__":
    main()
