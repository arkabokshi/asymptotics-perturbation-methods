import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature as quad
from scipy import special
import math
plt.rc('text',usetex=True)

t = np.linspace(0,4,2000)

plt.figure(1)
plt.plot(t,np.cos(4*(t**3/3-t)),linewidth=1.5,color='gray',label=r'$\cos[4(t^3/3-t)]$')
plt.plot(t,np.cos(2*(t**3/3-t)),linewidth=2.0,color='orange',label=r'$\cos[2(t^3/3-t)]$')
plt.plot(t,np.cos(2*(-2/3+(t-1)**2)),'--',linewidth=1.5,color='blue',label=r'$\cos[2(-2/3 + (t-1)^2)]$')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$y(t)$',size=20)
#plt.yticks(np.linspace(0,1,11),fontsize=12.5)
#plt.xticks(np.linspace(0,2,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='lower left',prop={'size':12.5})
plt.savefig('../strogatz-wk05-cos.pdf',bbox_inches='tight')

plt.figure(2)
x = np.linspace(1e-2,12,150)
approx = np.sqrt(2/(np.pi*x))*np.cos(x-np.pi/4)
plt.plot(x,approx,linewidth=2.0,label=r'$\sqrt{\frac{2}{\pi x}} \cos (x-\pi/4)$')
plt.plot(x,special.jv(0,x),linewidth=2.0,label=r'$J_0(x)$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'Bessel(x)',size=20)
plt.ylim([-0.5,1.3])
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='best',prop={'size':12.5})
plt.savefig('../strogatz-wk05-bessel.pdf',bbox_inches='tight')

plt.show()
