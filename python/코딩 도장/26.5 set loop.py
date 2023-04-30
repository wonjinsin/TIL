a = {1, 2, 3, 4}
for i in a:
    print(i)

a = {i for i in 'apple'}  # {'l', 'p', 'e', 'a'}

a = {i for i in 'pineapple' if i not in 'apl'}  # {'e', 'i', 'n'}
