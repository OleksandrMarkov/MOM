import math

def f(x):
    return pow( 1 - math.exp(x)*math.cos(x), 2)

def derivative(x):
    inc = 1e-5
    return (f(x+inc) - f(x))/inc


a = 3  # f`(a)>0
b = 1  # f`(b)<0
err = 1e-3
z = (a + b)/2

if abs(derivative(z)) <= err:
    print ('Xmin = ', z)
else:
    n = 0
    while abs(b-a) >= err:
        n = n + 1
        z = (a+b)/2
        print('Ітерація №', n, ': Xmin = ', round(z,5))
        if derivative(z) > 0:
            a = z
        else:
            b = z
            
print('Xmin = ', round(z,5))            