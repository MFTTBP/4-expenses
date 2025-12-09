"""
Мое дз
"""


buy_list = [100, 230, 1000, 3200, 1234, 222, 888]
list_sum = sum(buy_list)
general = sum(buy_list) // 7
print(f"Сумма: {list_sum}")
print(f"Среднее значение: {general}")
min_buy = min(buy_list)
max_buy = max(buy_list)
print(f"Минимальное значение: {min_buy}")
print(f"Максимальное значение: {max_buy}")

tuple_buy = list_sum, min_buy, max_buy

print(tuple_buy)
