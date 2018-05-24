                #1
a, b = (int(input()) for i in range(2))
while True:
    if a % 3 != 0:
        a+=1
    else:
        break
c = 0
t = 0
for i in range(a, b+1, 3):
    c += i
    t += 1
print(c/t)
                #2
# a,b = int(input()), int(input())
# a += -a%3
# b -= b%3
# print((a+b)/2)
