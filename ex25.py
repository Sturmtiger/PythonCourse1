lst = [int(i) for i in input().split()]
x = int(input())
if not x in lst:
    print("Отсутствует")
else:
    i = 0
    while i < len(lst):
        if x == lst[i]:
            print(i, end=" ")
        i += 1
