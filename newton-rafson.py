import math

def function(x):
    return round(pow(1 - math.exp(x)*math.cos(x),2) , 5)

def derivative(x):
    inc = 0.001
    ans = (function(x+inc)-function(x))/inc
    if ans == 0:
        return round(ans+1e-5, 5)
    else:
        return round(ans,5)

def solve(er, x0):
    n = 0
    x1 = round(x0 - function(x0)/derivative(x0), 5) 
    while abs(x1-x0) > er:
        n += 1
        x0 = x1
        x1 = round(x1 - function(x1)/derivative(x1), 5)
        print ('Ітерація № ', n, ': x = ', x1, ', F(x) = ', function(x1))
    

X0 = 1.5
error = 0.001
solve(error, X0)