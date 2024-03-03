
eps = 1e-4 # точність
s = 0; # сума ряду
k = 0; # індекс члена
a = 1; # член ряду

while abs(a) > eps :
    a *= 6.0 * pow(k,k) / pow(k+1, k+1)
    k += 1
    s += a
    print('{0:3d} {1:16.6g} {2:16.6g}'.format(k,a,s),sep=' \t')
print ('sum = ', s)    
