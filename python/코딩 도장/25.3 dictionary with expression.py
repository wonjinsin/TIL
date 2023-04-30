# 키만 가져옴 {'a': 0, 'b': 0, 'c': 0, 'd': 0}
{key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}

# 값을 키로 사용 {10: 0, 20: 0, 30: 0, 40: 0}
{value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}

# 키-값 자리를 바꿈 {10: 'a', 20: 'b', 30: 'c', 40: 'd'}
{value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}

# 중간에 dictionary 크기가 바뀌었다는 에러 발생
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제
print(x)

# 이런식으로 새로운 dictionary를 만들어야댐
# {'a': 10, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
