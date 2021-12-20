import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
plt.rc('text',usetex=True)

K = 0.1
nsteps = 1000

def integrand(u):
	return 1./np.sqrt( 1-(K*np.sin(u))**2 )

phi = np.linspace(0,2*np.pi,nsteps)
ellipticintegral = np.zeros(nsteps)

for pp in range(nsteps):
	ellipticintegral[pp] = quad( integrand,0,phi[pp] )[0]


plt.figure(1)
plt.plot(phi,integrand(phi),color='orange',label=r'$x$')
plt.plot(phi,ellipticintegral,color='blue',label=r'$x$')
plt.plot([0,2*np.pi],[2*np.pi,2*np.pi],'--')
plt.xlabel(r'$y$',size=20)
plt.ylabel(r'$u$',size=20)
#plt.yticks(np.linspace(-1,1,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':15})
plt.savefig('../pendulum.pdf',bbox_inchs='tight')


plt.show()
