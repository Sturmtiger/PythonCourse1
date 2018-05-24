    # Solution
from requests import get
url = open('C:\\Users\\Max\\Desktop\\dataset_3378_3.txt').read().strip()
link = 'https://stepic.org/media/attachments/course67/3.6.3/'
f1 = get((link + get(url).text)).text
while not 'We' in f1:
    f1 = get(link + f1).text
print(f1)




    #Балуюсь
# from requests import get
# url = open('C:\\Users\\Max\\Desktop\\dataset_3378_3.txt').read().strip()
# f1 = get(('https://stepic.org/media/attachments/course67/3.6.3/' + get(url).text)).text
# while not 'We' in f1:
#     f1 = get('https://stepic.org/media/attachments/course67/3.6.3/' + f1).text
# print(f1)