import math

def f(x):
    return pow(x,3)-2*x*x-3*x+4-2*math.cos(2*x+1)

def pd(a,b,eps=1e-8):
    if f(a)*f(b) > 0:
        print("error f(a)*f(b) > 0")
        return -1
    if a >= b:
        print("error a < b")
        return -1
    while True:
        x = a+(b-a)/2
        fx = f(x)
        if abs(fx) < eps:
            return x
        if f(a) * fx < 0:
            b = x
        else:
            a = x
        pass    

x1 = pd(1.4, 1.6)
x2 = pd(2.75, 2.90)

print('x1 = ', x1)
print('x2 = ', x2)
print(10*'-')
for x in [x1, x2]:
    print('f(',x,')=',f(x))
