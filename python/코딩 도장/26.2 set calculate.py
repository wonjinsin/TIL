a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합 연산
a | b  # {1, 2, 3, 4, 5, 6}
set.union(a, b)  # {1, 2, 3, 4, 5, 6}

# 교집합
a & b  # {3, 4}
set.intersection(a, b)  # {3, 4}

# 차집합
a - b  # {1, 2}
set.difference(a, b)  # {1, 2}

# 대칭 차집합 XOR
a ^ b  # {1, 2, 5, 6}
set.symmetric_difference(a, b)  # {1, 2, 5, 6}

# | 는 현재 세트에 다른 세트를 더함 update method
a = {1, 2, 3, 4}
a |= {5}
a  # {1, 2, 3, 4, 5}
a = {1, 2, 3, 4}
a.update({5})  # {1, 2, 3, 4, 5}

# 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}  # {1, 2, 3, 4}
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})  # {1, 2, 3, 4}

# 현재 세트에서 다른 세트를 빼기
a = {1, 2, 3, 4}
a -= {3}  # {1, 2, 4}
a = {1, 2, 3, 4}
a.difference_update({3})  # {1, 2, 4}

# 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}  # {1, 2, 5, 6}
a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})  # {1, 2, 5, 6}

# 현재 세트가 다른 세트의 부분집합(subset)인지 확인
a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}  # True
a <= {1, 2, 3}  # False
a.issubset({1, 2, 3, 4, 5})  # True

# 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인
a = {1, 2, 3, 4}
a < {1, 2, 3, 4, 5}  # True

# 현재 세트가 다른 세트의 상위집합(superset)인지 확인
a = {1, 2, 3, 4}
a >= {1, 2, 3, 4}  # True
a.issuperset({1, 2, 3, 4})  # True

# 현재 세트가 다른 세트의 진상위집합(proper superset)인지 확인
a = {1, 2, 3, 4}
a > {1, 2, 3}  # True

# 세트는 == 연산자를 사용하여 서로 같은지 확인
a = {1, 2, 3, 4}
a == {1, 2, 3, 4}  # True
a == {4, 2, 1, 3}  # True
a = {1, 2, 3, 4}
a != {1, 2, 3}  # True

# 세트가 겹치지 않는지 확인
a = {1, 2, 3, 4}
a.isdisjoint({5, 6, 7, 8})       # 겹치는 요소가 없음, True
a.isdisjoint({3, 4, 5, 6})    # a와 3, 4가 겹침, False
