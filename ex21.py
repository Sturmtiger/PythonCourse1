a = [int(i) for i in input().split()]
i = 0
while i < len(a):
    if len(a) > 1:
        print(a[i-1] + a[i+1-len(a)], end=" ")
    else:
        print(a[0])
    i += 1