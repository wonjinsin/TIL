from abc import *  # abstract base class의 약자


class 추상클래스이름(metaclass=ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        pass  # 추상클래스는 선언이 불가능하기 때문에 굳이 코드적어봐야 의미가 없음, 걍 pass 쓰면 됨

# 실제 사용


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')


james = Student()
james.study()
james.go_to_school()
