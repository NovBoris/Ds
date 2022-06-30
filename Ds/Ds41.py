# a = input()
# res = 0
# for i in a:
#     if i.lower() == 'g' or i.lower() == 'c':
#         res += 1
# print((res / len(a)) * 100)

# s = 'abcdefghijk'
# print(s[-1:-10:-2])
#
# a = input()
# b = a[0]
# res = ''
# for i in a + ' ':
#     if i not in b:
#         res = res + b[0] + str(len(b) - 1)
#         b = i
#         print(b)
#     b += i
# print(res)
#
# a = ['dsvsdv', 'sdvsdvsd']
# a += 'ascasc'
# print(a)

# a = [1, 2, 3]
# b = a
# # значения списка b?
# print(b)
# a[1] = 10
# # значения списка b?
# print(b)
# b[0] = 20
# # значения списка a?
# print(b)
# a = [5, 6]
# print(a)
# print(b)

# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if len(a) == 1:
#         print(i)
#     elif b == len(a) - 1:
#         print(a[b - 1] + a[0])
#     else:
#         print(a[b - 1] + a[b + 1], end=' ')
#     b += 1

# print((4 + 1) % 5)


# a = input().split()
# a.sort()
# b = []
# for i in a:
#     if a.count(i) != 1 and b.count(i) == 0:
#         b.append(i)
# print(' '.join(b))

# n = 3
# a =[[0] * n] * n
# a[0][0] = 5
# print(a)
#
# a = [[0] * n for i in range(3)]
# a[0][0] = 5
# print(a)
#
# a = [[0 for j in range(n)] for i in range(3)]
# print(a)


# a = [1, 2, 3, 4, 5, 6]
# print(min(a))
# b = a[0]
# for i in a:
#     if i < b:
#         b = i
# print(b)


# n = 5
# b = 5
#
#
# def pole(n, b, simp):
#     a = [[simp for i in range(n)] for c in range(b)]
#     for i in range(len(a) - 1):
#         print(*a[i])
#
# pole(n, b, 0)

# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1

# a = int(input())
# sum = a
# sum_2 = a ** 2
# while sum != 0:
#     a = int(input())
#     sum += a
#     sum_2 = sum_2 + a ** 2
# print(sum_2)

# n = int(input())
# res = []
# for i in range(n + 1):
#     for b in range(i):
#         res.append(i)
#         if len(res) == n:
#             break
#     if len(res) == n:
#         break
# print(*res)

# a = [int(i) for i in input().split()]
# x = int(input())
# n = 0
# res = 0
# for i in a:
#     if i == x:
#         print(n, end=' ')
#         res = 1
#     n += 1
# if res == 0:
#     print('Отсутствует')

# a = input()
# f = []
# while a != 'end':
#     a = list(map(int, a.split()))
#     f.append(a)
#     a = input()
# v_2 = []
# for i in range(len(f)):
#     v_3 = []
#     for v in range(len(f[0])):
#         z = (f[i - 1][v]) + (f[(i + 1) % len(f)][v]) + (f[i][v - 1]) + (f[i][(v + 1) % len(f[0])])
#         v_3.append(z)
#     v_2.append(v_3.copy())
#     v_3.clear()
# for i in range(len(v_2)):
#     print(*v_2[i])

# def spiral(n):
#     dx, dy = 1, 0
#     x, y = 0, 0
#     myarray = [[None] * n for j in range(n)]
#     for i in range(1, n ** 2 + 1):
#         myarray[x][y] = i
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
#             x, y = nx, ny
#         else:
#             dx, dy = -dy, dx
#             x, y = x + dx, y + dy
#     return myarray
#
#
# def printspiral(myarray):
#     n = range(len(myarray))
#     for y in n:
#         for x in n:
#             print(myarray[x][y], end=' ')
#         print()
#
#
# n = int(input())
# printspiral(spiral(n))
#
# myarray = [[None] * n for j in range(n)]
# print(myarray)


# a = int(input())
# matr = [[0] * a for i in range(a)]
# b = 0
# x = 0
# y = 0
# stage = 0
#
#
# def status(mtrx, a):
#     for i in range(a):
#         matr[stage][x] = b + 1
#         x += 1
#         if x == a:
#         x = 0

# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))


# matr[0][i] = i + 1
# matr[0][i] = i + 1
# matr[0][i] = i + 1
#         b += 1
# for i in range(len(matr)):
#     print(matr[i])


# a = [1, 3, 5, 7]
# a = list(filter(lambda x: x % 2 == 0, a))
# print(a)
# a = list(map(lambda x: x // 2, a))
# print(a)
# a = (list(map(int, a)))
# print(a)


# def modify_list(l):
#     l = list(filter(lambda x: x % 2 == 0, l))
#     l = list(map(lambda x: x // 2, l))
#     global lst
#     lst = l
#     return

# def modify_list(l):
#     le = len(l)-1
#     i = le
#     while i!=-1:
#         if l[i]%2:
#             del l[i]
#         else:
#             l[i]=l[i]//2
#         i -=1
#     return


# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [5, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

a = [1,2,3,4,5,6,7,8,9]
a[:] = [i / 2 for i in a]
print(a)