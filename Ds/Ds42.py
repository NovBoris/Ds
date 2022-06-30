import math

import requests

d = {}

# def update_dictionary(d, key, value):
#     if len(d) == 0:
#         d[key * 2] = [value]
#     else:
#         if key in d:
#             d[key] += [value]
#         elif key * 2 in d:
#             d[key * 2] += [value]
#         else:
#             d[key * 2] = [value]
#
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}


# a = input().lower().split()
# for i in set(a):
#     print(i, a.count(i))

# n = int(input())
# list = {}
# while n + 1 != 0:
#     n -= 1
#     x = int(input())
#     if x not in list:
#         list[x] = f(x)
#         print(list[x])
#     else:
#         print(list[x])

# with open('TestFile_1.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)
#
# with open('TestFile_1.txt', 'w') as inf:
#     inf.write(
#         'Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.')

# list = []
# res = ''
# num = ''
#
# with open('dataset_3363_2.txt', 'r') as text:
#     for i in text:
#         i = i.strip()
#         list.append(i)
#
# x = []
# y = []
# res = ''
# numb = ''
# print(list[0])
# for a in range(len(list)):
#     for i in list[0]:
#         if i.isdigit():
#             numb += i
#         else:
#             x.append(i)
#             if numb != '':
#                 y.append(int(numb))
#                 numb = ''
#
# y.append(int(numb))
#
#
#
# print(res)
# print(x)
# print(y)
# num = 0
# for a in y:
#     print(a * x[num])
#     num += 1
#
#
#
# with open('dataset_3363_2.txt', 'w') as test:
#     num = 0
#     for a in y:
#         test.write(a * x[num])
#         num += 1

# res = []
# list = {}
# with open('dataset_3363_3.txt', 'r') as text:
#     for i in text:
#         i= i.lower().split()
#         for a in set(i):
#             if a not in list:
#                 list[a] = i.count(a)
#             else:
#                 list[a] += i.count(a)
#
# print(list)
#
#
# for i, a in list.items():
#     v = [i, a]
#     if len(res) == 0:
#         res.append(v)
#     else:
#         if res[0][1] < a:
#             res.clear()
#             res.append(v)
#         if res[0][1] == a:
#             if res[0][0] > i:
#                 res.clear()
#                 res.append(v)
#
# print(*res[0])
# with open('dataset_3363_3.txt', 'w') as text:
#     text.write(res)

# print(ord('a'), chr(88))


# a = 'b'
# b = 'aLebt'
#
# print(a > b)


# list = [[], [], [], []]
# with open('dataset_3363_3.txt', 'r', encoding='utf-8') as text:
#     for i in text:
#         i = i.replace('\n', '').split(';')
#         a, b, c, d = i
#         list[0].append(int(b))
#         list[1].append(int(c))
#         list[2].append(int(d))
#         q = ((int(b) + int(c) + int(d)) / 3)
#         if len(str(q)) > 9:
#             list[3].append(('%.9f' % q))
#         else:
#             list[3].append(str(q))
#
# print(list)
# res = ''
# a, b, c = str(sum(list[0]) / len(list[0])), str(sum(list[1]) / len(list[1])), str(sum(list[2]) / len(list[2]))
#
#
# if len(str(a)) > 12:
#     res += ('%.9f' % float(a)) + ' '
# else:
#     res += a + ' '
# if len(str(b)) > 12:
#     res += ('%.9f' % float(b)) + ' '
# else:
#     res += b + ' '
# if len(str(c)) > 12:
#     res += ('%.9f' % float(c))
# else:
#     res += c
#
#
# print(res)
#
# with open('dataset_3363_3.txt', 'w') as text:
#     for i in list[3]:
#         text.write(i + '\n')
#     text.write(res)

# s = 'r1013f3'
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(i, j)
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j

# s, d = input(), []
# for i in s:
#     if not i.isdigit(): d.append(i)
#     else: d[-1] += i
# print(d)
# print(*[i[0]*int(i[1:]) for i in d], sep='')

# s = input()
# maxc = 0
# s = s.lower().strip().split()
# print(s)
# s.sort()
# print(s)
# for word in s:
#     counter = s.count(word)
#     if counter > maxc:
#         maxc = counter
#         result_word = word

# a = int(input())
# print(2 * pi() * a)

# import sys
#
# print(sys.argv)
# s = ''
# s2 = ''
# for i in range(1, len(sys.argv)):
#     s = s + sys.argv[i]+' '
# s2 = s
# print(s2,end=' ')


# import requests
#
# link = 'https://stepic.org/media/attachments/course67/3.6.3/'
# with open('dataset_3378_3.txt') as inf:
#     l = inf.readline().strip()
#
# r = requests.get(l)
# r = link + r.text
#
# flag = True
# while(flag):
#     r = requests.get(r)
#     if (r.text.count('.txt')):
#         print(r.text) # Что бы было видно что консоль не просто висит
#         r = link + r.text
#     else:
#         flag = False
#         print(r.text)


a = int(input())
b, c, d, e = input().split(';')


