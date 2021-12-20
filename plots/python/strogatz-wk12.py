import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import special
import math
plt.rc('text',usetex=True)

# Example 1

def soln_ex1(x,eps):
    return (np.exp(-x)-np.exp(-x/eps)) / (np.exp(-1)-np.exp(-1/eps))

xx = np.linspace(0,1,200)

yana_eps1 = soln_ex1(xx,0.1)
yana_eps2 = soln_ex1(xx,0.04)
yana_eps3 = soln_ex1(xx,0.02)
yapprox = np.exp(1.-xx)

plt.figure(1)
plt.plot(xx,yana_eps1,linewidth=2.5,color='blue',label=r'$y_\mathrm{ana}(\epsilon = 0.1)$')
plt.plot(xx,yana_eps2,linewidth=2.5,color='orange',label=r'$y_\mathrm{ana}(\epsilon = 0.04)$')
plt.plot(xx,yana_eps3,linewidth=2.5,color='green',label=r'$y_\mathrm{ana}(\epsilon = 0.02)$')
plt.plot(xx,yapprox,'--',linewidth=2.0,color='gray',label=r'$\mathrm{e}^{1-x}$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
#plt.yticks(np.linspace(0,1,11),fontsize=12.5)
#plt.xticks(np.linspace(0,2,11),fontsize=12.5)
#plt.xscale('log')
#plt.yscale('log')
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower right',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk12.pdf',bbox_inches='tight')

eps = 3e-1
power = np.linspace(-5,1,100)
x_inn = np.power(10,power)
y_inn = np.exp(1) * (1-np.exp(-x_inn/eps))
y_out = np.exp(1-x_inn)
y_com = np.exp(1) * ( np.exp(-x_inn) - np.exp(-x_inn/eps) )
y_ana = soln_ex1(x_inn,eps)

plt.figure(2)
plt.plot(x_inn,y_inn,linewidth=2.5,color='orange',label=r'$y_\mathrm{inn}$')
plt.plot(x_inn,y_out,linewidth=2.5,color='gray',label=r'$y_\mathrm{out}$')
plt.plot(x_inn,y_com,'--',linewidth=1.5,color='blue',label=r'$y_\mathrm{c}$')
plt.plot(x_inn,y_ana,'--',linewidth=1.5,color='green',label=r'$y_\mathrm{ana}$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$y(x)$',size=20)
plt.ylim([10**(-2),1.2*np.exp(1)])
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower left',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk12-composite-eps3e-1.pdf',bbox_inches='tight')

plt.show()
