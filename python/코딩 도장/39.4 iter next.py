import random
it = iter(range(3))  # iterator 생성
next(it)  # 0
next(it)  # 1
next(it)  # 2
next(it)  # error

# 0부터 5까지 무작위로 숫자를 생성할 때 2가 나오면 반복을 끝내도록 만들 수 있음
it = iter(lambda: random.randint(0, 5), 2)
