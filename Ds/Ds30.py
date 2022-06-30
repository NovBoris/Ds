# def System2(a):
#     d = 0
#     res = []
#     for i in a:
#         for c in i:
#             if int(c) == 0 and d == 0:
#                 continue
#             elif int(c) == 0:
#                 d = d * 2
#             elif int(c) == 1:
#                 d = d * 2 + 1
#         res.append(d)
#         d = 0
#     return ','.join(list(map(str, res))).replace(',', '.')
#
# a = 0
#
# b = []
# while a > 0:
#     c = []
#     for i in range(8):
#         c.append(a % 2)
#         a = a // 2
#     c.reverse()
#     b.append(c)
#     c = []
# b.reverse()
#
# if len(b) == 4:
#     print(System2(b))
# elif len(b) == 3:
#     print('0.' + System2(b))
# elif len(b) == 2:
#     print('0.0.' + System2(b))
# elif len(b) == 1:
#     print('0.0.0.' + System2(b))
# elif len(b) == 0:
#     print('0.0.0.0')
#
# from ipaddress import IPv4Address
# int32 = 32
# print(str(IPv4Address(int32)))
#
# int32 = 32
# print('{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big')))
#
#
# i = 2154959208
# print('.'.join([str(x) for x in [i >> 24 & 0xFF,
#                                       i >> 16 & 0xFF,
#                                       i >> 8 & 0xFF,
#                                       i & 0xFF]]))
