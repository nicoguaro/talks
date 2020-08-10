# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:48:10 2014

@author: nicoguaro
"""
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

pi = np.pi

def sol(x, t, L=1., v=1., N=50):
    """
    Compute the solution for the 1D equation with fixed ends and
    initial condition at time t
    
        u(x,0) = sin(pi*x/L) + 1/2*sin(2*pi*x/L) - \
                  1/2*sin(3*pi*x/L)
    """
    g = np.sin(pi*x/L) + 1./2.*np.sin(2*pi*x/L) - 1./2.*np.sin(3*pi*x/L)
    y = 2./L*g*(np.sin(pi*x/L)*np.cos(pi*v*t/L) +
        np.sin(2*pi*x/L)*np.cos(2*pi*v*t/L)+
        np.sin(3*pi*x/L)*np.cos(3*pi*v*t/L))
        
    return y


nt = 100
Tmax = 2.
T = np.linspace(0., Tmax, nt)
nx = 200
L = 1.
x = np.linspace(0, L, nx)
Y = np.zeros((nt, nx))
Y[0,:] = np.sin(pi*x/L) + 1./2.*np.sin(2*pi*x/L) - \
          1./2.*np.sin(3*pi*x/L)


plt.close('all')
for k,t in enumerate(T):
    Y[k,:] = sol(x, t, N=100)
    plt.figure()
    plt.plot(x, Y[k,:])
    plt.ylim([-5, 5])
    plt.xlabel(r"$\frac{x}{L}$", size=15)
    plt.ylabel(r"$y$", size=15)
    suf = str(round(t,3)).zfill(3)
    plt.savefig("img/examples/ex1D-t=%s.pdf"%suf, bbox="tight")
    plt.savefig("img/examples/ex1D-t=%s.png"%suf, dpi=300)
    plt.close()
    
##plt.close('all')
