import random
def RCNK(n, k):
    listrcnk = []
    for j in range(0, k):
        i = random.randrange(1, n+1)
        listrcnk.append(i)
    listrcnk.sort()
    if len(listrcnk) == k:
        print(listrcnk)
    return

for _ in range(10):
    RCNK(5, 3)