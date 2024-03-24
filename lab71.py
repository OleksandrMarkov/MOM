import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.5,+0.5,500)

xlab = 'Вісь X'
ylab = 'Вісь Y'

#Графіки функцій
yа = 3*pow(x,2)
yб = -6*pow(x,2)+3*x
yв = pow(x,3)+2*pow(x,2)
yг = pow(x,5)
yд = np.sin(x)
yе = np.cos(x-1)+ abs(x) 

legа = '3*exp(x,2)'
legб = '-6*exp(x,2)+3*x'
legв = 'exp(x,3)+2*exp(x,2)'
legг = 'exp(x,5)'
legд = 'sin(x)'
legе = 'cos(x-1)+|x|'

plt.grid(color = 'b', linewidth=1)

plt.xlabel(xlab, fontsize = 'x-large')
plt.ylabel(ylab, fontsize = 'x-large')

#Заголовок
plt.title('Варіант №2')

# Будуємо графіки
plt.plot(x,yа, 'g-', label = legа)
plt.plot(x,yб, 'b-', label = legб)
plt.plot(x,yв, 'r-', label = legв)
plt.plot(x,yг, 'c-', label = legг)
plt.plot(x,yд, 'm-', label = legд)
plt.plot(x,yе, 'k-', label = legе)

plt.legend(loc='best')

plt.grid(True)

plt.savefig('var2.png', format = 'png')

plt.show()
