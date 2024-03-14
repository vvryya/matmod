import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 0.01
b = 0.02

N = 12300
I0 = 140
R0 = 54
S0 = N - I0 - R0
x0 = [S0, I0, R0]

t0 = 0
tmax = 200
dt = 0.01
t = np.arange(t0, tmax, dt)

def S1(x, t):
	dx1_0 = 0
	dx1_1 = -b*x[1]
	dx1_2 = b*x[1]
	return dx1_0, dx1_1, dx1_2

def S2(x, t):
	dx2_0 = -a*x[0]
	dx2_1 = a*x[0] - b*x[1]
	dx2_2 = b*x[1]
	return dx2_0, dx2_1, dx2_2

y1 = odeint(S1, x0, t)
y2 = odeint(S2, x0, t)

plt.plot(t, y1[:,0], label='S(t)')
plt.plot(t, y1[:,1], label='I(t)')
plt.plot(t, y1[:,2], label='R(t)')
plt.title('I(0) <= I*')
plt.legend

plt.plot(t, y2[:,0], label='S(t)')
plt.plot(t, y2[:,1], label='I(t)')
plt.plot(t, y2[:,2], label='R(t)')
plt.title('I(0) <= I*')
plt.legend

