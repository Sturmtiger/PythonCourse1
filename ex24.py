n = int(input())
i = 1
st = []
while i <= n:
    for j in range(i):
        st += [i]
        if len(st) == n:
            i = n
            break
    i += 1
print(*st)