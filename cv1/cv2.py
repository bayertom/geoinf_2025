from math import *

def fn(n):
    f = 1
    while n > 1:
        f = n*f
        n = n-1 
        
    return f

def fn2(n):
    i = 1
    f = 1
    while i <= n:
        f = i * f
        i = i + 1
        
    return f

def maximum (L):
    l_max = L[0]
    for i in range(len(L)):
        if L[i] > l_max:
            l_max=L[i]
    return l_max

def maximum2 (L):
    l_max = L[0]
    for l in L:
        if l > l_max:
            l_max=l
    return l_max
   
def maximum3 (L):
    l_max = L[0]
    idx_max = 0
    for i in range(len(L)):
        if L[i] > l_max:
            l_max=L[i]
            idx_max = i
    return l_max, idx_max    

x = fn(5)
x2 = fn2(5)
print(x2)

L = [1, 12, -6, 5, 127, 1133]

#Access by index
for i in range(len(L)):
    print(L[i])

#Access by value
for l in L:
    print(l)
    
l_max, id_max = maximum3(L)
print('maximum:', l_max, ', index: ', id_max)
    











