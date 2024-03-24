import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.4,2.9,200)

xlab = 'Вісь X'
ylab = 'Вісь Y'

#Графіки функцій
y1 = pow(x,3)-2*x*x-3*x+4-2*np.cos(2*x+1)
leg1 = 'exp(x,3)-2exp(x,2)-3x+4-2cos(2x+1)'

plt.grid(color = 'b', linewidth=1)

plt.xlabel(xlab, fontsize = 'x-large')
plt.ylabel(ylab, fontsize = 'x-large')

#Заголовок
plt.title('Варіант №2')

# Будуємо графіки
plt.plot(x,y1, 'g-', label = leg1)

plt.legend(loc='best')

plt.grid(True)

plt.savefig('var2.2.png', format = 'png')

plt.show()
