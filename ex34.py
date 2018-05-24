#     #1 try
# with open('C:\\Users\\Max\\Desktop\\asas.txt', 'r') as asas:
#     s = asas.read().strip().lower().replace(',' and '.', '').split()
# d = {i : s.count(i) for i in s}
# ks = []
# vs = []
# cnt = []
# for key, value in d.items():
#     ks.append(key)
#     vs.append(value)
# for i in range(vs.count(max(vs))):
#     cnt.append(vs.index(max(vs)))
#     vs[vs.index(max(vs))] = 0
# ans = ks[cnt[0]]
# for i in cnt:
#     if ks[i] < ans:
#         ans = ks[i]
# m = ans + ' ' + str(max(d.values()))
# with open('C:\\Users\\Max\\Desktop\\out.txt', 'w') as out:
#     out.write(m)



with open('C:\\Users\\Max\\Desktop\\asas.txt', 'r') as file:
    s = file.read().strip().lower().split()
z = {i: s.count(i) for i in s}

maximum = max(z, key=z.get)
print(z[maximum])
x = {maximum: z[maximum]}

print(x)