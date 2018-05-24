                    #1 С помощью словаря
# l = [i.lower() for i in input().split()]
# d = dict()
# while l != []:
#     for i in l:
#         d[i] = l.count(i)
#         for j in range(l.count(i)):
#             l.remove(i)
# for key, value in d.items():
#     print(key, value)

                    #2 С помощью словаря(оптим.)
l = [i.lower() for i in input().split()]
d = {i : l.count(i) for i in set(l)} # или in set(l), что по идее сократить алгоритм выполнения
for key, value in d.items():
    print(key, value)

                    #3 Короткий метод(без словаря)
# l = input().lower().split()
# for i in set(l):
#     print(i, l.count(i))