def CNK(n, k):
    listcnk = []
    chooses = []
    for i in range(int(n)):
        listcnk.append(i+1)
    c(listcnk, len(listcnk), k, chooses, k)

def c(listcnk, n, k, chooses, m):
    if len(chooses) == m:
        print(chooses)
        return
    if n <= 0: return
    c(listcnk, n-1, k, chooses, m)
    chooses.append(listcnk[n-1])
    c(listcnk, n-1, k-1, chooses, m)
    chooses.pop()

CNK(5, 3)