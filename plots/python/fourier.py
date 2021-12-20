import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.rc('text',usetex=True)
plt.rcParams.update({'font.size':20.0})

wavelen = 3.
wavenum = 1. #2.*np.pi/wavelen
boxlen  = 50 #4.*wavelen
NN = 50

xx = np.linspace(-boxlen,boxlen,500)
nn = np.arange(0,NN+1)
print(nn)

deltak_1  = 0.005*wavenum * 0.5
deltak_2  = 0.005*wavenum * 1.0
deltak_3  = 0.005*wavenum * 2.0


fx_1 = np.zeros(len(xx))
fx_2 = np.zeros(len(xx))
fx_3 = np.zeros(len(xx))

for jj in range(len(nn)):
	fx_1 += np.sin(xx*(wavenum+nn[jj]*deltak_1))
	fx_2 += np.sin(xx*(wavenum+nn[jj]*deltak_2))
	fx_3 += np.sin(xx*(wavenum+nn[jj]*deltak_3))


plt.plot(xx,fx_1,color='gray',linestyle='solid',linewidth=2.0,label=r'$\Delta k = %.4f$'%deltak_1)
plt.plot(xx,fx_2,color='orange',linestyle='solid',linewidth=2.0,label=r'$\Delta k = %.4f$'%deltak_2)
plt.plot(xx,fx_3,color='blue',linestyle='solid',linewidth=2.0,label=r'$\Delta k = %.4f$'%deltak_3)
plt.grid(color='gray',linestyle='dotted',linewidth=0.5)
plt.legend(prop={'size':10})
#plt.ylim([-50,70])
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.savefig("../fourier.pdf",bbox_inches='tight')
plt.show()

