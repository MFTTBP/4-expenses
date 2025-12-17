"""
Мое дз
"""


a = input("")
b = a.split(" ")

if len(b) > 4 or len(b) < 2:
    print("Некорректный формат суммы")
elif len(b) == 2:
    print(f"{b[0]}.00 ₽")
elif len(b) == 4 and len(b[2]) < 2:
    print(f"{b[0]}.{b[2].zfill(2)} ₽")
else:
    print(f"{b[0]}.{b[2]} ₽")