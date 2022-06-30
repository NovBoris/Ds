list = [15, 48, 'hello', 6, 19, 'world']
suma = 0
vowels = 0
consonants = 0
list_of_vowels = []
list_of_consonants = []
list_pos = []
list_pos_2 = 0
result = []
alf = ['a','e','i','o','u','y']
def d():
    global list_pos_2
    global vowels
    global consonants
    if list_pos_2 == len(i):
        list_of_vowels.append(vowels)
        list_of_consonants.append(consonants)
        vowels = 0
        consonants = 0
        list_pos_2 = 0
for i in list:
    if isinstance(i, int):                                           #Проверка на тип данных элемента списка list
        if i % 2 == 0:                                               #
            for a in str(i):                                         #
                list_pos.append(int(a)) ##############################
                suma = int(a) + suma                                 #
                if len(str(i)) == len(list_pos):                     # Проверка на смену элемента в списке list + сумма цифр числа
                    if (sum(list_pos)) == suma:                      #
                        result.append(suma)                          #
                        suma = 0                                     #
                        list_pos.clear()##############################
        else:
            ind = list.index(i)                                      #Замена элемента нечетного числа на 1
            list.insert(ind, 1)                                      #
            list.remove(i)                                           #
    elif isinstance(i, str):                                         #Проверка на тип данных элемента списка list
        list_2 = []                                                  #
        list_2.append(i)                                             #                              #
        for i in list_2:                                             #
            for b in i:                                              #
                if b.lower() in alf:                                         #
                    vowels += 1                                      #Количество гласных
                    list_pos_2 += 1
                    d()
                elif b not in alf:                                   #
                    consonants += 1                                  #Количество согласных
                    list_pos_2 += 1
                    d()

print(list)
print(*result)
print(f'Гласные: {list_of_vowels}')
print(f'Согласные: {list_of_consonants}')
