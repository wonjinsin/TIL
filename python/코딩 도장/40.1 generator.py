# 제너레이터는 이터레이터를 생성해주는 함수
def number_generator():
    yield 0  # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1
    yield 2


for i in number_generator():
    print(i)


def one_generator():
    yield 1
    return 'return에 지정한 값'


try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)    # return에 지정한 값
