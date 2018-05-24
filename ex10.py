                            #ПЕРВОЕ РЕШЕНИЕ
num1 = int(input())
num2 = int(input())
num3 = int(input())
maxN = num1
minN = num2
remain = num3
if maxN >= num2 and maxN >= num3:
    print(maxN)
elif num2 >= num3:
    maxN = num2
    print(maxN)
elif num3 >= num2:
    maxN = num3
    print(maxN)

if minN <= num1 and minN <= num3:
    print(minN)
elif num1 <= num3:
    minN = num1
    print(minN)
elif num3 <= num1:
    minN = num3
    print(minN)

if num1 <= remain <= num2 or num2 <= remain <= num1:
    print(remain)
elif remain <= num1 and remain <= num2 and num1 >= num2:
    remain = num2
    print(remain)
elif remain <= num1 and remain <= num2 and num2 >= num1:
    remain = num1
    print(remain)
elif remain >= num1 and remain >= num2 and num1 >= num2:
    remain = num1
    print(remain)
elif remain >= num1 and remain >= num2 and num2 >= num1:
    remain = num2
    print(remain)
                    #ВТОРОЕ РЕШЕНИЕ
a,b,c = int(input()), int(input()), int(input())
if a < b:
	a, b = b, a
if a < c:
	a, c = c, a
if b > c:
	b, c = c, b
print(a, b, c, sep="\n")