"""
Мое дз
"""
a = input("").lower().strip()
b = a.split(" ")
c = False if b[0].isdigit() else True

if len(b) != 2 and len(b) != 4:
    print("Некорректный формат суммы1")
elif str(b[0]).startswith("00"):
    print("Некорректный формат суммы2")
elif b[1] != "руб":
    print("Некорректный формат суммы3")
elif len(b) == 4 and b[3] != "коп":
    print("Некорректный формат суммы4")
elif c:
    print("Некорректный формат суммы5")
elif len(b) == 4 and b[2].isdigit() is False:
    print("Некорректный формат суммы6")
elif len(b) == 4 and int(b[2]) > 99 and int(b[2]) < 0:
    print("Некорректный формат суммы7")
elif len(b) == 2:
    print(f"{b[0]}.00 ₽")
else:
    print(f"{b[0]}.{b[2].zfill(2)} ₽")
