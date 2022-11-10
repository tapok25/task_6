
def more_than_five(lst):
    x = []
    for i in lst:
        if abs(i) > 10:
            x.append(i)
    return x

lst = [5, 10, 15, -20]
print(more_than_five(lst))
