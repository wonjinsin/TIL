from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

# Invalid, 무조건 else가 있어야댐
# list(map(lambda x: str(x) if x % 3 == 0, a))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# 아래랑 같은 의미
"""
def f(x):
     if x == 1:
         return str(x)
     elif x == 2:
         return float(x)
     else:
         return x + 10
list(map(f, a))
"""

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))  # [2, 8, 18, 32, 50]

# filter 함수


def f(x):
    return x > 5 and x < 10


a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))  # [8, 7, 9]

# filter 함수 lambda로
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x: x > 5 and x < 10, a))  # [8, 7, 9]

# reduce 사용하기 : 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
a = [1, 2, 3, 4, 5]
reduce(lambda x, y: x + y, a)  # 15
