# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def credit_cart(cart):
#     if len(cart) == 16 and cart.isdigit():
#         print(f'{"**** "*3}{cart[-4:]}')
#     else:
#         print('Некорректный номер')
#
#
# credit_cart(input('Введите номер кредитной карты: ').strip())

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def palindrom(word):
#     if word == word[-1::-1]:
#         print('Это слово палиндром')
#     else:
#         print('Это слово не палиндром')
#
#
# palindrom(input('Введите слово для проверки на палиндром: ').lower().strip())

# 3. Решите задачу

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# # созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)


# class Tomato:
#     states = {1: 'Зеленый', 2: 'Молочный', 3: 'Бледно-бурый', 4: 'Розовый', 5: 'Красный'}
#     states_key = {'Зеленый': 1, 'Молочный': 2, 'Бледно-бурый': 3, 'Розовый': 4, 'Красный': 5}
#
#     def __init__(self, index: int):
#         self._index = index
#         self._state = self.states[1]
#
#     def grow(self):
#         if self.states_key[self._state] < 5:
#             self._state = self.states[self.states_key[self._state] + 1]
#         else:
#             print(f'Помидор {self._index} уже созрел')
#
#     def is_ripe(self):
#         if self._state == 'Красный':
#             print(f'Помидор {self._index} полностью созрел')
#             return True
#         else:
#             print(f'Помидор {self._index} еще не созрел, он только {self._state}')
#
#
# # Класс TomatoBush
# # 1. Создайте класс TomatoBush
# # 2. Определите метод __init__(), который будет принимать в качестве параметра
# # количество томатов и на его основе будет создавать список объектов класса
# # Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# # 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# # томатов на следующий этап созревания
# # 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# # списка стали спелыми
# # 5. Создайте метод give_away_all(), который будет чистить список томатов после
# # сбора урожая
#
#
# class TomatoBush:
#     def __init__(self, amount: int):
#         self.tomatoes = [Tomato(index) for index in range(1, amount + 1)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# # Класс Gardener
# # 1. Создайте класс Gardener
# # 2. Создайте метод __init__(), внутри которого будут определены два динамических
# # свойства: 1) name - передается параметром, является публичным и 2) _plant -
# # принимает объект класса Tomato, является protected
# # 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# # растению становиться более зрелым
# # 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# # садовник собирает урожай. Если нет - метод печатает предупреждение.
# # 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# # по садоводству.
#
# class Gardener:
#     def __init__(self, name: str, plant: (str, list)):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print('Садовник работает')
#         self._plant.grow_all()
#         print('Садовник закончил работу')
#         print()
#
#     def harvest(self):
#         print('Садовник проверяет урожай')
#         if self._plant.all_are_ripe():
#             print('Садовник собирает урожай')
#             self._plant.give_away_all()
#             print('Урожай собран')
#         else:
#             print('Еще не созрели')
#             print()
#
#     @staticmethod
#     def knowledge_base():
#         print('Растения высаживаются по углам воображаемого квадрата, в центре которого располагается поливная яма.\n'
#               'На одну яму приходится четыре куста помидоров. Расстояние между кустами примерно 50-60 см,\n'
#               'а диаметр ямы – около 40 см. Делать яму нужно одновременно с высадкой рассады,\n'
#               'или через неделю после этого.')
#         print()
#
# # Тесты:
# # 1. Вызовите справку по садоводству
# # 2. Создайте объекты классов TomatoBush и Gardener
# # 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# # 4. Попробуйте собрать урожай
# # 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# # 6. Соберите урожай
#
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     Tomato_B = TomatoBush(3)
#     Gardener_1 = Gardener('Antonio', Tomato_B)
#     Gardener_1.work()
#     Gardener_1.harvest()
#     Gardener_1.work()
#     Gardener_1.work()
#     Gardener_1.work()
#     Gardener_1.work()
#     Gardener_1.harvest()
