"""
Мое дз
"""


a = input("").lower().strip()
b = a.split(" ")
c = False if b[0].isdigit() else True


if len(b) > 4 or len(b) < 2 or c:
    print("Некорректный формат суммы")
elif len(b) != 2 and len(b) != 4:
    print("Некорректный формат суммы")
elif b[1] != "руб":
    print("Некорректный формат суммы")
elif len(b) == 4 and b[3] != "коп":
    print("Некорректный формат суммы")
elif len(b) == 2:
    print(f"{b[0]}.00 ₽")
elif not b[2].isdigit():
    print("Некорректный формат суммы")
elif len(b) == 4 and len(b[2]) < 2:
    print(f"{b[0]}.{b[2].zfill(2)} ₽")
else:
    print(f"{b[0]}.{b[2]} ₽")
