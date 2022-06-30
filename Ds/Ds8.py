# Калькулятор калорий
# Ввод возраста
import math

while 1 == 1:
    try:
        Age = int(input('Введите свой возраст: '))
        if Age < 13 or Age > 80:
            print('Возраст должен быть от 13 до 80 лет')
        else:
            break
    except ValueError:
        print('Это не возраст')
print(Age)
print('')

# Выбор пола

while 1 == 1:
    try:
        Sex = int(input('Введите пол: 1. Мужчина 2. Женщина Выберите 1 или 2: '))
        if Sex == 1:
            print('1. Мужчина')
            print('')
            break
        elif Sex == 2:
            print('2. Женщина')
            print('')
            break
    except ValueError:
        print('Такого варианта нет')

# Ввод веса

while 1 == 1:
    try:
        Weight_unit = int(input('Вес в килограммах или фунтах? Выберите 1 или 2: '))
        if Weight_unit == 1:
            print('1. Килограммах')
            print('')
            break
        elif Weight_unit == 2:
            print('2. Фунтах')
            print('')
            break
    except ValueError:
        print('Такого варианта нет')
while 1 == 1:
    if Weight_unit == 1:
        try:
            Weight = int(input('Введите свой вес: '))
            if Weight < 35 or Weight > 250:
                print('Вес должен быть в пределах от 35 до 250 кг')
            else:
                print(Weight, 'кг')
                print('')
                break
        except ValueError:
            print('Это не вес')
    elif Weight_unit == 2:
        try:
            Weight = int(input('Введите свой вес: '))
            if Weight < 75 or Weight > 550:
                print('Вес должен быть в пределах от 75 до 550 ib')
            else:
                print(Weight, 'ib')
                Weight = Weight * 0.4535923745
                print('')
                break
        except ValueError:
            print('Это не вес')

# Ввод роста

while 1 == 1:
    try:
        Growth_unit = int(input('Рост в сантиметрах или дюймах? Выберите 1 или 2: '))
        if Growth_unit == 1:
            print('1. Сантиметрах')
            print('')
            break
        elif Growth_unit == 2:
            print('2. Дюймах')
            print('')
            break
    except ValueError:
        print('Такого варианта нет')
while 1 == 1:
    if Growth_unit == 1:
        try:
            Growth = int(input('Введите свой рост: '))
            if Growth < 80 or Growth > 300:
                print('Рост должен быть в пределах от 80 до 300 см')
            else:
                print(Growth, 'см')
                print('')
                break
        except ValueError:
            print('Это не рост')
    elif Growth_unit == 2:
        try:
            Growth = int(input('Введите свой рост: '))
            if Growth < 30 or Growth > 120:
                print('Рост должен быть в пределах от 30 до 120 ib')
            else:
                print(Growth, 'Inch')
                Growth = Growth * 2.54
                print('')
                break
        except ValueError:
            print('Это не рост')

# Выбор интенсивности нагрузки.
# Выбор коэффициента физической нагрузки.

physical_activity_every_day = 1.9
physical_activity_6_7 = 1.725
physical_activity_3_5 = 1.55
physical_activity_1_3 = 1.375
no_physical_activity = 1.2
Coefficient = 0

try:
    Degree_of_physical_activity = int(input(
        '1. Очень высокая. Тренировки по несколько раз в день,\n2. Высокая. Ежедневные или физические нагрузки минимум 6 раз в неделю,\n3. Средняя. Не более 5 дней тренировок в неделю,\n4. Низкая. Физические нагрузки до 3 раз в неделю,\n5. Минимальная. Сидячий образ жизни, нет никаких тренировок\nВыберите 1,2,3,4,5: '))
except (ValueError):
    while 1 == 1:
        try:
            Degree_of_physical_activity = int(input('Выберите 1,2,3,4,5: '))
            break
        except ValueError:
            print('Такого варианта нет')

while 1 == 1:
    if Degree_of_physical_activity == 1:
        print('1. Очень высокая.')
        print('')
        Coefficient = physical_activity_every_day
        break
    elif Degree_of_physical_activity == 2:
        print('2. Высокая.')
        print('')
        Coefficient = physical_activity_6_7
        break
    elif Degree_of_physical_activity == 3:
        print('3. Средняя.')
        print('')
        Coefficient = physical_activity_3_5
        break
    elif Degree_of_physical_activity == 4:
        print('4. Низкая.')
        print('')
        Coefficient = physical_activity_1_3
        break
    elif Degree_of_physical_activity == 5:
        print('5. Минимальная.')
        print('')
        Coefficient = no_physical_activity
        break
    else:
        input('Выберете 1,2,3,4,5: ')
        break

# Выбор формулы рассчета.

try:
    Formula = int(input('1. Формула Миффлина - Сан-Жеора\n2. Формула Харриса-Бенедикта\nПо какой формуле считать?: '))
except ValueError:
    while 1 == 1:
        try:
            Formula = int(input('Выберите 1 или 2: '))
            if Formula == 1 or Formula == 2:
                break
        except ValueError:
            print('Такого варианта нет')
if Formula == 1:
    print('1. Формула Миффлина - Сан-Жеора')
    print('')
elif Formula == 2:
    print('2. Формула Харриса-Бенедикта')
    print('')

Calories = 0


def calculation_1():
    global Calories
    Calories = (10 * int(Weight)) + (6.25 * int(Growth)) - (5 * Age) + 5
    Calories = Calories * Coefficient
    print(math.ceil(Calories), 'ккал/день')


def calculation_2():
    global Calories
    Calories = (10 * int(Weight)) + (6.25 * int(Growth)) - (5 * Age) - 161
    Calories = Calories * Coefficient
    print(math.ceil(Calories), 'ккал/день')


def calculation_3():
    global Calories
    Calories = 66.47 + (9.6 * int(Weight)) + (1.85 * int(Growth)) - (4.68 * Age)
    Calories = Calories * Coefficient
    print(math.ceil(Calories), 'ккал/день')


def calculation_4():
    global Calories
    Calories = 66.47 + (13.75 * int(Weight)) + (5 * int(Growth)) - (6.74 * Age)
    Calories = Calories * Coefficient
    print(math.ceil(Calories), 'ккал/день')


if Formula == 1:
    if Sex == 1:
        if Weight_unit == 1:
            if Growth_unit == 1:
                calculation_1()
            elif Growth_unit == 2:
                calculation_1()

        elif Weight_unit == 2:
            if Growth_unit == 1:
                calculation_1()
            elif Growth_unit == 2:
                calculation_1()

    elif Sex == 2:
        if Weight_unit == 1:
            if Growth_unit == 1:
                calculation_2()
            elif Growth_unit == 2:
                calculation_2()

        elif Weight_unit == 2:
            if Growth_unit == 1:
                calculation_2()
            elif Growth_unit == 2:
                calculation_2()

elif Formula == 2:
    if Sex == 1:
        if Weight_unit == 1:
            if Growth_unit == 1:
                calculation_3()
            elif Growth_unit == 2:
                calculation_3()

        elif Weight_unit == 2:
            if Growth_unit == 1:
                calculation_3()
            elif Growth_unit == 2:
                calculation_3()

    elif Sex == 2:
        if Weight_unit == 1:
            if Growth_unit == 1:
                calculation_4()
            elif Growth_unit == 2:
                calculation_4()

        elif Weight_unit == 2:
            if Growth_unit == 2:
                calculation_4()
            elif Growth_unit == 1:
                calculation_4()


print('Конец')
