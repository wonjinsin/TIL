def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


x = [10, 20, 30]
print_numbers(*x)  # list unpacking


def print_numbers(*args):
    for arg in args:
        print(arg)


print_numbers(10)  # 10
print_numbers(10, 20, 30, 40)
# 10
# 20
# 30
# 40


def print_numbers(a, *args):
    print(a)
    print(args)


print_numbers(1, 10, 20)
# 1
#(10, 20)
