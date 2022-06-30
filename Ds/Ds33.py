# def factorial(n):
#     fac = 1
#     while n != 0:
#         fac *= n
#         n -= 1
#     return fac
#
# print(factorial(3))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(3))

# def args(*arg):
#     return sum(arg) / len(arg)
#
#
# print(args(2,5,2,5,2,5,2,5,2,5))

# a = [275,10,53,11,17,20,90,-77, -282, -228, 21051, 55]

# def sorting(lst, func):
#     lst2=[]
#     for x in lst:
#         if func(x):
#             lst2.append(x)
#     lst2.sort()
#     print(lst2)
#
#
# sorting(a,lambda x: True if x>0 else False)
#  #положительные
# sorting(a,lambda x: True if str(x)[-1]=='5' else False)
#  #заканчиваются на 5
# sorting(a,lambda x: True if x%5 ==0 else False) #делятся на 5
