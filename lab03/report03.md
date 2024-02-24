---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №3"
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

Построить графики модели боевых действий.

# Задание

**Вариант 35**
  Задача: Между страной Х и страной Y идет война. Численность состава войск исчисляется от начала войны, и являются временными функциями x(t) и y(t). В начальный момент времени страна X имеет армию численностью 31050 человек, а в распоряжении страны Y армия численностью в 20002 человек. Для упрощения модели считаем, что коэффициенты a, b, c, h постоянны. Также считаем P(t) и Q(t) непрерывными функциями.
  Постройте графики изменения численности войск армии X и армии Y для следующих случаев:

1. Модель боевых действий между регулярными войсками:
  $\frac{\partial x}{\partial t} = -0,25x(t)-0,74y(t)+sin(t+5)$  
  $\frac{\partial y}{\partial t} = -0,64x(t)-0,55y(t)+cos(t+6)$

2. Модель боевых действий с участием регулярных войск и партизанских отрядов: 
  $\frac{\partial x}{\partial t} = -0,32x(t)-0,89y(t)+2sin(10t)$  
  $\frac{\partial y}{\partial t} = -0,51x(t)y(t)-0,62y(t)+2cos(10t)$

# Выполнение лабораторной работы


**1. Рассмотрим подробнее уравнения**

1.1. В первом случае потери, не связанные с боевыми действиями, описывают члены -0,25x(t) и -0,55y(t), а -0,74y(t) и -0,64x(t) отражают потери на поле боя. Также sin(t+5) и cos(t+6) учитывают возможность подхода подкрепления к войскам Х и У в течение одного дня.

1.2. Во втором случае в борьбу добавляются партизанские отряды и потери, не связанные с боевыми действиями, описывают члены -0,32x(t) и -0,43y(t), а -0,89y(t) и -0,51x(t)y(t) отражают потери на поле боя. Также sin(t+5) и cos(t+6) учитывают возможность подхода подкрепления к войскам Х и У в течение одного дня.  
 
1.3. Начальные условия для обоих случаев будут равно $x_{0}=31.050$, $y_{0}=20.002$

**2. Построение графиков численности войск**

2.1. Написала программу на Modelica для 1 случая:

'''

model lab03
        parameter Real a=-0.25;
        parameter Real b=-0.74;
        parameter Real c=-0.64;
        parameter Real h=-0.55;
        parameter Real x0=31050;
        parameter Real y0=20002;
        Real x(start=x0);
        Real y(start=y0);
        Real t;
equation
        der(x)=a*x+b*y+sin(t+5);
        der(y)=c*x+h*y+cos(t+6);
        t=0;
end lab03;

'''
Varvara Pavlova <pvarua@gmail.com>
	
23 февр. 2024 г., 12:33 (22 часа назад)
	
кому: мне
---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №3"
subtitle: "дисциплина: Математическое моделирование"
author: "Миленин Иван Витальевич"

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

Построить графики модели боевых действий.

# Задание

**Вариант 35**  
  Задача: Между страной Х и страной У идет война. Численность состава войск
исчисляется от начала войны, и являются временными функциями
x(t) и y(t). В начальный момент времени страна Х имеет армию численностью 31 050 человек, а
в распоряжении страны У армия численностью в 20 002 человек. Для упрощения
модели считаем, что коэффициенты a, b, c, h постоянны. Также считаем
P(t) и Q(t) непрерывные функции.  
  Постройте графики изменения численности войск армии Х и армии У для
следующих случаев:

1. Модель боевых действий между регулярными войсками  
  $\frac{\partial x}{\partial t} = -0,25x(t)-0,74y(t)+sin(t+5)$  
  $\frac{\partial y}{\partial t} = -0,64x(t)-0,55y(t)+cos(t+6)$

2. Модель ведение боевых действий с участием регулярных войск и
партизанских отрядов  
  $\frac{\partial x}{\partial t} = -0,32x(t)-0,89y(t)+2sin(10t)$  
  $\frac{\partial y}{\partial t} = -0,51x(t)y(t)-0,62y(t)+2cos(10t)$

# Выполнение лабораторной работы

**1. Рассмотрим подробнее уравнения**

1.1. В первом случае потери, не связанные с боевыми действиями, описывают члены -0,25x(t) и -0,55y(t), а
-0,74y(t) и -0,64x(t) отражают потери на поле боя. Также sin(t+5) и cos(t+6) учитывают
возможность подхода подкрепления к войскам Х и У в течение одного дня.

1.2. Во втором случае в борьбу добавляются партизанские отряды и потери, не связанные с боевыми действиями, описывают члены -0,32x(t) и -0,43y(t), а
-0,89y(t) и -0,51x(t)y(t) отражают потери на поле боя. Также sin(t+5) и cos(t+6) учитывают
возможность подхода подкрепления к войскам Х и У в течение одного дня.  
 
1.3. Начальные условия для обоих случаев будут равно $x_{0}=31.050$, $y_{0}=20.002$

**2. Построение графиков численности войск**

2.1. Написал программу на Modelica для 1 случая:

```
model lab03
  parameter Real a=-0.25;
  parameter Real b=-0.74;  
  parameter Real c=-0.64;
  parameter Real h=-0.55;
  parameter Real x0=31050;
  parameter Real y0=20002;
  Real x(start=x0);
  Real y(start=y0);
  Real t;
equation
  der(x)=a*x+b*y+sin(t+5);
  der(y)=c*x+h*y+cos(t+6);
  t=0;
end lab03;
```
Получил следующий график (см. рис. -@fig:001).

![Рис. 1. График для 1 случая](image/2.png){ #fig:001 width=70% }

2.2. Написала программу на Modelica для 2 случая:

```
model lab0302
        parameter Real a=-0.32;
        parameter Real b=-0.89;
        parameter Real c=-0.51;
        parameter Real h=-0.62;
        parameter Real x0=31050;
        parameter Real y0=20002;
        Real x(start=x0);
        Real y(start=y0);
        Real t;
equation
        der(x)=a*x+b*y+2*sin(10*t);
        der(y)=c*x+h*y+2*cos(10*t);
        t=0;
end lab0302;
```

Получила следующий график (см. рис. -@fig:002).

![Рис. 2. График для 2 случая](image/4.png){ #fig:002 width=70% }

# Выводы

В ходе выполнения данной лабораторной работы я построила графики модели боевых действий.

