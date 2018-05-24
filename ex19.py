                            #1
a = input()
st = ""
i = 1
while i < len(a):
    count = 1
    while i < len(a) and a[i] == a[i-1]:
        count += 1
        i += 1
    st += a[i-1] + str(count)
    i += 1
print(st)

                            #2
# string = input()
# count = 0
# current = string[0]
#
# for i in string:
#     if i == current:
#         count += 1
#     else:
#         print(current + str(count), end = '')
#         count = 1
#         current = i
# print(current + str(count))
