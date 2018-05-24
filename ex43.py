#   # 1 try
# outputCoordinates = [0, 0] #восток(-запад), север(-юг)
# for i in range(int(input())):
#     route = input().split()
#     if route[0] == 'восток':
#         outputCoordinates[0] += int(route[1])
#     elif route[0] == 'север':
#         outputCoordinates[1] += int(route[1])
#     elif route[0] == 'запад':
#         outputCoordinates[0] -= int(route[1])
#     elif route[0] == 'юг':
#         outputCoordinates[1] -= int(route[1])
# print(*outputCoordinates)




#   # 2 try(the Best)
# coords = {'восток': 0, 'запад': 0, 'север': 0, 'юг': 0}
# for i in range(int(input())):
#   route = input().split()
#   coords[route[0]] += int(route[1])
# print(coords['восток'] - coords['запад'], coords['север'] - coords['юг'])