---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №5"
subtitle: "дисциплина: Математическое моделирование"
author: "Павлова Варвара Юрьевна"

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

Построить график для модели «хищник-жертва».

# Задание

**Вариант 35**  
  Задача: Для модели «хищник-жертва»:  
  $\frac{\partial x}{\partial t} = -0,29x(t)+0,031x(t)y(t)$  
  $\frac{\partial y}{\partial t} = 0,33y(t)-0,024x(t)y(t)$

Постройте график зависимости численности хищников от численности жертв,
а также графики изменения численности хищников и численности жертв при
следующих начальных условиях: $x_{0} = 7$, $y_{0} = 14$.
Найдите стационарное состояние системы.

# Выполнение лабораторной работы

**1. Теоритические сведения**
Простейшая модель взаимодействия двух видов типа "хищник-жертва", содель Лотки-Вольтерры. Данная двувидовая модель основывается на следующих предположениях:
1. Численность популяции жертв x и хищников y зависят только от времени(модель не учитывает пространственное распределение популяции на занимаемой территории).
2. В отсутствии взаимодействия численность видов изменяется по модели Мальтуса, при этом число жертв увеличивается, а число хищников падает.
3. Естественная смертность жертвы и естественная рождаемость хищника считается несущественным.
4. Эффект насыщения численности обеих популяций не учитывается.
5. Скорость роста численности жертв уменьшается пропорционально численности хищников:
  $\frac{\partial x}{\partial t} = ax(t)-bx(t)y(t)$
  $\frac{\partial y}{\partial t} = -cy(t)+dx(t)y(t)$

В этой модели x - число жертв, y - число хищников. Коэффициент a
описывает скорость естественного прироста числа жертв в отсутствие хищников, с
- естественное вымирание хищников, лишенных пищи в виде жертв. Вероятность
взаимодействия жертвы и хищника считается пропорциональной как количеству
жертв, так и числу самих хищников (xy). Каждый акт взаимодействия уменьшает
популяцию жертв, но способствует увеличению популяции хищников (члены -bxy
и dxy в правой части уравнения).  
  Стационарное состояние системы (1) (положение равновесия, не зависящее
от времени решение) будет в точке:
 
  $x_{0} = \frac{c}{d}$  
  $y_{0} = \frac{a}{b}$ 

**2. Построение графика**

2. Написала программу на Modelica:
```
model lab05
  parameter Real a=-0.29;
  parameter Real b=-0.031;
  parameter Real c=-0.33;
  parameter Real d=-0.024;
  parameter Real x0=7;
  parameter Real y0=14;
  Real x(start=x0);
  Real y(start=y0);
equation
  der(x)=a*x-b*x*y;
  der(y)=-c*y+d*x*y;
end lab05;
```
Получила следующий график (см. рис. -@fig:001).

![Рис. 1. График](image/1.png){ #fig:001 width=70% }

**3. Стационарное состояние**

Стационарная точка будет иметь коориднаты
$x_{0} = \frac{c}{d} = \frac{-0,33}{-0,024} = 13,75$ и
$y_{0} = \frac{a}{b} = \frac{-0,29}{-0,031} = 9,35$
# Выводы

В ходе выполнения данной лабораторной работы я построила график для модели "хищник-жертва"
