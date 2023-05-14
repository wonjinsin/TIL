# yield from에 코루틴를 지정하면 해당 코루틴에서 return으로 반환한 값을 가져옵니다

def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환
        total += x


def sum_coroutine():
    while True:
        # accumulate의 반환값을 가져옴, return오고 또 호출하면 기면 accumulate 없애고 다시 실행하는 느낌
        total = yield from accumulate()
        print(total)


co = sum_coroutine()
next(co)

for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄, 기존 값도 전부 초기화

for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
