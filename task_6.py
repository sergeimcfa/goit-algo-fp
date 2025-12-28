items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості
    items_list = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        items_list.append((name, data["cost"], data["calories"], ratio))
    
    # Сортуємо за спаданням співвідношення
    items_list.sort(key=lambda x: x[3], reverse=True)
    
    total_calories = 0
    total_cost = 0
    chosen_items = []
    
    for item in items_list:
        if total_cost + item[1] <= budget:
            chosen_items.append(item[0])
            total_cost += item[1]
            total_calories += item[2]
            
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(item_names)
    
    # Таблиця DP: dp[i][w] - макс калорії для перших i предметів з бюджетом w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]
                
    # Відновлення обраних предметів
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(item_names[i-1])
            w -= costs[i-1]
            
    return chosen_items, dp[n][budget]

# Тестування
budget = 100
greedy_res = greedy_algorithm(items, budget)
dp_res = dynamic_programming(items, budget)

print(f"Жадібний алгоритм (бюджет {budget}): Вибрано {greedy_res[0]}, Калорії: {greedy_res[1]}, Вартість: {greedy_res[2]}")
print(f"Динамічне програмування (бюджет {budget}): Вибрано {dp_res[0]}, Калорії: {dp_res[1]}")
