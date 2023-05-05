def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환 뒤에 () 붙이면 안됨


c = calc()
print(c(1), c(2), c(3), c(4), c(5))  # 8 11 14 17 20

# make with lambda


def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환


c = calc()
print(c(1), c(2), c(3), c(4), c(5))  # 8 11 14 17 20


def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add


c = calc()
c(1)  # 8
c(2)  # 19 
c(3)  # 33
