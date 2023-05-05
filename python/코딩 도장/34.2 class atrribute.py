class Person:
    def __init__(self):  # self는 자기 자신을 뜻함
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)


class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.

print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

# 클래스의 위치 인수, 키워드 인수


class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]


maria = Person(*['마리아', 20, '서울시 서초구 반포동'])


class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
        self.__wallet = 10000  # 비공개 변수

    def __privateMethod():  # 비공개 함수
        return


maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
