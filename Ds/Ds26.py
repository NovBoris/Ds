# a = [-1, 0, 5, 3, 2]
# print([i + 7.2 for i in a])

# a = input().split()
# print(sorted(a + a))

# mtx1 = [[1, 2], [3, 4], [5, 6]]
# mtx2 = [[1, 0], [0, 1], [1, 1]]
# total = [[0, 0], [0, 0], [0, 0]]
# for i in range(len(mtx1)):
#     for j in range(len(mtx1[0])):
#         total[i][j] = mtx1[i][j]+mtx2[i][j]
# for k in total:
#     print(k)

# a = input()
# print(a.count('5'))

# a = [1,2,3,4,5]
# b = list(a)
# a.append(124124)
# print(a, b)

# a = 1
# list = []
# while a != 0:
#     a = int(input())
#     if a != 0:
#         list.append(a**2)
# print(list)

# b = ['+72354235', '+22354235', '+52354235', '+72354235', '+72354235']
# a = b.copy()
# for i in a:
#     print(i)
#     if '+7' in i:
#         b.remove(i)
# print(b)
# a = ['+7912123456', '+7915213456', '+6915213456', '+4915213456', '+7915213456']
# print([i for i in a if '+7' not in i])

# lst = [1, 2, 3, 4, 5, 6]
# print([lst[-1]] + lst[0:-1])
# print(lst)

# a = list(input())
# print(a[1:] + [a[0]])
# print(a)

# a = [1,2,3,4,5,6]
# print(a)
# b =[]
# for i in a:
#     b.append(i)
# b.pop(0)
# b.append(a[0])
# print(b)
#
# a = [1,2,3,4,5,6]
# print(a)
# b =[]
# b.append(a[-1])
# a.pop()
# for i in a:
#     b.append(i)
# print(b)

# lst = [1, 2, 3, 4, 5, 6]
# lst.insert(0,lst.pop(-1)) # вырезаем последний элемент и вставляем в начало
# print(lst)
# N = 10
# list = [x ** 2 for x in range(N) if x % 2 == 0]
# print(list[::-1])

# a = [1,5,3,4,6,8,1,23,4,56,53]
# a.sort()
# print(a)
# n = len(a)
# for i in range(n - 1):
#     for b in range(i + 1, n):
#         if a[i] > a[b]:
#             a[i], a[b] = a[b], a[i]
# print(a)

# a = input().split()
# a = ([i for i in a if int(i) % 2 == 0])
# c = []
# for b in a:
#     c.append([int(b), int(b) ** 2])
# c = dict(c)
# print(c)
# print(c[4])

# d = {}
# for n in input("Введите числa через запятую: ").split():
#     n = int(n)
#     if n % 2 == 0:
#         d.setdefault(n, n ** 2)
#
# print(d)

# string = "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
# string = dict(string)
# print(string)

# string = "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип"
# my_dict = dict([n.replace("=", ",").split(",") for n in string.split(", ")])
# print(my_dict)
#
# string = 'int = целое число, dict = словарь, list = список, bool = булевый тип'
# print(dict(([i.split(' = ') for i in string.split(',')])))
#
# input = input('введите так: английское слово: перевод1, перевод2, перевод3: ')
# print(dict([[input.split(':')[0], input.split(':')[1:]]]))

# a = input()
# b = ''
# res = 0
# for i in a.lower():
#     if a.lower().count(i) > 1:
#         b += i
#         a = a.lower().replace(i, '')
#         res += 1
# print(res)

# text = input()
# print(set(text))
# count = 0
# for c in set(text.lower()):
#     if text.lower().count(c) > 1:
#         count += 1
# print(count)

# pin = input()
# print(pin.isdigit() if len(pin) in (4,6) else False)

# import math
# a, b, c = 8, 9, -2
# a, b, c = sorted([a, b, c])
# print(a)
# p = ((a+b+c)/2)
# try:
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(True if s > 0 and a > 0 and b > 0 and c > 0 else False)
# except ValueError:
#     print(False)

# a = input()
# lenr = len(a) / 2
# if len(a) % 2 == 0:
#     print(a[int(lenr)-1] + a[int(lenr)])
# else:
#     print(a[math.floor(lenr)])
# import math
#
# n = 3
# if n >= 0:
#     a = math.sqrt(n).__floor__()
#     if a ** 2 == n:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# s1 = 'loopingisfunbutdangerous'
# s2 = 'lessdangerousthancoding'
# s = s1 + s2

# a = [1,1,1,1]
# res = 1
# for i in a:
#     if i == 0:
#         res *= 2
#     else:
#         res = (res * 2) + 1
# print(res)

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []
# for item in old_list:
#     new_list.append(int(item))
# print (new_list)
# new_list = list(map(int, old_list))
# print(new_list)
#
# def miles_to_kilometers(num_miles):
#     return num_miles * 1.6
#
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(miles_to_kilometers, mile_distances))
# print (kilometer_distances)

# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
# print (kilometer_distances)
#
# mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
# zolushka = list(filter(lambda x: x == 'мак', mixed))
# print (zolushka)

# words = ['aabb', 'abcd', 'bbaa', 'dada']
# word = 'abba'
# print(len(''.join(sorted(word))))
# list = []
# for i in words:
#     print(len(''.join(sorted(i))))
#     if (''.join(sorted(i))) in (''.join(sorted(word))) and len((''.join(sorted(i)))) == (len(''.join(sorted(word)))):
#         list.append(i)
# print(list)
# print(list(filter(lambda x: sorted(word) == sorted(x), words)))

# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = []
#
# for a in a1:
#     for b in a2:
#         if a in b:
#             r.append(a)
# print(list(sorted(set(r))))