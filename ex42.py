#     #1 try
# vocabulary, words, unitedWords = [input().lower() for i in range(int(input()))], [input().lower().split() for i in range(int(input()))], []
# for i in words:
#     unitedWords += i
# for i in set(unitedWords):
#         if not i in vocabulary:
#             print(i)




#    #2 try
# vocabulary, lines = {input().lower() for i in range(int(input()))}, set()
# [[lines.add(j) for j in input().lower().split()] for i in range(int(input()))]
# print('\n'.join(lines - vocabulary))




#   # 3 try(THE BEST SOLUTION)
def generate(n):
    s = set()
    [[s.add(j) for j in input().lower().split()] for i in range(n)]
    return s
vocabulary, lines = generate(int(input())), generate(int(input()))
print('\n'.join(lines - vocabulary))




# #   # 4 try
# vocabulary, words = {input().lower() for i in range(int(input()))}, [input().lower().split() for i in range(int(input()))]
# unitedWords = {i for c in words for i in c}
# print('\n'.join(unitedWords - vocabulary))