a = [i for i in range(10)]
b = list(i for i in range(10))

a = [i for i in range(10) if i % 2 == 0]

a = [i * j for j in range(2, 10)
     for i in range(1, 10)]
