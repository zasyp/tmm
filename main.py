import numpy as np
f = np.pi / 6
OMEGA_1 = -1
LENGTH_AO = 0.02
LENGTH_AB = 0.08
x_b = 0

def phi(phi_1):
    global omega_1
    return np.pi/2 + omega_1 * phi_1

def x_a(phi_1):
    global LENGTH_AO
    return LENGTH_AO * np.cos(phi(phi_1))

def y_a(phi_1):
    global LENGTH_AO
    return LENGTH_AO * np.sin(phi(phi_1))

def phi_2(phi_1):
    global LENGTH_AB
    return np.arccos(-(x_a(phi_1)/LENGTH_AB))

def y_b(phi_1):
    global LENGTH_AB
    return y_a(phi_1) + LENGTH_AB * np.sin(phi_2(phi_1))

def x_s2(phi_1):
    pass

