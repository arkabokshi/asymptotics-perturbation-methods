import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rc('text',usetex=True)

eps = 0.2
a0 =  1.0
f0  = [ 1.0,0.0 ]
t = np.linspace(0,50,1000)

def rhs(f,t):
    x,y = f
    dfdt = [ y, -eps*(y**3)-x ]
    return dfdt

xana = np.cos(t) / np.sqrt( eps*t*0.75 + 1./a0**2 )
xnum = odeint( rhs, f0, t )

plt.figure(1)
plt.plot(t,xnum[:,0],color='orange',label=r'$x_\mathrm{num}$')
plt.plot(t,xana,'--',color='black',label=r'$x_\mathrm{moa}$')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$x(t)$',size=20)
plt.yticks(np.linspace(-1,1,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':15})
plt.savefig('../nonlin-oscillator.pdf',bbox_inchs='tight')

plt.figure(2)
plt.scatter(xnum[:,0],xnum[:,1],s=1.5)
plt.xlabel(r'$x(t)$',size=20)
plt.ylabel(r'$\dot{x}(t)$',size=20)
plt.yticks(np.linspace(-1,1,11),fontsize=12.5)
plt.xticks(np.linspace(-1,1,11),fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.savefig('../nonlin-oscillator-phasespace.pdf',bbox_inchs='tight')


plt.show()
