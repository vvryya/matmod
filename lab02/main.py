import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k = 16.4
fi = 3*math.pi/4

#функция, описывающая движение катера береговой охраны
def dr(r, tetha):
    dr = sqrt(5)*r/math.sqrt(21)
    return dr

r01 = 83/15

te = np.arange(0, 2*math.pi, 0.01)

r1 = odeint(dr, r01, te)

#функция, описывающая движение лодки браконьеров
def xt(t):
    xt = math.tan(fi)*t
    return xt

t = np.arange(0, 20, 1)

#Перевод в полярные координаты
tete = (np.tan(xt(t)/t))**-1
rr = np.sqrt(t*t + xt(t)*xt(t))

#построение траектории движения катера в полярных координатах. 1 случай
plt.polar(te, r1, 'g')
#построение траектории движения лодки в полярных координатах
plt.polar(tete, rr, 'b')

#точки пересечения
idx = np.argwhere(np.diff(np.sign(rr - r1))).flatten()
print (tete[-1])
print (rr[idx[-1]])
