def plus_ten(x):
    return x + 10

# lint가 funcion으로 바꿔버림
# plus_ten = lambda x: x + 10
# plus_ten


# (lambda x: y=10; x + y)(1)  # invalid, lambda 안에서 변수 선언 안됨

y = 10
(lambda x: x + y)(1)

list(map(lambda x: x + 10, [1, 2, 3]))  # [11, 12, 13]

(lambda: 1)()  # 빈거여도 () 있어야함
