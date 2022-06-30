# 1. Сделайте так чтобы он вывел элементы кортежа countries, кроме первых двух.
import random
#
# # countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# # print(countries[2:])
#
#
# # 2. На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# # Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
#
numbers = [input('Ведите число: ') for i in range(int(input('Введите количество чисел: ')))]
print(f'Количество чисел {len(numbers)}, числа: {" ".join(numbers)}')
result = []
for digit_check in range(0, 10):
    number = -1
    for number_to_check in numbers:
        if str(digit_check) in number_to_check:
            number = int(digit_check)
        else:
            number = -1
            break
    if number != -1:
        result.append(str(number))
print(f"Все общие цифры в числах🧐: {' '.join(sorted(result))}" if result else 'Общих цифр нет🤯')
#
# # 3. Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая
# # значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо присвоить переменной result.
#
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {first_dict_key: first_dict_value + second_dict_value for first_dict_key, first_dict_value in dict1.items()
#           for second_dict_key, second_dict_value in dict2.items() if first_dict_key == second_dict_key}
# print(result)
#
# result_new = {}
# for first_dict_key, first_dict_value in dict1.items():
#     for second_dict_key, second_dict_value in dict2.items():
#         if first_dict_key == second_dict_key:
#             result_new[first_dict_key] = first_dict_value + second_dict_value
#             break
# print(result_new)

