import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
plt.rc('text', usetex=True)	# IMPORTANT FOR TEX
plt.rcParams.update({'font.size':15.0})

def line(c):
	return xx*c + c*c

Nx = 500
Nc = 30
xx = np.linspace(-20,20,Nx)
cc = np.linspace(-10,10,Nc)

yy = np.zeros([Nx,Nc])

for jj in range(Nc):
	yy[:,jj] = line(cc[jj])

# SETUP

fig,ax = plt.subplots()
plt.plot(xx,yy[:,:],color='gray',linestyle='solid',linewidth=0.5)
plt.plot(xx,line(cc[Nc/2]),color='gray',linestyle='solid',linewidth=0.5,label=r'$y_g=cx+c^2$')
plt.plot(xx,-xx*xx/4., color='blue',linewidth=2.0, label=r'$y_s=-x^2/4$')
plt.grid()
plt.ylim([-50,50])
plt.legend()
plt.savefig("../clairuteqn.pdf",bbox_inches='tight')
plt.show()
