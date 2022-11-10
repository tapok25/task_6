def reverse_list(lst):
    n = [0, 0, 0, 0]
    h = 3
    for i in lst:
        n[h] = i
        h = h - 1
    return n
list = [8,1,0,4]
list = reverse_list(list)
print(list)


