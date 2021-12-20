import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import special
import math
plt.rc('text',usetex=True)

# Example 1

def rocket(v,t):
    y,g  = v 
    dvdt = [g,-1/(1+eps*y)**2]
    return dvdt

eps = 0.1
tau0 = np.linspace(0,2,100)
tau1 = np.linspace(0,2+eps*4./3.,100)

sol = odeint(rocket,[0,1],tau1)
y0 = tau0 - tau0**2/2.
y1 = tau1 - tau1**2/2. + eps*(tau1**3/3. - tau1**4/12.)

plt.figure(1)
plt.plot(tau0,y0,linewidth=2.5,color='blue',label=r'$y_0(\tau)$')
plt.plot(tau1,y1,linewidth=2.5,color='orange',label=r'$y_1(\tau)$')
plt.plot(tau1,sol[:,0],'--',linewidth=2.0,color='green',label=r'$y(\tau)_\mathrm{num}$')
plt.xlabel(r'$\tau$',size=20)
plt.ylabel(r'$y(\tau)$',size=20)
#plt.yticks(np.linspace(0,1,11),fontsize=12.5)
#plt.xticks(np.linspace(0,2,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower left',prop={'size':15})
plt.savefig('../pdf/strogatz-wk11.pdf',bbox_inches='tight')


# Example 2

eps = 0.5
x = np.linspace(0,2,100)

yana = 1. / (-eps + (1+eps)*np.exp(x))
y0 = np.exp(-x)
y1 = y0 + eps*( -np.exp(-x) + np.exp(-2*x) )

plt.figure(2)
plt.plot(x,y0,'--',linewidth=2.5,color='blue',label=r'$y_0$')
plt.plot(x,y1,linewidth=2.5,color='blue',label=r'$y_0 + \epsilon y_1$')
plt.plot(x,yana,linewidth=2.5,color='orange',label=r'$y(x)_\mathrm{ana}$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower left',prop={'size':15})
plt.savefig('../pdf/strogatz-wk11-ex2.pdf',bbox_inches='tight')

# EXAMPLE 3

eps = 0.05
x = np.linspace(1e-3,1,100)
yfunc = x + np.exp(-x/eps)
yasym = x

plt.figure(3)
plt.plot(x,yasym,linewidth=2.5,color='orange',label=r'$x$')
plt.plot(x,yfunc,'--',linewidth=2.0,color='blue',label=r'$x+\exp(-x/\epsilon)$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower right',prop={'size':15})
plt.savefig('../pdf/strogatz-wk11-ex3.pdf',bbox_inches='tight')

plt.show()
