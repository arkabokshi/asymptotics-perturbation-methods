import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rc('text',usetex=True)
plt.rcParams['lines.linewidth'] = 1.75
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 12.5
plt.rcParams['ytick.labelsize'] = 12.5

eps = 0.1

def dvdt(v,t):
    y,z = v
    return [z,y*(z-1)/eps]


t_low = np.linspace(0,3,1000)
t_upp = np.linspace(0,1,100)

init_yz_low = [[0,-3],[0,-6],[0,-9],[0,-12]]
init_yz_upp = [[-1.0,5],[-1.1,5],[-1.3,5],[-1.5,5]]


# CALC & PLOT

lc = ['red','green','blue','black','orange']

plt.figure(1)

i=0
for t0 in init_yz_low:
    sol = odeint( dvdt,t0,t_low )
    plt.plot(sol[:,0],sol[:,1],color=lc[i])
    i += 1

i=0
for t0 in init_yz_upp:
    sol = odeint( dvdt,t0,t_upp )
    plt.plot(sol[:,0],sol[:,1],color=lc[i])
    i += 1

plt.plot([1,1],[-20,5],linewidth=5,color='gray',alpha=0.3)
plt.plot([-1,-1],[-20,5],linewidth=5,color='gray',alpha=0.3)
plt.xlabel(r'$y(t)$')
plt.ylabel(r'$z(t)$')
plt.ylim(-12.5,5)
plt.xlim(-1.5,1.5)
plt.grid(axis='both',linestyle='--')
plt.savefig('../pdf/strogatz-wk16.pdf',bbox_inches='tight')


plt.figure(2)

i = 2
ic = [[1,0.8],[1,0.99],[1,0.9]]
tt = np.linspace(0,1,100)
for t0 in ic:
    sol = odeint( dvdt,t0,tt )
    plt.plot(tt,sol[:,0],color=lc[i],label=r'$z(0)={:.2f}$'.format(t0[1]))
    i += 1

plt.plot([0.5,0.5],[-20,5],linewidth=5,color='gray',alpha=0.3)
plt.xlabel(r'$t$')
plt.ylabel(r'$y(t)$')
plt.ylim(-1.5,1.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk16-z-guess.pdf',bbox_inches='tight')

plt.show()
