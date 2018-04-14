# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:29:18 2017

@author: Jacob Engelbrecht 
"""

from pylab import zeros
from pylab import sin
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

""" Variables meants to be altered by users """

steps = 2001

steps2 = 251
delt = 0.05

k = 0.50
population = 3
N = 2
a = 0.09
b = 1
a2 = 0.25

""" The rest of variables are initialized """

p1 = zeros(steps)
p2 = zeros(steps2)
t1 = zeros(steps)
t2 = zeros(steps2)
p1[0] = population
p2[0] = population
t1[0] = 0
t2[0] = 0

"""Equation used to calculate tests using steps"""

def equation(p, t, z, step):
    global steps; global delt
    iteration = 1
    while (iteration < step):
        p[iteration] = p[iteration - 1] + delt * (k * p[iteration - 1] * (1 - p[iteration - 1] / N) - z*(1+sin(b*t[iteration - 1])))
        if p[iteration] < 0:
            p[iteration] = 0
        t[iteration] = iteration / (1 / delt)
        iteration += 1
    return (p, t)
 
""" The actual population of the arrays with data """
    
p1, t1 = equation(p1, t1, a, steps)
p2, t2 = equation(p2, t2, a2, steps2)
    
""" Plots the First Figure """

plt.figure(1)     #initializes figure
plt.clf()         #clears anything in the figure 

line1, = plt.plot(t1, p1, 'bs-', label='k = 0.50 \nN = 2 \np[0] = 1\na = 0.09\nDelta T = 0.05')        #use these for p(t) vs t

plt.xlabel('Time', fontsize=20, color='black')     #sets labels, axises 
plt.ylabel('Fish Population', fontsize=20, color='black')                            #sets the y label 
plt.title('$\it{Plot\ K:\ Fish\ Population\ with\ Periodic\ Harvesting}$', fontsize=30, weight='bold') #sets the title and is italicized
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)}, loc = 4)

""" Plots the Second Figure """
plt.figure(2)
plt.clf()

line2, = plt.plot(t2, p2, 'bo-', label='k = 0.50 \nN = 2 \np[0] = 1\na = 0.25\nDelta T = 0.05')        #use these for p(t) vs t

plt.xlabel('Time', fontsize=20, color='black')     #sets labels, axises 
plt.ylabel('Fish Population', fontsize=20, color='black')                            #sets the y label 
plt.title('$\it{Plot\ L:\ Fish\ Population\ with\ Periodic\ Harvesting}$', fontsize=30, weight='bold') #sets the title and is italicized
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
