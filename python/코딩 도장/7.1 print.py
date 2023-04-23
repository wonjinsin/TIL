print(1, 2, 3)  # 1 2 3
print(1, 2, 3, sep=',')  # 1,2,3
print(1, 2, 3, sep='\n')  # 123이 엔터쳐진 상태로 들어감

# 123나옴 \n 없어짐
print(1, end='')
print(2, end='')
print(3)
