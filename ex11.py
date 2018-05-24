                    #ПЕРВОЕ РЕШЕНИЕ
# count = int(input())
# if (count % 10 == 5) or (count % 10 == 5) or (count % 10 == 6) or (count % 10 == 7) or (count % 10 == 8) or (count % 10 == 9) or (count % 10 == 0) and (count % 10 != 1):
#     print(count, "программистов")
# elif (count % 100 == 11) or (count % 100 == 12) or (count % 100 == 13) or (count % 100 == 14) or (count % 100 == 15) or (count % 100 == 16) or (count % 100 == 17) or (count % 100 == 18) or (count % 100 == 19):
#     print(count, "программистов")
# elif (count % 10 == 1) and (count % 100 != 11):
#     print(count, "программист")
# elif (count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4):
#     print( count, "программиста")
                    #ВТОРОЕ РЕШЕНИЕ
count = int(input())
print(count,'программист'+('ов' if count%10==0 or 4<count%10<10 or 10<count%100<15 else 'а' if 1<count%10<5 else ''))