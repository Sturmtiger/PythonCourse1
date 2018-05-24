                # test by input
# st = input() # a2b10f1
# i = 0
# l = []
# s = []
# while i < len(st):
#     cnt = ''
#     while '0' <= st[i] <= '9':
#         cnt += st[i]
#         i += 1
#         if i == len(st):
#             break
#     else:
#         l.append(st[i])
#     i += 1
#     if cnt != '':
#         s.append(cnt)
# j = 0
# while j < len(s):
#     print(l[j] * int(s[j]), end='') # aabbbbbbbbbbf
#     j += 1

                # solution
with open('C:/Users/Max/Desktop/lel.txt', 'r') as lel:
    st = lel.readline().strip()
i = 0
l = []
s = []
while i < len(st):
    cnt = ''
    while '0' <= st[i] <= '9':
        cnt += st[i]
        i += 1
        if i == len(st):
            break
    else:
        l.append(st[i])
    i += 1
    if cnt != '':
        s.append(cnt)
j = 0
out = ''
while j < len(s):
    out += l[j] * int(s[j] )
    j += 1
with open('C:/Users/Max/Desktop/kek.txt', 'w') as kek:
    kek.write(out)