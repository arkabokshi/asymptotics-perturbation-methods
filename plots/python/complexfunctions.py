import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

i = np.complex(0.0,1.0)
print(i)

Nx = 100
Ny = 100
realt = np.linspace(-3,3,Nx)
imagt = np.linspace(-4,4,Ny)

complexfunc = np.zeros([Nx,Ny],dtype=complex)

realAx,imagAx = np.meshgrid(realt,imagt)

L = 1.
for rr in range(Nx):
	for ii in range(Ny):
		t = complex(realt[rr],imagt[ii])
		complexfunc[rr,ii] = np.exp(L*t +np.power(t,2)/2.0) / np.sqrt(t*t-1.0)
		#complexfunc[rr,ii] = 1.0

plt.contourf(realAx,imagAx,complexfunc.real)
plt.colorbar()
plt.show()
		
 
