from typing import List, Dict, Tuple

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    # Тут повинен бути ваш код
    memo = {}

    def helper(n: int) -> Tuple[int, List[int]]:
        if n == 0:
            return 0, [] # Якщо довжина стрижня = 0, то прибуток 0
        if n in memo:
            return memo[n] # Якщо вже обчислено, повертаємо результат

        max_profit = -1 # Ініціалізуємо максимальний прибуток; -1, щоб він був менший за будь-який прибуток
        best_cuts = []
        for i in range(1, n + 1):
            if i <= len(prices):
                current_profit, current_cuts = helper(n - i) # Рекурсивно знаходимо прибуток для решти стрижня
                current_profit += prices[i - 1] # Додаємо прибуток від розрізу
                if current_profit > max_profit:
                    max_profit = current_profit # Зберігаємо найкращий прибуток
                    best_cuts = current_cuts + [i] # Зберігаємо найкращий розріз

        memo[n] = (max_profit, best_cuts)
        return memo[n]

    max_profit, cuts = helper(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    # Тут повинен бути ваш код

    dp = [0] * (length + 1) # Ініціалізуємо список для зберігання максимального прибутку
    cuts = [[] for _ in range(length + 1)] # Ініціалізуємо список для зберігання розрізів

    for i in range(1, length + 1):
        max_profit = -1 # Ініціалізуємо максимальний прибуток; -1, щоб він був менший за будь-який прибуток
        best_cut = []
        for j in range(1, i + 1):
            if j <= len(prices):
                current_profit = prices[j - 1] + dp[i - j] # Знаходимо прибуток від розрізу
                if current_profit > max_profit:
                    max_profit = current_profit # Зберігаємо найкращий прибуток
                    best_cut = cuts[i - j] + [j] # Зберігаємо найкращий розріз
        dp[i] = max_profit
        cuts[i] = best_cut

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
