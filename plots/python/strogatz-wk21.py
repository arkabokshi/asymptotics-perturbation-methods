import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.special import airy
plt.rc('text',usetex=True)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 12.5
plt.rcParams['ytick.labelsize'] = 12.5


y = np.linspace(-2.3,2.3,100)
dydt = y - y**3/3

plt.figure(1)
plt.plot(y,dydt,color='blue',label=r'$f(y)$')
plt.plot(y,dydt-0.5,'--',color='blue',label=r'$f(y)-0.5$')
plt.scatter([0,np.sqrt(3),-np.sqrt(3)],[0,0,0])
plt.plot(y,dydt-1.0,linestyle='dotted',color='blue',label=r'$f(y)-1.0$')
plt.scatter([np.sqrt(3),-np.sqrt(3)],[0,0])
plt.xlabel(r'$y$')
plt.ylabel(r'$\mathrm{d}y/\mathrm{d}\tau$')
#plt.ylim([-7.5,5])
plt.legend(loc='lower left',prop={'size':12.5})
plt.grid(axis='both',linestyle='--')
plt.savefig('../pdf/strogatz-wk21.pdf',bbox_inches='tight')

plt.figure(2)
y = np.linspace(-2,2,100)
t = y - np.power(y,3)/3
plt.plot(t,y,color='blue')
plt.grid(axis='both',linestyle='--')
plt.xlabel(r'$t$')
plt.ylabel(r'$y_0$')
plt.savefig('../pdf/strogatz-wk21-layers.pdf',bbox_inches='tight')


plt.figure(3)
x = np.linspace(-3,5,300)
ai,aip,bi,bip = airy(-x)
plt.plot(x,-aip/ai,linewidth=2.,label=r'$-\mathrm{Ai}^\prime(-x)/\mathrm{Ai}(-x)$')
plt.plot(x,ai,linewidth=2.,label='$\mathrm{Ai}(-x)$')
plt.ylim([-2,2])
plt.grid(axis='both',linestyle='--')
plt.xlabel(r'$\tilde{t}$')
#plt.ylabel(r'$\mathrm{Ai}\prime / \mathrm{Ai}$')
plt.legend(loc='lower left',prop={'size':12.5})
plt.savefig('../pdf/strogatz-wk21-aip_ai.pdf',bbox_inches='tight')


plt.figure(4)
y = np.linspace(-2.3,2)
plt.plot(y,y-y**3/3-2/3,color='orange',linewidth=2.0)
plt.scatter([-2,1],[0,0])
plt.grid(axis='both',linestyle='--')
plt.xlabel(r'$Y_0^\ast$')
plt.ylabel(r'$\mathrm{d}Y_0^\ast / \mathrm{d}t^\ast$')
plt.savefig('../pdf/strogatz-wk21-interior.pdf',bbox_inches='tight')

plt.show()
