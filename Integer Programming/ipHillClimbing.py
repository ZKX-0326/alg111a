from ipData import *
# 這是習題，請完成以下程式碼！
import random

def point(a):
    c = 0
    p = 0
    for i in range(len(coefs)):
        for j in range(len(coefs[i])):
            b = coefs[i][j] * a[j]
            c += b
        if c < maxs[i]:
            p += c - maxs[i]
            c = 0
        else:
            p += 9999
    return abs(p)

def loss(t):
    return point(t)

def tryip():
    fail = 0
    t = [0.0, 0.0, 0.0, 0.0, 0.0]
    h = 1
    while fail < 5000:
        fail+=1
        dx0 = random.randint(-h, h)
        dx1 = random.randint(-h, h)
        dx2 = random.randint(-h, h)
        dx3 = random.randint(-h, h)
        dx4 = random.randint(-h, h)
        tc = [t[0]+dx0, t[1]+dx1, t[2]+dx2, t[3]+dx3, t[4]+dx4]
        for i in range(len(tc)):
            if tc[i] < 0:
                tc[i] = 0
        if loss(tc) < loss(t):
            t = tc
    return t

t = tryip()

v = 0
for i in range(len(t)):
    v += t[i] * cost_fn[i]
print("Objective value = %f" %(v))

for i in range(len(t)):
    print("%s = %f" %(unknowns[i], t[i]))