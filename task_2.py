import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

T = np.arange(0, 20, 0.01)

def radio_function(q, t):
    dmdt = k * q * t
    return dmdt
 
Q = 1000
k = - 0.08

m_t = odeint(radio_function, Q, T)

plt.plot(T, m_t[:,0])
plt.xlabel('Время, года')
plt.ylabel('')
plt.title('Инвестировал в говно')
plt.savefig('task_2.png')