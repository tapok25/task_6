def is_prime(x):
    n = 0
    for i in range(2, x):
        if x % i == 0:
            n = n + 1
    if n <= 0:
        print(True)
    else:
        print(False)
x = int(input("Введите число от 0 до 1000:"))
is_prime(x)


