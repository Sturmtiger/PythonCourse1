a = float(input())
b = float(input())
c = input()
if (c == "/" or c == "div" or c == "mod") and (b == 0.0):
    print("Деление на 0!")
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "div":
    print(a // b)
elif c == "mod":
    print(a % b)
elif c == "pow":
    print(a ** b)