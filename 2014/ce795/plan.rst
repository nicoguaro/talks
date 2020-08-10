Covered
--------
- Introduction
- Review Vectors, Matrices, Tensors, Notation
- Displacement fields, Deformation Tensor, Definition of Strain (infinitesimal vs. large deformations)
- Internal Forces, Stress definitions

First lecture
-------------
- Motivation: Why waves? What waves are?

- Examples of waves in solids.

- Deduce the wave equation in a string doing the force balance in a differential element.

.. math::
  \nabla^2 u = \frac{1}{c^2}\frac{\partial^2 u}{\partial t^2},\\
  c^2 = \frac{T}{\lambda}\ .
  
- Explain basic concepts about waves: frequency, wavenumber, wavespeed (dispersion relations?).
  
- Derive momentum equations from a differential block (through balance of forces and moments of forces)
  
  - Use consitutive equations (Hooke's law) to deduce Navier-Cauchy equations.
  - Use Helmholtz decomposition and apply rotational and divergence to obtain wave equations.
  
- Explain monochromatic expansions and why are they useful

.. math::
  \nabla^2 u = \ddot{u}\\
  u = U e^{i\omega t}\\
  \nabla^2 U = -\omega^2 U
  
  
Second lecture
--------------
- Computational methods.
