import math

def f(x):
    return round(pow(1-math.exp(x)*math.cos(x),2), 5)

def derivative(x):
    inc = 1e-3
    return round((f(x+inc)-f(x))/inc, 5)


def solve(x1, x2, err):
    n = 0
    while abs(x2-x1) >= err:
        n += 1
        f1 = f(x1)
        f2 = f(x2)
        f1d = derivative(x1)
        f2d = derivative(x2)
        z = f1d + f2d - 3*((f2-f1)/(x2-x1))
        w = math.sqrt(z*z - f1d*f2d)
        u = (w + z - f1d)/(2*w-f1d+f2d)                   
        opt = x1 + u*(x2-x1)
        if f1d * derivative(opt) < 0:
            x1 = x1
            x2 = opt
        else:
            x1 = opt
            x2 = x2
        print('Ітерація №', n, ': Xmin = ', round(opt,5))    

x1 = 1
x2 = 3
err = 1e-3
solve(x1,x2,err)
    