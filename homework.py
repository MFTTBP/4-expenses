"""
#Мое дз
#"""
a = input("").lower().strip()
b = a.strip().split()


if len(b) < 2 or len(b) > 4:
    print("Некорректный формат суммы")
elif not b[0]:
    print("Некорректный формат суммы")
elif str(b[0]).startswith("00"):
    print("Некорректный формат суммы")
elif b[1] != "руб":
    print("Некорректный формат суммы")
elif len(b) == 4 and b[3] != "коп":
    print("Некорректный формат суммы")
elif len(b) == 2 and not b[0].isdigit():
    print("Некорректный формат суммы")
elif len(b) == 4 and not b[2].isdigit():
    print("Некорректный формат суммы")
elif len(b) == 4 and int(b[2]) > 99:
    print("Некорректный формат суммы")
elif len(b) == 2:
    print(f"{b[0]}.00 ₽")
else:
    print(f"{b[0]}.{b[2].zfill(2)} ₽")