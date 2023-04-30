from collections import defaultdict    # collections 모듈에서 defaultdict를 가져옴
x = {"a": 1}
x.setdefault("b")  # {'a': 1, 'b': None}
x.setdefault("c", 1)  # {'a': 1, 'b': None, 'c': 1}
x.update(a=2, b=3)  # {'a': 2, 'b': 3, 'c': 1}, key가 문자열일때만 가능

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})  # {1: 'ONE', 2: 'two', 3: 'THREE'}
# {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
y.update([[2, 'TWO'], [4, 'FOUR']])
# {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}
y.update(zip([1, 2], ['one', 'two']))

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')  # 10
x  # {'b': 20, 'c': 30, 'd': 40}
x.pop('z', 0)  # z 없으므로 기본값 설정한 0 반환

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']  # {'b': 20, 'c': 30, 'd': 40}

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()  # pop을 하고 tuple을 반환 ('d', 40)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()  # {}

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a')  # 10
x.get('z', 0)  # 0

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()  # dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
x.keys()  # dict_keys(['a', 'b', 'c', 'd'])
x.values()  # dict_values([10, 20, 30, 40])

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)  # {'a': None, 'b': None, 'c': None, 'd': None}
y = dict.fromkeys(keys, 100)  # {'a': 100, 'b': 100, 'c': 100, 'd': 100}

y = defaultdict(int)    # int로 기본값 생성
y['z']  # 그냥 dict는 에러나는데, defaultdict는 없는 key부르면 defaultint인 0 나옴

z = defaultdict(lambda: 'python')
z['a']  # 'python'
z[0]  # 'python'
