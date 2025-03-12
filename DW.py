import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

growth_rate = 0.2
death_rate = 0.7
albedo_g = 0.5
albedo_w = 0.75
albedo_b = 0.25
alpha_w = 0.2
alpha_b = 0.2
S = 917
sigma = 5.67*10**(-8)
q = 2.06*10**9
k = 17.5**(-1/2)
temp_opt = 295.5

frames = 500
L = np.linspace(0.6, 1.6, frames)

def func(smth, L):
    alpha_w, alpha_b = smth

    temp = (S*L*(1-A)/sigma)
    temp_w = (q*(A-albedo_w)+temp)**(1/4)
    temp_b = (q*(A-albedo_b)+temp)**(1/4)

    if np.abs(temp_w - temp_opt) < k**(-1/2):
        beta_T_w = 1 - k*(temp_w - temp_opt)**2
    else:
        beta_T_w = 0
    if np.abs(temp_b - temp_opt) < k**(-1/2):
        beta_T_b = 1 - k*(temp_b - temp_opt)**2
    else:
        beta_T_b = 0

    alpha_g = 1 - alpha_w - alpha_b
    A = alpha_w*albedo_w + alpha_b*albedo_b + alpha_g*albedo_g

    dalpha_wdt = alpha_w * (alpha_g * beta_T_w - death_rate)
    dalpha_bdt = alpha_b * (alpha_g * beta_T_b - death_rate)

    return dalpha_wdt, dalpha_bdt

smth0 = (alpha_w, alpha_b)
sol = odeint(func, smth0, L)

plt.plot(L, sol[:,0])
plt.plot(L, sol[:,1])
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.savefig('DW.png')

print(sol)