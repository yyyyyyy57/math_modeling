import numpy as np
import matplotlib.pyplot as plt

temp_min = 278.15
temp_max = 313.15
temp_opt = 295.65
albedo_barren = 0.5
albedo_white = 0.75
albedo_black = 0.25
albedo_3 = 0.5
area_white = 0.01
area_black = 0.01
area_3 = 0.01
death_rate = 0.3
S = 1000
sigma = 5.67032e-8
insul = 0.12

if __name__ == '__main__':

    luminosity = np.arange(0.5, 1.6, 0.0001)
    area_black_a = np.zeros_like(luminosity)
    area_white_a = np.zeros_like(luminosity)
    area_3_a = np.zeros_like(luminosity)
    temp_planet_a = np.zeros_like(luminosity)
    
    for j, lum in enumerate(luminosity):

        if area_black < 0.01:
            area_black = 0.01
        if area_white < 0.01:
            area_white = 0.01
        if area_3 < 0.01:
            area_3 = 0.01
        area_barren = 1 - (area_black + area_white + area_3)

        albedo_planet = (area_black * albedo_black + area_white * albedo_white +  area_3 * albedo_3 + area_barren * albedo_barren)
        temp_planet = (lum*S*(1-albedo_planet)/sigma)**(0.25)
        temp_black = (insul*lum*S/sigma*(albedo_planet-albedo_black) + temp_planet**4)**(0.25)
        temp_white = (insul*lum*S/sigma*(albedo_planet-albedo_white) + temp_planet**4)**(0.25)
        temp_3 = (insul*lum*S/sigma*(albedo_planet-albedo_3) + temp_planet**4)**(0.25)

        if (temp_black >= temp_min and temp_black <= temp_max):
           birth_black = 1 - 0.003265*(temp_opt-temp_black)**2
        else:
            birth_black = 0
        if (temp_white >= temp_min and temp_white <= temp_max):
            birth_white = 1 - 0.003265*(temp_opt-temp_white)**2
        else:
            birth_white = 0
        if (temp_3 >= temp_min and temp_3 <= temp_max):
            birth_3 = 1 - 0.003265*(temp_opt-temp_3)**2
        else:
            birth_3 = 0

        area_black += area_black*(birth_black*area_barren-death_rate)
        area_white += area_white*(birth_white*area_barren-death_rate)
        area_3 += area_3*(birth_3*area_barren-death_rate)

        area_black_a[j] = area_black
        area_white_a[j] = area_white
        area_3_a[j] = area_3
        temp_planet_a[j] = temp_planet

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(luminosity, 100*area_black_a, color='black')
    ax[0].plot(luminosity, 100*area_white_a, color='red')
    ax[0].plot(luminosity, 100*area_3_a, color='green')
    ax[0].set_ylabel('Площадь (%)')

    ax[1].plot(luminosity, temp_planet_a-273.15, color='black')
    ax[1].set_xlabel('Светимость звезды')
    ax[1].set_ylabel('Температура планеты (°C)')
    plt.savefig('DW_3.png')