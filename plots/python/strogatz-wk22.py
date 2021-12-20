import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rc('text',usetex=True)

eps = 0.2
x0  = [ 1.0,0.0 ]
t = np.linspace(0,25,1000)

def rhs(x,t):
    y,f = x
    dxdt = [ f, -y - eps*(y**3) ]
    return dxdt

yana = np.cos(t + 3./8.*t*eps)
ynum = odeint( rhs, x0, t )
ysec = np.cos(t) + eps*( 1./32.*np.cos(3*t) - 1./32.*np.cos(t) - 3./8.*t*np.sin(t) )

plt.plot(t,ynum[:,0],color='orange',label=r'$y_\mathrm{num}$')
plt.plot(t,yana,'--',color='black',label=r'$y_\mathrm{msa}$')
plt.plot(t,ysec,color='blue',linewidth=1.25,label=r'$y_\mathrm{pert}$')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$y(t)$',size=20)
plt.yticks(np.linspace(-1,1,5),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper left',prop={'size':15})
plt.savefig('../pdf/strogatz-wk22-duffing.pdf',bbox_inchs='tight')

plt.show()
