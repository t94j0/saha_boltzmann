#!/usr/bin/env python3

# Combining both the Boltzmann and Saha equations and considering only transition
# from n=1 to n=2 and from neutral to ionized Hydrogen (i.e. neglecting
# all n > 2 states):
# 1. Turn in a graph (computer generated, excel is ok) of the Nn=2/Ntotal vs
# temperature states. The x-axis should display temperatures from 5,000 K
# to 25,000 K, the y-axis should run from 0 to 1.

import math
import matplotlib.pyplot as plt

def boltzmann(T):
    gb = 8
    ga = 2
    Eb = -13.6/4
    Ea = -13.6
    k = 8.617e-5

    return (gb/ga)*math.exp(-(Eb-Ea)/(k*T))

def saha(T):
    k   = 1.38e-23
    h   = 6.63e-34
    me  = 9.11e-31
    Xi  = 2.18e-18
    Pe  = 20
    Zi1 = 1
    Zi  = 2


    term1 = ((2 * k * T * Zi1) / (Pe * Zi))
    term2 = ((2 * math.pi * me * k * T) / (h**2)) ** 1.5
    term3 = math.e ** (-Xi/(k*T))

    return term1 * term2 * term3

def ratio(T):
    b = boltzmann(T)
    s = saha(T)
    return (b / (1 + b)) * (1 / (1 + s))

LOWER_BOUND = 5000
UPPER_BOUND = 25000
SKIP = 10

def plot():
    x = []
    y = []
    for i in range(LOWER_BOUND, UPPER_BOUND):
        if i % SKIP == 0:
            x.append(i)
            y.append(ratio(i))

    # plt.axis([5000, 25000, 0.0, 1.0])
    plt.title('Temperature vs N_II/N_total')
    plt.ylabel('N_II/N_total')
    plt.xlabel('Temperature (K)')
    plt.plot(x, y)
    plt.show()

plot()
