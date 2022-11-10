import math
def distanse(x1, y1, x2, y2):
    x = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)
    return x
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(distanse(x1, y1, x2, y2))
