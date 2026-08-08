# Перелік страв з вартістю та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Жадібний підхід (Greedy approach)
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості (calories / cost)
    sorted_items = sorted(
        items.items(), 
        key=lambda x: x[1]["calories"] / x[1]["cost"], 
        reverse=True
    )
    
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in sorted_items:
        cost = details["cost"]
        calories = details["calories"]
        
        # Якщо страва вміщується в залишок бюджету — беремо її
        if cost <= remaining_budget:
            chosen_items.append(item)
            total_calories += calories
            remaining_budget -= cost

    return total_calories, budget - remaining_budget, chosen_items


# Підхід динамічного програмування (Dynamic Programming approach)
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    # Таблиця DP: rows (0..n) x cols (0..budget)
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Побудова таблиці максимальних калорій
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                # Вибираємо максимум між: не брати страви або взяти страву + калорії за залишок бюджету
                dp_table[i][b] = max(dp_table[i - 1][b], dp_table[i - 1][b - cost] + calories)
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    # Відновлення обраного набору страв з таблиці DP
    chosen_items = []
    temp_budget = budget

    for i in range(n, 0, -1):
        # Якщо значення змінилося, значить i-та страва була включена в оптимальний набір
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            name = item_names[i - 1]
            chosen_items.append(name)
            temp_budget -= items[name]["cost"]

    chosen_items.reverse()  # Повертаємо початковий порядок страв
    total_cost = budget - temp_budget
    max_calories = dp_table[n][budget]

    return max_calories, total_cost, chosen_items


if __name__ == '__main__':
    budget = 100

    greedy_calories, greedy_cost, greedy_items = greedy_algorithm(items, budget)
    dp_calories, dp_cost, dp_items = dynamic_programming(items, budget)

    print("=== Результат жадібного алгоритму ===")
    print(f"Калорії: {greedy_calories}, Витрачено: {greedy_cost}, Страви: {greedy_items}")

    print("\n=== Результат динамічного програмування ===")
    print(f"Калорії: {dp_calories}, Витрачено: {dp_cost}, Страви: {dp_items}")
