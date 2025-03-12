import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
seconds = 20
t = np.linspace(0, seconds, frames)
 
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6) = s
    
    dxdt1 = v_x1
    dv_xdt1 = k*q1*Q * x1 / (x1**2 + y1**2)**1.5 / m1
    dydt1 = v_y1
    dv_ydt1 = k*q1*Q * y1 / (x1**2 + y1**2)**1.5 / m1

    dxdt2 = v_x2
    dv_xdt2 = k*q2*Q * x2 / (x2**2 + y2**2)**1.5 / m2
    dydt2 = v_y2
    dv_ydt2 = k*q2*Q * y2 / (x2**2 + y2**2)**1.5 / m2

    dxdt3 = v_x3
    dv_xdt3 = k*q3*Q * x3 / (x3**2 + y3**2)**1.5 / m3
    dydt3 = v_y3
    dv_ydt3 = k*q3*Q * y3 / (x3**2 + y3**2)**1.5 / m3

    dxdt4 = v_x4
    dv_xdt4 = k*q4*Q * x4 / (x4**2 + y4**2)**1.5 / m4
    dydt4 = v_y4
    dv_ydt4 = k*q4*Q * y4 / (x4**2 + y4**2)**1.5 / m4

    dxdt5 = v_x5
    dv_xdt5 = k*q5*Q * x5 / (x5**2 + y5**2)**1.5 / m5
    dydt5 = v_y5
    dv_ydt5 = k*q5*Q * y5 / (x5**2 + y5**2)**1.5 / m5

    dxdt6 = v_x6
    dv_xdt6 = k*q6*Q * x6 / (x6**2 + y6**2)**1.5 / m6
    dydt6 = v_y6
    dv_ydt6 = k*q6*Q * y6 / (x6**2 + y6**2)**1.5 / m6
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6)

k = 9 * 10**9
Q = 0.009

x01 = -30
v_x01 = 20
y01 = 0
v_y01 = 15
q1 = 0.0001
m1 = 0.1

x02 = -30
v_x02 = 10
y02 = 10
v_y02 = 15
q2 = -0.0001
m2 = 0.5

x03 = -30
v_x03 = -10
y03 = -10
v_y03 = -10
q3 = -0.0001
m3 = 0.1

x04 = -30
v_x04 = -10
y04 = 20
v_y04 = 15
q4 = -0.0001
m4 = 0.8

x05 = -30
v_x05 = 20
y05 = 30
v_y05 = -5
q5 = 0.0001
m5 = 0.8

x06 = -30
v_x06 = 20
y06 = -20
v_y06 = -5
q6 = 0.0001
m6 = 0.3

s0 = (x01, v_x01, y01, v_y01,
      x02, v_x02, y02, v_y02,
      x03, v_x03, y03, v_y03,
      x04, v_x04, y04, v_y04,
      x05, v_x05, y05, v_y05,
      x06, v_x06, y06, v_y06)
sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()
	
ball1, = plt.plot([], [], 'o', color='r')
ball_line1, = plt.plot([], [], '-', color='r')

ball2, = plt.plot([], [], 'o', color='b')
ball_line2, = plt.plot([], [], '-', color='b')

ball3, = plt.plot([], [], 'o', color='b')
ball_line3, = plt.plot([], [], '-', color='b')

ball4, = plt.plot([], [], 'o', color='b')
ball_line4, = plt.plot([], [], '-', color='b')

ball5, = plt.plot([], [], 'o', color='r')
ball_line5, = plt.plot([], [], '-', color='r')

ball6, = plt.plot([], [], 'o', color='r')
ball_line6, = plt.plot([], [], '-', color='r')

plt.plot([0], [0], 'o', color='y', ms=20)

plt.axis('equal')

edge = 80
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball1.set_data([sol[i][0]], [sol[i][2]])
    ball_line1.set_data(sol[:i, 0], sol[:i, 2])

    ball2.set_data([sol[i][4]], [sol[i][6]])
    ball_line2.set_data(sol[:i, 4], sol[:i, 6])

    ball3.set_data([sol[i][8]], [sol[i][10]])
    ball_line3.set_data(sol[:i, 8], sol[:i, 10])

    ball4.set_data([sol[i][12]], [sol[i][14]])
    ball_line4.set_data(sol[:i, 12], sol[:i, 14])

    ball5.set_data([sol[i][16]], [sol[i][18]])
    ball_line5.set_data(sol[:i, 16], sol[:i, 18])

    ball6.set_data([sol[i][20]], [sol[i][22]])
    ball_line6.set_data(sol[:i, 20], sol[:i, 22])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

ani.save('1.gif', writer='pillow')