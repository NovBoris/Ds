a = (i for i in range(0, 10))
print(sum(tuple(a)))
Tuple = tuple(range(10))

week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = 7
mean_temp = sum_temp / days
print(int(mean_temp))

text = input('Введите текст: ').split()
print(max(text, key=len))

res = []
for a in text:
    if len(a) >= len(''.join(res)):
        res.clear()
        res.append(a)
print(*res)

my_tuple = (777,)
print(my_tuple)

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
Tuple = [i for i in range(a, b + 1)]
print(tuple(Tuple))
