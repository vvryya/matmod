---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №4"
subtitle: "дисциплина: Математическое моделирование"
author: ""

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы



# Задание

**Вариант 35**  
  Задача: Постройте фазовый портрет гармонического осциллятора и решение уравнения
гармонического осциллятора для следующих случаев:

1. Колебания гармонического осциллятора без затуханий и без действий внешней
силы  $x'' + 7.4x = 0$

2. Колебания гармонического осциллятора c затуханием и без действий внешней
силы $x'' + 10.1x' + 0.1x = 0$

3. Колебания гармонического осциллятора c затуханием и под действием внешней
силы $x'' + 3x' + 3.3x = 0,2sin(3.5t)$

На интервале t = [0;33] (шаг 0.05) с начальными условиями $x_{0}=0$, $y_{0}=-1.4$

# Выполнение лабораторной работы

**1. Теоретические сведения**

Движение грузовика на пружинке, маятника, заряда в электрическом контуре, а также эволюция во времени многих систем в физике, химии, биологии и других науках при определенных предположениях можно описать одним и тем же дифференциальным уравнением, которое в теории колебаний выступает в качестве основной модели. эта модель называется линейным гармоническим осциллятором.
Уравнение свободных колебаний гармонического осциллятора имеет следующий вид:  
  $x'' + 2yx' + w_{0}^2x = 0$  
  где x – переменная, описывающая состояние системы (смещение грузика, заряд конденсатора и т.д.), y – параметр, характеризующий потери энергии (трение механической системе, сопротивление в контуре), $w_{0}$ – собственная частота колебаний, t – время.  
  Предыдущее уравнение - линейное однородное дифференциальное уравнение второго порядка и оно является примером линейной динамической системы.  
  При отсутствии потерь в системе ($y = 0$ получаем уравнение консервативного осциллятора энергия колебания которого сохраняется во времени: $x'' + w_{0}^2x = 0$. Для однозначной разрешимости уравнения второго порядка необходимо задать два начальных условия $x(t_{0}) = x_{0}$ и $x'(t_{0}) = y_{0}$.  
  Уравнение второго порядка можно представить в виде системы двух уравнений первого порядка: $x' = y$ и $y' = -w_{0}^2x$; и тогда начальные условия примут вид: $x(t_{0}) = x_{0}$ и $y(t_{0}) = y_{0}$.

**2. Построение графиков**

2.1 Написала программу на Python
```
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x0 = np.array([0, -1.4]) #вектор начальных условий

w1 = 7.4
g1 = 0.0

w2 = 0.1
g2 = 10.0

w3 = 3.3
g3 = 3

t0 = 0
tmax = 33
dt = 0.05
t = np.arange(t0, tmax, dt)

def Y1(x, t):
    dx1_1 = x[1]
    dx1_2 = - w1*x[0] - g1*x[1] - 0
    return dx1_1, dx1_2

def Y2(x, t):
    dx2_1 = x[1]
    dx2_2 = - w2*x[0] - g2*x[1] - 0
    return dx2_1, dx2_2

def Y3(x, t):
    dx3_1 = x[1]
    dx3_2 = - w3*x[0] - g3*x[1] - 0.2*math.cos(4*t)
    return dx3_1, dx3_2

x1 = odeint(Y1, x0, t)
x2 = odeint(Y2, x0, t)
x3 = odeint(Y3, x0, t)

y1_1 = x1[:, 0]
y1_2 = x1[:, 1]

y2_1 = x2[:, 0]
y2_2 = x2[:, 1]

y3_1 = x3[:, 0]
y3_2 = x3[:, 1]

plt.plot(y1_1, y1_2)
plt.grid(axis = 'both')

plt.plot(y2_1, y2_2)
plt.grid(axis = 'both')

plt.plot(y3_1, y3_2)
plt.grid(axis = 'both')
```
Получила следующие графики (см. рис. -@fig:001, -@fig:002, -@fig:003).

![Рис. 1. График для 1 случая](image/1.png){ #fig:001 width=70% }

![Рис. 2. График для 2 случая](image/2.png){ #fig:002 width=70% }

![Рис. 3. График для 3 случая](image/3.png){ #fig:003 width=70% }

# Выводы

В ходе выполнения данной лабораторной работы я построила фазовый портрет гармонического осциллятора и решила уравнения гармонического осциллятора.
