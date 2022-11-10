a = range(500)
for i in a:
    s = str(i)
    if "8" in s and i % 7 == 0:
        print(i)