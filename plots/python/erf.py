import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.rc('text',usetex=True)
plt.rcParams.update({'font.size':20.0})

def gaussian(u):
	return 2./np.sqrt(np.pi)*np.exp(-u*u)


def erf(x):
	return integrate.quad( gaussian,0.0,x )

xx = np.linspace(-2,2,1000)
yy = np.zeros(len(xx))
zz = np.zeros(len(xx))


for ii in range(len(xx)):
	yy[ii] = erf(xx[ii])[0]
	zz[ii] = 1.-yy[ii]


plt.plot(xx,gaussian(xx),label=r'$f(x) = \frac{2}{\sqrt{\pi}} \exp(-x^2)$',color='gray',linestyle='dashed',linewidth=1.5)
plt.plot(xx,yy,label=r'$\mathrm{erf}(x)$',color='blue',linewidth=2.0)
plt.plot(xx,zz,label=r'$\mathrm{erfc}(x)$',color='green',linewidth=2.0)
plt.grid(color='gray',linestyle='dotted',linewidth=0.5)
plt.legend(prop={'size':12.5})
plt.savefig("../erf.pdf",bbox_inches='tight')
plt.show()

