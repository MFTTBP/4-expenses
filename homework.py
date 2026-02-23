"""
#Мое дз
#"""
menu = [
    "1 - Добавить расход",
    "2 - Показать все расходы",
    "3 - Показать сумму и средний расход",
    "4 - Удалить расход по номеру",
    "Выход"
]
expenses = []

def add_expense(value: float):
    expenses.append(value)
    

def summa():
    s = sum(expenses)
    return s

def srednee():
    s = sum(expenses) / len(expenses)
    return s

def delete():
    del expenses[del_us]
    return expenses

while True:
    for i in menu:
        print(i)
    user = input("").capitalize()
    if user == "1":
        user_exp = float(input(""))
        add = add_expense(user_exp)
    elif user == "2":
        print(expenses)
    elif user == "3":
        print(f"Сумма: {summa()}")
        print(f"Среднее значение: {srednee()}")
    elif user == "4":
        del_us = int(input(""))
        dele = delete()
    if user == "Выход":
        break

