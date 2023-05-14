# __name__은 모듈의 이름이 저장되는 변수

# hello.py 파일에 아래가 있다고 해보자
print('hello 모듈 시작')
print('hello.py __name__:', __name__)


# main.py 파일
# import hello    # hello 모듈을 가져옴, 위에 print로 인해 __name__변수 hello 나옴
print('hello 모듈 끝')
print('main.py __name__:', __name__)    # __name__ 변수 출력, __main__

# hello.py 파일에 대해 실행
# hello.py에서 hello.py파일을 실행해버리면, __main__ 나옴
print('hello.py __name__:', __name__)

# 아래처럼 import아니고 직접 실행일때만 동작하도록 할 수 있음


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10, 20))
    print(mul(10, 20))
