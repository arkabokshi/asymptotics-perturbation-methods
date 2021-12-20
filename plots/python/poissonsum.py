import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.rc('text',usetex=True)
plt.rcParams.update({'font.size':25.0})


def fhat(x):
	return np.sin(0.055*x)*np.exp(-0.11*x*x)

eta = np.linspace(-15,15,300)
theta = np.linspace(-20,20,400)
mm = np.arange(-6,7)

ftheta = np.zeros([len(theta),len(mm)])

for tt in range(len(mm)):
	ftheta[:,tt] = fhat(theta+2.*np.pi*mm[tt])

plt.figure(1)
plt.plot(eta,fhat(eta),color='orange',linewidth=2.5,label=r'$\hat{f}(\eta)=\sin(0.055 \eta)*\exp(-0.11\eta^2)$')
plt.grid(color='gray',linestyle='dotted',linewidth=0.5)
#plt.legend(prop={'size':15})
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\hat{f}(\eta)$')
plt.savefig("../poissonsum_1.pdf",bbox_inches='tight')

plt.figure(2)
plt.plot(theta,ftheta,linewidth=2.0)
plt.grid(color='gray',linestyle='dotted',linewidth=0.5)
#plt.legend(prop={'size':10})
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\hat{f}(\theta+2 \pi m)$')
plt.savefig("../poissonsum_2.pdf",bbox_inches='tight')

plt.figure(3)
plt.plot(theta,np.sum(ftheta,-1),color='blue',linewidth=2.5)
plt.grid(color='gray',linestyle='dotted',linewidth=0.5)
#plt.legend(prop={'size':10})
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\sum_m \hat{f}(\theta+2\pi m)$')
plt.savefig("../poissonsum_3.pdf",bbox_inches='tight')

plt.show()
