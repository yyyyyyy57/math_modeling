import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# пределы изменения переменной величины
# в данном случае время
t = np.arange(0, 10**6, 100)

# запись диф уравнения в виде функции
def radio_function(m, t):
    dmdt = - k * m
    return dmdt

# определение начальных условий и параметров 
m_0 = 10
k = 1.61 * 10**(-6) # постоянная распада для висмута 210

# решение уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)

# построение решения в виде графика функции
plt.plot(t, m_t[:,0])
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.savefig('fig_1.png')