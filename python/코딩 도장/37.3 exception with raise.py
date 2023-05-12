def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)                                       # 현재 함수 안에는 except가 없으므로
    # 예외를 상위 코드 블록으로 넘김


try:
    three_multiple()
except Exception as e:                             # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('예외가 발생했습니다.', e)


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise RuntimeError('3의 배수가 아닙니다.')    # 예외를 발생시킴, 에러 타입 설정할수도 있음
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김


try:
    three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)
# 3의 배수를 입력하세요: 5 (입력)
# three_multiple 함수에서 예외가 발생했습니다. 3의 배수가 아닙니다.
# 스크립트 파일에서 예외가 발생했습니다. 3의 배수가 아닙니다.
