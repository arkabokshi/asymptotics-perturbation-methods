import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature as quad
import math
plt.rc('text',usetex=True)

x = 4
scale = 50
s = np.linspace(1e-2,3,101)

plt.figure(1)
plt.plot(s,-s,'--',linewidth=2,color='green',label=r'$-s$')
plt.plot(s,np.log(s),'--',linewidth=2,color='blue',label=r'$\ln s$')
plt.plot(s,np.log(s)-s,linewidth=2,color='orange',label=r'$\ln s - s$')
plt.plot(s,scale*np.exp(x*(np.log(s)-s)),linewidth=2,color='gray',label=r'$\mathrm{e}^{x(\ln s - s)}$')
plt.xlabel(r'$s$',size=20)
plt.ylabel(r'$y(s)$',size=20)
#plt.yticks(np.linspace(0,1,11),fontsize=12.5)
#plt.xticks(np.linspace(0,2,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower right',prop={'size':12.5})
plt.savefig('../strogatz-wk04.pdf',bbox_inchs='tight')


plt.show()
