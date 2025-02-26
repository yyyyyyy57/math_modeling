import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
seconds_in_year = 0.001
years = 1
t = np.linspace(0, years*seconds_in_year, frames)
 
def move_func(s, t):
    x, v_x, y, v_y = s
    
    dxdt = v_x
    dv_xdt = k*q*Q * x / (x**2 + y**2)**1.5 / m
    dydt = v_y
    dv_ydt = k*q*Q * y / (x**2 + y**2)**1.5 / m
    
    return dxdt, dv_xdt, dydt, dv_ydt

k = 9 * 10**9
Q = 100

x0 = 50
v_x0 = 0
y0 = 50
v_y0 = 0

q = 1
m = 0.1

s0 = (x0, v_x0, y0, v_y0)
sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()
	
ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
plt.plot([0], [0], 'o', color='y', ms=20)

plt.axis('equal')

edge = 100
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data(sol[:i,0], sol[:i, 2])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

ani.save('1.gif', writer='pillow')