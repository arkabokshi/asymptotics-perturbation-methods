import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature as quad
import math
plt.rc('text',usetex=True)


t = np.linspace(0,2,201)
def func(x):
    return np.exp(-np.power(x,4))

numsoln = np.zeros(len(t))
fullarea = 0.25*math.gamma(1./4.)

for i in range(len(t)):
    localarea,err = quad(func,0,t[i])
    numsoln[i] = fullarea - localarea

ts = t[:-50]
tl = t[len(t)//100:]
small1_x = fullarea - (ts)
small2_x = fullarea - (ts - ts**5/5 )
small3_x = fullarea - (ts - ts**5/5 + ts**9/18)
large1_x = 1/4*np.exp(-tl**4)/tl**3 
large2_x = 1/4*np.exp(-tl**4)/tl**3 - 3/16/tl**7*np.exp(-tl**4) 

plt.figure(1)
plt.plot(t,numsoln,color='orange',label=r'$I_\mathrm{num}=\int_x^\infty \mathrm{e}^{-t^4} \mathrm{d}t$')
#plt.plot(t,func(t),'--',color='black',label=r'$e^{-t^4}$')
plt.plot(ts,small1_x,'--',color='blue', label=r'$I_\mathrm{ana} \sim I_0$')
plt.plot(ts,small2_x,'--',color='green',label=r'$I_\mathrm{ana} \sim I_0 + I_1$')
plt.plot(ts,small3_x,'--',color='gray', label=r'$I_\mathrm{ana} \sim I_0 + I_1 + I_2$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$I(x)$',size=20)
plt.yticks(np.linspace(0,1,11),fontsize=12.5)
plt.xticks(np.linspace(0,2,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.ylim([0,1])
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':10})
plt.title(r'$x \rightarrow 0$', fontsize=20)
plt.savefig('../strogatz-wk03-smallx.pdf',bbox_inchs='tight')


plt.figure(3)
plt.plot(t,numsoln,color='orange',label=r'$I(x)=\int_x^\infty \mathrm{e}^{-t^4} \mathrm{d}t$')
#plt.plot(t,func(t),'--',color='black',label=r'$e^{-t^4}$')
plt.plot(tl,large1_x,'--',color='green',label=r'$I_\mathrm{ana} \sim I_0$')
plt.plot(tl,large2_x,'--',color='blue', label=r'$I_\mathrm{ana} \sim I_0 + I_1$')
plt.xlabel(r'$x$',size=20)
plt.ylabel(r'$I(x)$',size=20)
plt.yticks(np.linspace(0,1,11),fontsize=12.5)
plt.xticks(np.linspace(0,2,11),fontsize=12.5)
plt.xticks(fontsize=12.5)
plt.grid(axis='both',linestyle='--')
plt.legend(loc='upper right',prop={'size':11})
plt.yscale('log')
plt.title(r'$x \gg 1$', fontsize=20)
plt.savefig('../strogatz-wk03-largex.pdf',bbox_inchs='tight')


plt.show()
