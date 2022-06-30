import random

Number = random.randint(100,999)
print(Number)
sum = 0
deli = 0
while Number > 0:
    deli = Number % 10
    Number //= 10
    sum += deli
print(sum)