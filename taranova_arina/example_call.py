# example_call.py
from taranova_ttl import ttl_cache
import time

@ttl_cache(5)
def slow_add(a, b):
    print(f"Обчислення slow_add({a}, {b})")
    time.sleep(0.5)
    return a + b

if __name__ == "__main__":
    print("Перший виклик:")
    print(slow_add(1, 2))

    print("\nДругий виклик (кеш):")
    print(slow_add(1, 2))

    print("\nПісля зміни аргументів:")
    print(slow_add(2, 3))

    print("\nЧекаємо 6 секунд...")
    time.sleep(6)
    print(slow_add(1, 2))

    print("\nІнформація про кеш:")
    print(slow_add.cache_info())

    print("\nОчищення кеша:")
    slow_add.cache_clear()
    print(slow_add.cache_info())
