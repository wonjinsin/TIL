class Person:
    bag = []  # 여기서 선언하면 모든 class 인스턴스가 공유함, list, dict 같은 pointer 공유하는 것들만, string, int는 아님

    def put_bag(self, stuff):
        # 이렇게 Person의 값을 바꾸면 class 끼리 다 공유됨 (string, int도)
        Person.bag.append(stuff)
        self.bag.append(stuff)  # 이건 list, dict 같은 pointer만 공유


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)  # ['책', '북']
print(maria.bag)  # ['책', '북']


class Person:
    def __init__(self):
        self.bag = []  # 여기서 처음 선언하면 공유안함

    def put_bag(self, stuff):
        self.bag.append(stuff)
