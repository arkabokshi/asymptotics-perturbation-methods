import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rc('text',usetex=True)
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 12.5
plt.rcParams['ytick.labelsize'] = 12.5

eps = 0.05

def dvdt(v,t):
    x,y = v
    return [ y, -x*np.exp(-eps*t) ]


# Solve AX = B to determine {a,b}
S = np.sin(2/eps)
C = np.cos(2/eps)

A = np.array([[S,C],[-C,S]])
B = np.array([1,-eps/4])
X = np.linalg.solve(A,B)
print('[a,b]=',X)


# CALC & PLOT

time = np.linspace(0,200,1000)
sol  = odeint( dvdt,[1,0],time )

phase = 2/eps * np.exp(-eps*time/2)
yana = np.exp(eps*time/4) * ( X[0]*np.sin(phase) + X[1]*np.cos(phase) )

plt.figure(1)
plt.plot(time,np.exp(eps*time/4),color='gray',linewidth=1.75,label=r'$\exp(\epsilon t/4)$')
plt.plot(time,yana,color='orange',label=r'$y_\mathrm{ana}$')
plt.plot(time,sol[:,0],'--',color='blue',linewidth=1.75,label=r'$y_\mathrm{num}$')
plt.xlabel(r'$t$')
plt.ylabel(r'$x(t)$')
plt.ylim([-7.5,5])
plt.legend(loc='lower left',prop={'size':12.5})
plt.grid(axis='both',linestyle='--')
plt.savefig('../pdf/strogatz-wk18.pdf',bbox_inches='tight')


plt.show()
