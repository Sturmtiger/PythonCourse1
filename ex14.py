            #1
a = int(input())
b = int(input())
if a == b:
    print(a)
elif a > b:
    count = a
    while True:
        if count % b != 0:
            count += a
        else:
            print(count)
            break
elif a < b:
    count = b
    while True:
        if count % a != 0:
            count += b
        else:
            print(count)
            break
            #2
# a = int(input())
# b = int(input())
# d = a # или max = a if a > b else b
# while d%b:
#     d += a
# print(d)