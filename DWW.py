import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

death_rate = 0.3
albedo_g = 0.5
albedo_w = 0.75
albedo_b = 0.25
area_w = 0.2
area_b = 0.2
solar_input = 3668
sigma = 5.67032*10**(-8)
R = 0.12                     # temperature insulation
q = 2.06*10**9
k = 17.5**(-2)
temp_opt = 295.5

frames = 100
luminosity = np.linspace(0.65, 1.65, frames)

def func(areas, luminosity):
    areas = area_w, area_b

    area_g = 1 - area_w - area_b
    albedo = area_w*albedo_w + area_b*albedo_b + area_g*albedo_g

    temp = (luminosity * solar_input / 4 / sigma * (1-albedo))**(1/4)
    temp_w = (R * luminosity * solar_input / 4 / sigma * (albedo-albedo_w) + temp**4)**(1/4)
    temp_b = (R * luminosity * solar_input / 4 / sigma * (albedo-albedo_b) + temp**4)**(1/4)
    temp_g = (R * luminosity * solar_input / 4 / sigma * (albedo-albedo_g) + temp**4)**(1/4)
    print(temp, temp_w, temp_b)

    birth_rate_w = 1 - 0.003265 * (temp_w - 295.5)**2
    birth_rate_b = 1 - 0.003265 * (temp_b - 295.5)**2

    darea_wdt = area_w * (birth_rate_w * area_g - death_rate)
    darea_bdt = area_b * (birth_rate_b * area_g - death_rate)

    return darea_wdt, darea_bdt

areas = area_w, area_b
sol = odeint(func, areas, luminosity)

plt.plot(luminosity, sol[:,0])
plt.plot(luminosity, sol[:,1])
#plt.plot(luminosity, sol[:,1]+sol[:,0])
#plt.ylim(0, 0.7)
plt.xlabel('Luminosity')
plt.ylabel('Area fraction')
plt.title('Population')
plt.savefig('DWW.png')

print(sol)