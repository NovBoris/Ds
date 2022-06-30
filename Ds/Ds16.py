import random
list = []
while len(list) != 7:
    Number = random.randint(1,10)
    list.append(Number)
print(list)
honest = 0
odd = 0
for i in list:
    if i % 2 == 0:
        honest += 1
    else:
        odd += 1
print(honest)
print(odd)
if honest > odd:
    print(sum(list))
else:
    print(list[0] * list[2] * list [5])