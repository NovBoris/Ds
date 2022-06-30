figure = int(input('Сколько углов в фигуре?: '))
if figure == 3:
    print('Это треугольник, продолжим')
    first_corner = int(input('Сколько градусов угол № 1?: '))
    second_corner = int(input('Сколько градусов угол № 2?: '))
    third_corner = int(input('Сколько градусов угол № 3?: '))
    if (first_corner + second_corner + third_corner) > 180 or (first_corner + second_corner + third_corner) < 180:
        print('Сумма углов треугольника не может быть больше или меньше 180 градусов')
    else:
        if first_corner < 90 and second_corner < 90 and third_corner < 90 and first_corner != second_corner:
            print('Это остроугольный треуголник')
        elif first_corner == 90 or second_corner == 90 or third_corner == 90:
            print('Это прямоугольный треугольник')
        elif first_corner != second_corner and second_corner != third_corner and first_corner != third_corner:
            print('Это разносторонний треугольник:')
        elif first_corner == 60 and second_corner == 60 and third_corner == 60:
            print('Это равностороний треугольник')
        elif first_corner > 90 and first_corner != second_corner and second_corner != third_corner and first_corner != third_corner or first_corner > 90 and first_corner != second_corner and second_corner != third_corner and first_corner != third_corner or first_corner > 90 and first_corner != second_corner and second_corner != third_corner and first_corner != third_corner:
            print('Это тупоугольный треугольник')
        else:
            print('Это равнобедренный треугольник')
else:
    print('Это не треугольник')
