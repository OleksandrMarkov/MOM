# Функція розрахунку члена ряду
def next_val(n):
    return pow(6,n)/pow(n,n)

eps = 1e-4 # точність
s = 0; # сума ряду
k = 0; # індекс члена
a = 1; # член ряду

while abs(a) > eps :
    k += 1
    a = next_val(k)
    s += a
    print('{0:3d} {1:16.6g} {2:16.6g}'.format(k,a,s),sep=' \t')
print ('sum = ', s)    
