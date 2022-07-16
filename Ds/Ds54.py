# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() -
# пусть в текущем классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
#
# from string import ascii_uppercase
#
#
# class Alphabet:
#     def __init__(self, lang: str, letters: str):
#         self.lang = lang
#         self.letters = letters
#
#     def print(self):
#         print(self.letters)
#
#     def letters_num(self):
#         return len(self.letters)
#
#
# class EngAlphabet(Alphabet):
#     __letters_num = 26
#
#     def __init__(self, lang: str = 'En', letters: str = ascii_uppercase):
#         super().__init__(lang, letters)
#
#     def is_en_letter(self, letter):
#         if letter.upper() in self.letters:
#             print(f'Буква {letter} из английского алфавита')
#         else:
#             print(f'Буква {letter} не из английского алфавита')
#
#     def letters_num(self):
#         return f'Количество букв в алфавите {self.__letters_num}'
#
#     @staticmethod
#     def example():
#         return 'Пример текста на английском: Meet my family. There are five of us – my parents, my elder brother, ' \
#                'my baby sister and me.\n' \
#                'First, meet my mum and dad, Jane and Michael. My mum enjoys reading and my dad enjoys playing chess' \
#                ' with my brother Ken. My mum is slim and rather tall.'


# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

# if __name__ == '__main__':
#     eng_text = EngAlphabet()
#     eng_text.print()
#     print(eng_text.letters_num())
#     eng_text.is_en_letter('F')
#     eng_text.is_en_letter('Щ')
#     print(eng_text.example())
#     print(EngAlphabet.example())
#     test_text = Alphabet('random', 'abcde123бабвгд')
#     test_text.print()
#     print(test_text.letters_num())
#     test_text_2 = EngAlphabet('random', 'abcde123бабвгд')
#     test_text_2.print()
#     print(test_text_2.letters_num())
