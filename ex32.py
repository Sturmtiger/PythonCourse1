def f(x): #проверочная функция
    return x * 100
#
                    # 1 try
# n = [int(input()) for i in range(int(input()))]
# d = dict()
# for i in n:
#     if d.get(i) == None:
#         d[i] = f(i)
# for i in n:
#     print(d[i])
                    # 2 optimized

n = [int(input()) for i in range(int(input()))]
b = {x : f(x) for x in set(n)}
print (*[b[i] for i in n], sep='\n')