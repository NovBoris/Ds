# print(1,2,3,4,5,6,7,8,9, sep=' - ')
# print(1,2,3,4,5,6,7,8,9, sep=' - ', end=' = ')
# print(1,2,3,4,5,6,7,8,9, sep=' - ')
# print(1,2,3,4,5,6,7,8,9, sep='-')

# -------------------------------------------------------------------------------------------------

# with open('TestFile_1.txt', "w") as f:
#     print('Write to file', file = f)
#
# with open("TestFile_1.txt", "a") as F:
#     print("Now it will be recorded after", file = F)


# -------------------------------------------------------------------------------------------------

# file = open("test.txt", "w")
# file.close()
# file = open(r"C:\Users\User\Desktop\Code\TestFile_2.txt", "w")
# file.close()
#
# f = open(r"C:\Users\User\Desktop\Code\TestFile_2.txt", "w")
# print(f.mode)
# print(f.name)
# f.write('Привет Файл\n' * 23)
# f.write('Пока Файл\n' * 23)
# f.close()
# f = open(r"C:\Users\User\Desktop\Code\TestFile_2.txt", "a")
# print(f.mode)
# print(f.name)
# f.write('Привет Файл\n' * 23)
# f.write('Пока Файл\n' * 23)
# f.close()

# --------------------------------------------------------------------------

# A = open('test.txt', 'wb')
# A.write(bytes('строка', 'utf8'))
# A.close()

# --------------------------------------------------------------------------

# try:
#     file = open("TestFile_1.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print('Not found')
# except IOError:
#     print('Something else')

# --------------------------------------------------------------------------

# try:
#     f = open("test.txt", "rb")
#     b = f.read(1)
#     str = ""
#     while True:
#         b = f.read(1)
#         if b == b'':
#             break
#         str += b.hex()
#     print(str)
#     f.close()
# except IOError:
#     print('error')

# ------------------------------------------------------------

# A = open("TestFile_2.txt", "w")
# A.write("Test file 2")
# A.close()

# with open("TestFile_1.txt", 'r') as A:
#     print(A.read())

# import time
# import sys
#
# for i in range(5):
#     print (i),
#     sys.stdout.flush()
#     time.sleep(1)

#---------------------------------------------------------------------

# A = [1,2,3,4,5,6,7,8,9,0]
# print(A)
# A = tuple([1,2,3,4,5])
# print(A)
# print(A[-2])
#
#---------------------------------------------------------------------

# a = tuple(i for i in range(0,10))
# print(a,'\n')
#
# data = [i for i in range(0, 10) if i % 2 == 0]
#
# data = [i * j for i in range(0, 3) for j in range(0, 3)]
# print(data,'\n')
#
# data = [[0 for x in range(2)] for y in range(3)]
# print(data)
# print()
# data = [(lambda i: i*i)(i) for i in range(0, 10)]
# print(data)

#---------------------------------------------------------------------

# A = 5
# B = 10
# print()
# C = [(lambda i: B/A)(i) for i in range (0,10)]
# print(C)
# import itertools
#
# data = [i for i in itertools.repeat(1, 5)]
# print(data)
#
# b = (5, 3.6, "квадрат", 15, 'В')
# print(b[1])
# print(b[2:4])
#
# a = (32, 33, 34, 33, 34, 33)
# print(a.index(33))
#
# a = (32, 33, 34, 33, 34, 33)
# print(a.count(33))

#---------------------------------------------------------------------

# import collections
# from collections import  namedtuple
# Flower = namedtuple('Flower', 'color cost comment')
# rose = Flower('red', 5, 'beautiful')
# print(rose.cost)
# print(rose.color)
# print(rose.comment)
# print(rose[0])

#---------------------------------------------------------------------

# a = [(1,2,3),(4,5,6)]
#
# a = ('One', 'Two', 'Three')
# a = tuple(sorted(a))
# print(a)
#
# a = (3, 1, 5 ,2, 6, 7)
# a = tuple(sorted(a))
# print(a)
#
# a = (1,2,3)
# a = list(a)
# print(a)
#
# a = [1, 2.6, "квадрат"]
# a = tuple(a)
# print(a)
#
# a = (('a', 2),('b', 4))
# a = dict(a)
# print(a)
#
# a = ('one','two','three')
# b = ''.join(a)
# c = ','.join(a)
# print(b)
# print(c)

#---------------------------------------------------------------------

# print('\nЧто будет c %2d и что будет с %3.2f' % (4, 123.1241241))
#
# print(('{0}, будет праздновать свой {1} день рождения в {2}'
#        .format('Борис', '25', '2025 году')))
#
# print('Я вешу {m:2.2f} и я родился в {a:4d}'
#       .format(m = 80.12412, a = 1999))
#
# data = dict(name ="Бендер", race ="Робот")
# print("Это {name}, он - {race}".format(**data))

#---------------------------------------------------------------------

# string = "text"
# newString = "%+10s" % string
# print(newString)


#---------------------------------------------------------------------

# try:
#     for i in range(4):
#         if (i == 3):
#             i = text
#         print(f"Попытка {i} прошла успешно")
# except Exception as err:
#     print("Возникла ошибка: \"{}\"".format(err))

# ---------------------------------------------------------------------

# a = ['python', 3, 'лучший', 'язык', 'программирования']
# for val in a:
#     print(val, end=' ')


#---------------------------------------------------------------------



# from array import *
# arr = array('i', [1,3,6,2,5])
# for i in range(len(arr)):
#     print("%d-й элемент массива = %d" %(i, arr[i]))

#---------------------------------------------------------------------


# a = {1: "one", 2: "two", 3: "three"}
# for key, value in a.items():
#   print("{0}: {1}".format(key,value))
#
#   arr = {"Один": "one", "Два": "two", "Три": "three"}
#   print(" _________________ ")
#   print("|  Rus   :  Eng   |")
#   print("|-----------------|")
#   for key, value in arr.items():
#       print("|  {r:5s} :  {w:5s} |".format(r=key, w=value))
#   print("|-----------------|")


#---------------------------------------------------------------------

# mtx = [[  2, 4, 12],
#        [ -6, 3,  9],
#        [334, 0, 11]]
# print(mtx)
# for row in mtx:
#     for x in row:
#         print("%3d" %(x), end = " ")
#     print()

#---------------------------------------------------------------------

# import os
# sayt = input()
# if 'https://' in sayt:
#     os.system('start ' + sayt)
#     print('Сайт')
# import random

#---------------------------------------------------------------------

# print(random.choice('sequence'))
