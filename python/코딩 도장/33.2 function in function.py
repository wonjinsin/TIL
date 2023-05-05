def print_hello():
    hello = 'Hello, world!'

    def print_message():
        print(hello)
    print_message()


print_hello()


def A():
    x = 10        # A의 지역 변수 x

    def B():
        x = 20    # x에 20 할당

    B()
    print(x)      # A의 지역 변수 x 출력


def A():
    x = 10        # A의 지역 변수 x

    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당

    B()
    print(x)      # A의 지역 변수 x 출력

# 제일 가까운 함수부터 찾음, 결과 50, 400


def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()


A()

# 함수가 뭐든 global 쓰면 전역변수 씀
x = 1


def A():
    x = 10

    def B():
        x = 20

        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()


A()
