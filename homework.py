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


def print_report(exp: list, summ: float):
    print(f"Расходы:{exp}\nСумма:{summ}")


def add_expense(value: float):
    expenses.append(value)


def summa():
    return sum(expenses)


def srednee():
    if len(expenses) == 0:
        return 0
    return sum(expenses) / len(expenses)


def delete(index):
    if 0 <= index < len(expenses):
        del expenses[index]
    else:
        print("Неверный номер расхода")


while True:
    for i in menu:
        print(i)
    user = input("")
    if user == "1":
        user_exp = float(input(""))
        add_expense(user_exp)
    elif user == "2":
        print(expenses)
    elif user == "3":
        print(f"Сумма: {summa()}")
        print(f"Среднее значение: {srednee()}")
    elif user == "4":
        del_us = int(input(""))
        delete(del_us)
    if user.lower() == "выход":
        print_report(expenses, summa())
        break
