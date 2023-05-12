# dir([1, 2, 3]) 했을떄 __iter__ 있으면 iterator 사용 가능

it = [1, 2, 3].__iter__()
it.__next__()  # 1
it.__next__()  # 2
it.__next__()  # 3
it.__next__()  # error 발생

for i in range(3):  # 이때도 for문이 iter 호출하고, next 호출하면서 작동
    print(i)
