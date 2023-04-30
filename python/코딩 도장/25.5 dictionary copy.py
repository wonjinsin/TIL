import copy             # copy 모듈을 가져옴
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
x is y  # True

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
x is y  # False

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'  # x와 y 둘다 바뀜

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)    # copy.deepcopy 함수를 사용하여 깊은 복사
y['a']['python'] = '2.7.15'
