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
expenses: list[float] = []


def print_report(exp: list[float], summ: float):
    print(f"Расходы:{exp}\nСумма:{summ}")


def add_expense(exp: list[float], value: float):
    exp.append(value)


def summa(exp: list[float]):
    return sum(exp)


def srednee(exp: list[float]):
    if len(exp) == 0:
        return 0
    return sum(exp) / len(exp)


def delete(exp: list[float], index: int):
    if 0 <= index < len(exp):
        del exp[index]
    else:
        print("Неверный номер расхода")


while True:
    for i in menu:
        print(i)
    user = input("")
    if user == "1":
        user_exp = float(input(""))
        add_expense(expenses,user_exp)
    elif user == "2":
        print(expenses)
    elif user == "3":
        print(f"Сумма: {summa(expenses)}")
        print(f"Среднее значение: {srednee(expenses)}")
    elif user == "4":
        del_us = int(input(""))
        delete(expenses,del_us - 1)
    elif user.lower() == "выход":
        print_report(expenses, summa(expenses))
        break
