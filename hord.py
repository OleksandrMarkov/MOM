import math

def f(x):
    return pow(1-math.exp(x)*math.cos(x),2)

# a = (i-1)-й член
# b = i-й член

tmp = 1e-5

def findroot(a,b,err):
    n = 0
    while abs(b-a) > err:
        n = n + 1
        a = b - (b-a)*f(b)/(f(b)-f(a))
        if f(a)-f(b) == 0:
            b = a + (a-b)*f(a)/tmp
        else:
            b = a + (a-b)*f(a)/(f(a)-f(b))
        print ('Ітерація №', n, ': x = ', round(b,5), ', F(x) = ', round(f(b),5))

x0 = 2
x1 = 1
err = 0.001
findroot(x0,x1,err)
    