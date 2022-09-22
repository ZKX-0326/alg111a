from ipData import *
# 這是習題，請完成以下程式碼！
import random

def loss(a):
    c = 0
    p = 0
    # 4組資料輪流進行判定
    for i in range(len(coefs)):
        for j in range(len(coefs[i])):
            b = coefs[i][j] * a[j]
            c += b
        # 判定是否違反限制，若違反則將分數提高
        if c < maxs[i]:
            p += maxs[i] - c
            c = 0
        else:
            p += 9999
    return p

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
        # 因(x1,x2,x3,x4,x5)不為負，故將負數轉為0
        for i in range(len(tc)):
            if tc[i] < 0:
                tc[i] = 0
        # 分數判定，判定基準為接近4線交會點，並將交會點的分數假定為0，故取分數較小者
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