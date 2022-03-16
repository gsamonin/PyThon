from gevent import monkey; monkey.patch_all()
import math
y = float(input())

def ex1 (y = 'val1'):
    x, z = 0,0
    if y<-55:
        a = ((43 + y) ** 4) / 49
        b = 9 * (((y ** 2) / 24) - 5 * y) ** 2
        c = (11 * y) ** 3
        f = a - b - c
        return round(f, 1)
    if -55 <= y < 43:
        f = 9 * (y ** 4)
        return math.ceil(f)

    if 43 <= y < 62:
        f = 54 * (y ** 5)
        return round(f, 1)
    if y >= 62:
        f = 93 * (y ** 6) + ((y ** 2) / 91)
        return round(f, 1)
    if y > 100: x = 10
    if var != True:
        print("var is not equal to True")
    if var == None:
        print("var is equal to None")
    k = True
    if k == True:
        print('Pravda')
print(main(y))