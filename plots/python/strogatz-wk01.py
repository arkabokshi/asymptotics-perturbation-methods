import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

x = 10

# PART I : Numerical solution

f = lambda t: np.exp(-x*t) / (1+t)

area = integrate.quadrature(f,0.,2)
print('Integral = ',area)

t = np.linspace(0,2,100)
ft = np.exp(-x*t) / (1+t)

plt.plot(t,ft)
plt.yscale('log')
plt.show()

# PART II : Partial sums

n = 15      
Sn = 0.
for k in range(n+1):
    an = math.factorial(k) / np.power(x,k+1) * np.power(-1,k)
    Sn += an
    print(str(k).ljust(3),str(an).rjust(17),str(Sn).ljust(20))





