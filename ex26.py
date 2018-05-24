#     #1 var
# lst = input()
# a = []
# while lst != 'end':
#     a.append([int(i) for i in lst.split()])
#     lst = input()
# b = [[0 for j in range(len(a[i]))] for i in range(len(a))]
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         b[i][j] = a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1]
#         j += 1
#     i += 1
# for i in range(len(b)):
#     print(*b[i])


    #2 var
a = []
while True:
    lst = input().split()
    if lst == ["end"]:
        break
    a.append(lst)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(int(a[i - 1][j]) + int(a[i - len(a) + 1][j]) + int(a[i][j - 1]) + int(a[i][j - len(a[i]) + 1]), end=" ")
    print()