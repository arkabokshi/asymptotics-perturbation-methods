import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
plt.rc('text',usetex=True)

eps = 0.02

def dydx(x,y):
    return np.vstack((y[1], (y[0]-x**2*y[1])/eps))

# residual boundary values
def bc(ya,yb):
    return np.array([ya[0]-1.0, yb[0]-1.0])


x = np.linspace(1e-4, 1, 30, endpoint=True)
y = np.zeros((2, x.size))

soln = solve_bvp(dydx, bc, x, y)

xnum = np.linspace(0,1,50,endpoint=True)
ynum = soln.sol(xnum)[0]

yinn = np.exp(-x/np.sqrt(eps))
yout = np.exp(1-1/x)
ycom = yinn + yout

plt.figure(1)
plt.plot(x,yinn,linewidth=1.5,color='green',label=r'$y_\mathrm{inn} = \mathrm{e}^{-x/\sqrt{\epsilon}}$')
plt.plot(x,yout,linewidth=1.5,color='red',label=r'$y_\mathrm{out} = \mathrm{e}^{1-1/x}$')
plt.plot(x,ycom,linewidth=2.5,color='orange',label=r'$y_\mathrm{inn}+y_\mathrm{out}$')
plt.plot(xnum,ynum,'--',linewidth=2.5,color='blue',label=r'$y_\mathrm{num}$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower right',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk14.pdf',bbox_inches='tight')

plt.show()
