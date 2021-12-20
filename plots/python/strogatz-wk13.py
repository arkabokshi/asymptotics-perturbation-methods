# Provided by Amit K. Singh
# 21 Oct '21
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
plt.rc('text',usetex=True)

eps = 1e-2

def dydx(x,y):
    return np.vstack((y[1], (-(1.0+x)*y[1]-y[0])/eps))

# residual boundary values
def bc(ya,yb):
    return np.array([ya[0]-0.0, yb[0]-1.0])


x = np.linspace(0, 1, 10)
y = np.zeros((2, x.size))

soln = solve_bvp(dydx, bc, x, y)

coef = np.linspace(-5,0,100)
x_p = np.power(10,coef)
y_p = soln.sol(x_p)[0]

yapprox = 2*(1/(1+x_p) - np.exp(-x_p/eps))

plt.figure(1)
plt.plot(x_p,y_p,linewidth=2.5,color='orange',label=r'$y_\mathrm{num}$')
plt.plot(x_p,yapprox,'--',linewidth=1.5,color='black',label=r'$y_\mathrm{ana}$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
plt.xscale('log')
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper left',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk13.pdf',bbox_inches='tight')

plt.show()
