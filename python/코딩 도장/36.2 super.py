class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)    # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

# Person의 init 호출해줘야댐


class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        # super()로 기반 클래스의 __init__ 메서드 호출,  super(Student, self).__init__() 이렇게 파생 클래스와 self를 줘도 됨
        super().__init__()
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)

# 기반 클래스를 호출하지 않아도 되는 경우


class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    pass  # init method 사용안하면 알아서 상위의 init method 실행함


james = Student()
print(james.hello)
