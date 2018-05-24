a = []
while True:
    a.append(int(input()))
    if sum(a) == 0:
        print(sum(i ** 2 for i in a))
        break



