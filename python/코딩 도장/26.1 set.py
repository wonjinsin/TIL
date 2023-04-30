fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}

fruits = {'orange', 'orange', 'cherry'}  # {'cherry', 'orange'} 중복안됨

'orange' in fruits  # True

a = set('apple')    # 유일한 문자만 세트로 만듦 {'e', 'l', 'a', 'p'}
b = set(range(5))  # {0, 1, 2, 3, 4}
c = set()  # 빈 세트

a = frozenset(range(10))  # 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없습니다.
