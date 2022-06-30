# Задание 1

# a = input('Введите число: ')
# print(a.isdigit())

# Задание 2

# b = int(input('Введите число: '))
# print(b % 6 == 0)

# Задание 3

# a = input('Введите 1 сторону треуголника: ')
# b = input('Введите 2 сторону треуголника: ')
# c = input('Введите 3 сторону треуголника: ')
# print(a == b and a == c)

# Задание 4

a = input('Введите строку: ')
list_vowels = []
alf = ['a','e','i','o','u','y']
res = ''
alf_status = False

for i in a + ' ':
    if i.lower() in alf:
        alf_status = True
    else:
        alf_status = False
    if alf_status:
        res += i
    else:
        if len(res) != 0:
            list_vowels.append(res)
            res = ''
print(*list_vowels)

for b in a:
    if b.lower() not in alf:
        a = a.replace(b, ' ')
print(' '.join(a.split()))