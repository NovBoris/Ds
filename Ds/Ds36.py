# a = (-10, 2, 3)
# res = ''
# for i in a:
#     if i > 0:
#         hen = f'{i: x}'
#         print(len(hen.strip()))
#         if i >= 0 and len(hen.strip()) < 2:
#             res = res + '0' + hen
#     elif i < 0:
#         res = res + '00'
# print(''.join(res.split()).upper())
#
# print(''.join(f'{a[0]: x}{a[1]: x}{a[2]: x}'.split()).upper())

# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))
#
# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num
#
#
# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

r = 255
print(f'{r:X}')