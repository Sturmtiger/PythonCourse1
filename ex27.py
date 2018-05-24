#     # 1 try
# n = int(input())
# a = [[0 for j in range(n)] for i in range(n)]
# num = 1
# k = 0
# while k < n:
#     for i in range(n):
#         if a[k][i] == 0:
#             a[k][i] = num
#             num += 1
#     if num > n ** 2:
#         break
#     for j in range(n):
#         if a[j][n - 1 - k] == 0:
#             a[j][n - 1 - k] = num
#             num += 1
#     if num > n ** 2:
#         break
#     for r in range(n):
#         if a[j - k][-(r + 1)] == 0:
#             a[j - k][-(r + 1)] = num
#             num += 1
#     if num > n ** 2:
#         break
#     for h in range(n):
#         if a[-(h + 1)][k] == 0:
#             a[-(h + 1)][k] = num
#             num += 1
#     if num > n ** 2:
#         break
#     k += 1
# for i in range(n):
#     print(*a[i])


    # 2 try
n = int(input())
m = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1
for k in range(n ** 2):
    m[i][j] = k + 1
    if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
        di, dj = dj, -di
    i, j = i + di, j + dj
[print(*i) for i in m]
