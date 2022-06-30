def Evkl(a,b):
    if a < b:
        a, b = b, a


    if b != 0:
        a, b = b, a % b
        return Evkl(a, b)
    else:
        return a


print(Evkl(8, 20))


# a = 1,2,5,6,7,8,912,1,2,2,2,6
# def Max(args, func):
#     list = []
#     for x in args:
#         if func(x):
#             list.append(x)
#     return max(list), min(list)
#
# print(Max(a, lambda x: True if x % 2 == 0 else False))