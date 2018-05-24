a = int(input("Рекоменд.:")) #6
b = int(input("Пересып:")) # 10
h = int(input("Ваше время:"))
if b >= h >= a:
    print("Это нормально")
elif a > h:
    print("Недосып")
else:
    print("Пересып")