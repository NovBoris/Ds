S = 'Тестовая строка №1'
S2 = '12412.4124'
print(S[::3])
print(S[0], end='')
print(S[-1])
print(S[0] + S[-1])
A = (S[0],S[-1])
print(''.join(A))
print(S.upper())
print(S[::-1])
print(S.isnumeric())
print(S2.isdigit())
print(S2.isnumeric())