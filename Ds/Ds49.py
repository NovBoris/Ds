# def concatenation_strings(string):
#     return ''.join(string.split())


#
# for i, line in enumerate(sys.stdin, 1):
#     print(i, line, end='')



lines_index = []
with open('dataset_3363_2.txt', 'r+', encoding='utf-8') as file:
    while file.readline():
        lines_index.append(file.tell())
    for i, line in enumerate(file.readlines(), 1):
        file.seek(lines_index[i])
        file.write(f'{i}')  # Прочитать шестую строку
        print(lines_index)