import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

death_rate = 0.2
albedo_g = 0.3
albedo_w = 0.5
albedo_b = 0.1
alpha_w = 0.15
alpha_b = 0.15
S = 917
sigma = 5.67*10**(-8)
q = 2.06*10**9
k = 17.5**(-2)
temp_opt = 295.5

frames = 500
L = np.linspace(0.8, 1.2, frames)

def func(smth, L):
    alpha_w, alpha_b = smth

    alpha_g = 1 - alpha_w - alpha_b                              
    A = alpha_w*albedo_w + alpha_b*albedo_b + alpha_g*albedo_g  

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


    dalpha_wdt = alpha_w * (alpha_g * beta_T_w - death_rate)   
    dalpha_bdt = alpha_b * (alpha_g * beta_T_b - death_rate)   

    return dalpha_wdt, dalpha_bdt

smth0 = (alpha_w, alpha_b)
sol = odeint(func, smth0, L)

plt.plot(L, sol[:,0])
plt.plot(L, sol[:,1])
plt.plot(L, sol[:,1]+sol[:,0])
plt.ylim(0, 0.7)
plt.xlabel('Luminosity')
plt.ylabel('Area fraction')
plt.title('Population')
plt.savefig('DWW.png')

print(sol)