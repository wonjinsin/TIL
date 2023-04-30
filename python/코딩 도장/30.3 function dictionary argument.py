def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)  # 딕셔너리의 key 개수와 이름이 같아야함


def personal_info(**kwargs):
    # 관례적으로 keyword arguments를 줄여서 kwargs로 사용
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')


personal_info(name='홍길동')  # name: 홍길동
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
"""
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
"""
