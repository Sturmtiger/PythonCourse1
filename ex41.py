#    # 1st way(zip)

# a, b, c, d = [input() for i in range(4)]
# a, b, c, d = ['abcd', '*d%#', 'abacabadaba', '#*%*d*%'] # test
# cipher = dict(zip(a, b))
# newC = ''
# for i in c:
#     newC += cipher[i]
# newD = ''
# for j in d: # с помощью данного цикла узнаем нужный ключ от значения
#     for k, v in cipher.items():
#         if v == j:
#             newD += k
#             break
# print(newC, newD, sep='\n')



#     #2nd way(zip) THE BEST SOLUTION

a, b, c, d = [input() for i in range(4)]
cipher, cipherRev = dict(zip(a, b)), dict(zip(b, a))
newC, newD = '', ''
for i in c:
    newC += cipher[i]
for j in d:
    newD += cipherRev[j]
print(newC, newD, sep='\n')



#    #3rd way

# a, b, c, d = [input() for i in range(4)]
# newC, newD = '', ''
# i = 0
# while i < len(c):
#     newC += b[a.find(c[i])]
#     i += 1
# j = 0
# while j < len(d):
#     newD += a[b.find(d[j])]
#     j += 1
# print(newC, newD, sep='\n')



#    # :D просто от нечего делать. Это непрактично

# a, b, c, d = [input() for i in range(4)]
# cipher, cipherRev = dict(zip(a, b)), dict(zip(b, a))
# [print(cipher[i], end='') for i in c]
# print()
# [print(cipherRev[j], end='') for j in d]


