def number_generator():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달


for i in number_generator():
    print(i)


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def three_generator():
    yield from number_generator(3)    # 숫자를 세 번 바깥으로 전달


for i in three_generator():
    print(i)
