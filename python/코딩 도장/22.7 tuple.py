a = (11, 22, 33)
a.index(22)  # 2

a = (11, 22, 33, 22, 22)
a.count(22)  # 3

a = tuple(i for i in range(10) if i % 2 == 0)

a = tuple(map(int, a))
