with open('C:\\Users\\Max\\Desktop\\dataset_3363_4.txt', 'r') as ds:
    lst = []
    for line in ds:
        s = line.strip().split(';')
        lst.append(s)
for row in lst:
    for j in range(len(row)):
        if row[j].isdigit() == True:
            row[j] = int(row[j])
[print((mathematics + physics + rusLang) / 3) for secondName, mathematics, physics, rusLang in lst]
midMathematics = []
midPhysics = []
midRusLang = []
for secondName, mathematics, physics, rusLang in lst:
    midMathematics.append(mathematics)
    midPhysics.append(physics)
    midRusLang.append(rusLang)
print(sum(midMathematics) / len(lst), sum(midPhysics) / len(lst), sum(midRusLang) / len(lst), sep=' ')
