import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# пределы изменения переменной величины
# в данном случае время
T = np.arange(0, 60, 1)

# запись диф уравнения в виде функции
def radio_function(n, t):
    dmdt = k * n
    return dmdt

# определение начальных условий и параметров 
N = 1
k = 1/15 # постоянная распада для висмута 210

# решение уравнения функцией odeint
m_t = odeint(radio_function, N, T)

# построение решения в виде графика функции
plt.plot(T, m_t[:,0])
plt.xlabel('Время, минуты')
plt.ylabel('')
plt.title('Рост популяции бактерий')
plt.savefig('task_1.png')