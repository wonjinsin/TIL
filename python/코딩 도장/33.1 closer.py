def foo():
    x = 10
    print(x)


foo()
print(x)  # error. 지역변수 호출

x = 10          # 전역 변수


def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력


foo()
print(x)        # 전역 변수 출력


x = 10          # 전역 변수


def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력


foo()
print(x)        # 전역 변수 출력

# 전역 변수 x가 없는 상태


def foo():
    global x    # x를 전역 변수로 만듦
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력


foo()
print(x)        # 전역 변수 출력
