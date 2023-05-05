# class method도 static method처럼 인스턴스 생성없이 생성할수 있지만, 메서드 안에서 class 속성에 접근해야할때 사용, static method는 self나 cls를 안붙이니까
class Person:
    count = 0    # 클래스 속성

    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
        # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근

    # method안에서 현재 클래스의 인스턴스 생성 가능
    @classmethod
    def create(cls):
        p = cls()    # cls()로 인스턴스 생성
        return p


james = Person()
maria = Person()

Person.print_count()    # 2명 생성되었습니다.
