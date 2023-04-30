x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')
# a b c d

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)
"""
a 10
b 20
c 30
d 40
"""

for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end=' ')
# a b c d

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value, end=' ')
