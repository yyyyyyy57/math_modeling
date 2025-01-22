import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

T = np.arange(0, 200, 1)

def radio_function(m, a, k, v):
    dmdt = a + k*v*v/m
    return dmdt

A = 10
v0 = 10
M = 10
g = - 0.5

m_t = odeint(radio_function, M, A, g, v0)

plt.plot(T, m_t[:,0])
plt.xlabel('Время, года')
plt.ylabel('')
plt.title('Инвестировал в говно')
plt.savefig('task_3.png')