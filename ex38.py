from requests import get
url = open('C:\\Users\\Max\\Desktop\\dataset_3378_3.txt').read().strip()
print(len(get(url).text.splitlines()))
