a = int(input('Введите число a: ')) -1
b = int(input('Введите число b: '))
while a != b:
    a += 1
    if a != 0 and a % 777 == 0:
        break
    elif a % 2 == 0 or a % 3 == 0:
        continue
    print(a)
