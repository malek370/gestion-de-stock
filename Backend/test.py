import random
import math
def listAleaInt(n,a,b):
    return [random.randint(a,b) for _ in range(n)]

def minMaxMoy(l):
    return min(l),max(l),int(sum(l)/len(l))

a=listAleaInt(5,10,20)
mini=a.index(min(a))
print(a)
a[0],a[mini]=a[mini],a[0]
print(a)
print("===========")
print(minMaxMoy(a))
