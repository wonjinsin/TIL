a = [1.2, 2.5, 3.7]
a = list(map(int, a))  # [1, 2, 3]

x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음
