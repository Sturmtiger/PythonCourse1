with open('C:\\Users\\Max\\Desktop\\dataset_3380_5.txt', 'r') as dataset:
    growthLines =[[int(line.split()[0]), int(line.split()[2])] for line in dataset.readlines()]
    growthDict = {i: 0 for i in range(1, max(a[0] for a in growthLines)+1)}
    for group, growth in growthLines:
        growthDict[group] += growth / list(zip(*growthLines))[0].count(group)
    for k, v in growthDict.items():
        if v == 0:
            print(k, '-')
        else:
            print(k, v)
# Вот и всё. Конец первого курса..
