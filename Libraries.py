# # Стандартная библиотека sys
# import sys
# print(sys.argv) # !список(list)! аргументов строки, по-умолч. самый первый - имя вызываемого файла



# # Стандартная библиотека subprocess
# import subprocess
# subprocess.call(['py', '-m', 'pip']) #вызовет справку о менеджере пакетов ‘pip’ у нас в программе


# # Библиотека requests
# import requests
#
# r = requests.get('http://example.com') # простой GET запрос
# print(r.text) # вывод ответа от сервера
#
#
# url = 'http://example.com'
# par = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=par) # Передача параметров в GET запрос
# print(r.url) # Сформированный url-адрес с учётом параметров GET запроса(http://example.com/?key1=value1&key2=value2)
#
#
# url = 'http://httpbin.org/cookies'
# cookies = {'cookies_are': 'working'}
# r = requests.get(url, cookies=cookies) # отправка сформированных cookies на сервер
# print(r.text)
#
#
# print(r.cookies['example_cookie_name']) # использование cookies, полученных от сервера



# # Библиотека NumPy
# from numpy import *
# a = array([2, 3, 4])
# b = array([(2.4, 4, 5), (5, 5, 6)])
# print(b)
# print(b.ndim, 'row') #размерность массива(Одномерный, двумерный и т.д.)
# print(b.shape, 'row, col') #кол-во строк и столбцов
# print(b.size, 'elements') # кол-во элементов
#
# z = zeros((3, 3)) #row, col(массив заполненный нулями)
# print(z)
#
# c = arange(10, 30, 5) #генератор списка, не включая 30 с шагом 5
# print(c)
#
# d = linspace(0, 2, 9) # генерирует 9 чисел на отрезке от 0 до 2 с равным шагом
# print(d)
#
# e = arange(12).reshape(4, 3) # от 0 до 12(не вкл.).row 4/col 3
# print(e)
#
# print(a + b) # арифм. операции на массивах выполняются поэлементно
# print(a - b)
# print(a ** 2)
# print(2 * sin(a))
# print(a < 20)



# # Библиотека matplotlib(модуль pylab)
# from pylab import *
# x = linspace(0, 5, 10)
# y = x ** 2
# print(x)
# print(y)
#
# %matplotlib inline
# figure() # построение графика
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
# show()
#


