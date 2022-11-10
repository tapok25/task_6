def invers(x):
    k = 0
    y = []
    for i in x:
        if i % 2 == 1:
            y.append(i)
    y = list(reversed(y))
    for i in x:
        if i % 2 == 1:
            x[i] = y[k]
            k = k + 1
    return x
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(invers(x))