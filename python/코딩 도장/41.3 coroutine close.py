def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()    # 코루틴 종료


def number_coroutine():
    # NOTE: coroutine with error
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()


def sum_coroutine():
    # couroutine with custom error
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total    # 코루틴 바깥으로 값 전달


co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))  # 190
"""
예외로 코루틴 끝내기
190
"""
