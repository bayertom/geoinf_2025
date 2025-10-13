from math import *

def add_multiply(a, b):
    c = a + b
    d = a * b
    return c, d


def quadr(a, b, c):
    #Compute discriminant
    D = b**2 - 4*a*c

    #D > 0
    if D > 0:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        
    #D == 0
    elif D == 0:
        x1 = -b/(2*a)
        x2 = x1    
    
    else:
        x1 = nan
        x2 = x1
    
    
    return x1, x2   

x = 10
y = 25

z1, z2 = add_multiply(x, y)
print("c= a + b =", z1, ", d = a * b =", z2)

a=1
b=2
c=3

x1,x2=quadr(a,b,c)
print(x1, x2)






