def modify_list(l):
    for i in range(len(l) - 1, 0 - 1, -1):
        if l[i] % 2 != 0:
            del l[i]
    for i in range(len(l)):
        l[i] = l[i] // 2
