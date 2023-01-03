import random
def RCNK(n, k):
    listrcnk = []
    lista = []
    for m in range(1, n+1):
        lista.append(m)
    for j in range(0, k):
        i = random.choice(lista)
        listrcnk.append(i)
        lista.remove(i)
    listrcnk.sort()
    if len(listrcnk) == k:
        print(listrcnk)
    return

for _ in range(10):
    RCNK(5, 3)