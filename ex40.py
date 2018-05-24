        #Футбол(1. ввод числа матчей. 2.формат ввода: команда;голов;команда;голов)
matches = [[j for j in input().split(';')]for i in range(int(input()))]
statistics = {matches[match][command]:[0] * 5 for command in (0, 2) for match in range(len(matches))}
for commandOne, goalsOne, commandTwo, goalsTwo in matches:
    statistics[commandOne][0] += 1
    statistics[commandTwo][0] += 1
    if goalsOne > goalsTwo:
        statistics[commandOne][1] += 1
        statistics[commandOne][4] += 3
        statistics[commandTwo][3] += 1
    elif goalsOne < goalsTwo:
        statistics[commandTwo][1] += 1
        statistics[commandTwo][4] += 3
        statistics[commandOne][3] += 1
    else:
        statistics[commandOne][2] += 1
        statistics[commandOne][4] += 1
        statistics[commandTwo][2] += 1
        statistics[commandTwo][4] += 1
[print(key + ':', *value) for key, value in statistics.items()]


		#2 try(optimized)
n = int(input())
matches = [[j for j in input().split(';')]for i in range(n)]
statistics = {matches[match][command]:[0] * 5 for command in (0, 2) for match in range(n)}
for commandOne, goalsOne, commandTwo, goalsTwo in matches:
    statistics[commandOne][0] += 1
    statistics[commandTwo][0] += 1
    if goalsOne > goalsTwo:
        statistics[commandOne][1] += 1
        statistics[commandOne][4] += 3
        statistics[commandTwo][3] += 1
    elif goalsOne < goalsTwo:
        statistics[commandTwo][1] += 1
        statistics[commandTwo][4] += 3
        statistics[commandOne][3] += 1
    else:
        statistics[commandOne][2] += 1
        statistics[commandOne][4] += 1
        statistics[commandTwo][2] += 1
        statistics[commandTwo][4] += 1
[print(key + ':', *value) for key, value in statistics.items()]


