a = [4, 6, 'py', 78]
b = [44, 'hello', 56, 'exept', 3]
print(a + b)
b.insert(2,6)
print(b)
for i in a:
    if isinstance(i, str):
        a.remove(i)
for i in b:
    if isinstance(i, str):
        b.remove(i)
print(a)
print(b)
print(len(a))
print(len(b))