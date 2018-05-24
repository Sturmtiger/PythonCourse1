room = input()
if room == "треугольник":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif room == "прямоугольник":
    a = int(input("a: "))
    b = int(input("b: "))
    S = a * b
    print(S)
elif room == "круг":
    r = int(input("r: "))
    S = 3.14 * (r ** 2)
    print(S)
