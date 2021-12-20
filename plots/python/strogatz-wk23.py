import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rc('text',usetex=True)

# EXAMPLE 1

eps = 0.02
x0  = [ 1.0,0.0 ]
t = np.linspace(0,100,1000)

def rhs(x,t):
    y,f = x
    dxdt = [ f, -y - 2*eps*f ]
    return dxdt

yana = np.cos(t)*np.exp(-eps*t)
ynum = odeint( rhs, x0, t )

plt.figure(1)
plt.plot(t,ynum[:,0],linewidth=2.0,color='orange',label=r'$y_\mathrm{num}$')
plt.plot(t,yana,'--',linewidth=1.0,color='black',label=r'$y_\mathrm{msa}$')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$y(t)$',size=20)
plt.yticks(np.linspace(-1,1,5),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':15})
plt.savefig('../pdf/strogatz-wk23-ex1.pdf',bbox_inchs='tight')


# EXAMPLE 2: van der Pol 

eps = 0.1
x0  = [ 1./2.,0 ]
R0  = 1./4.     # since y(0) = 2*R0*cos( \theta_0 ) 

def vdP_rhs(x,t):
    y,f = x
    dxdt = [ f, -y - eps*f*(y**2-1) ]
    return dxdt

t    = np.linspace(0,100,1000)
yana = 2*np.cos(t) / np.sqrt( 1 + np.exp(-eps*t)*(-1+(1/R0**2)) )
ynum = odeint( vdP_rhs, x0, t )

plt.figure(2)
plt.plot(t,ynum[:,0],linewidth=2.0,color='orange',label=r'$y_\mathrm{num}$')
plt.plot(t,yana,'--',linewidth=1.0,color='black',label=r'$y_\mathrm{msa}$')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$y(t)$',size=20)
plt.yticks(np.linspace(-2,2,5),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower left',prop={'size':15})
plt.savefig('../pdf/strogatz-wk23-vdP.pdf',bbox_inchs='tight')

plt.show()
