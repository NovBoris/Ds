# prod = int(input())
# b = 0
# c = 1
# d = [0, 1]
#
# while c < a * 2:
#     b += c
#     c += b
#     d.append(b)
#     d.append(c)
# print(d)
#
# for b in d:
#     c = d[d.index(b) + 1]
#     if a == 2:
#         res = [1, 1, True]
#         break
#     if b * c == a:
#         res = [b, c, True]
#         break
#     elif b * c > a:
#         res = [b, c, False]
#         break
#
# print(res)

# a, b = 0, 1
# while prod > a * b:
#     a, b = b, a + b
# print([a, b, prod == a * b])

# a = [2, 22, 37, 11, 4, 1, 5, 0]
# b = []
# c = []
# for i in a:
#     if i % 2 != 0:
#         b.append(i)
#
# b = list(map(str, sorted(b)))
# a = list(map(str, a))
# print(a)
# print(b)
# for i in a:
#     print(c)
#     if len(c) == len(a):
#         break
#     elif int(i) % 2 != 0:
#         c.append(b[0])
#         del b[0]
#     else:
#         c.append(i)
# print(list(map(int, c)))

# arr = [2, 22, 37, 11, 4, 1, 5, 0]
# source_array = [2, 22, 37, 11, 4, 1, 5, 0]
#
# odds = sorted((x for x in arr if x%2 != 0), reverse=True)
# print(odds)
# print([x if x%2==0 else odds.pop() for x in arr])
#
# odds = iter(sorted(v for v in source_array if v % 2))
# print([next(odds) if i % 2 else i for i in source_array])
