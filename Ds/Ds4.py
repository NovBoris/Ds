import random

# number = random.randint(100,999)
# print(number)
#
# sum = 0
#
# while sum < 1000:
#     Ost = number % 10
#     sum = Ost + sum
#     while sum <1000:
#         Ost = sum % 10
#         sum = Ost + sum
#         print(sum)
# print(sum)

# number2 = random.uniform(100,999)
# print(number2)
#
# sum2 = 0
#
# while number2 > 0:
#     Ost = number2 % 10
#     sum2 = Ost + sum2
#     number2 = number2//10
# print(int(sum2))
#
number3 = random.randint(100,999)
print(number3)
sum3 = 0
number3 = str(number3)
for i in number3:
    sum3 += int(i)
print(sum3)

# number4 = random.uniform(100,999)
# print(number4)
# sum4 = 0.0
# number4 = str(number4)
# for i in number4:
#     sum4 += float(i)
# print(sum4)