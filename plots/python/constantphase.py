import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
plt.rc('text', usetex=True)	# IMPORTANT FOR TEX


# SETUP
NX = 500
NY = 500

Xaxis = np.linspace(-3,3,NX)
Yaxis = np.linspace(-3,3,NY)
XX,YY = np.meshgrid(Xaxis,Yaxis)


# FUNCTION
#ZZ = np.power(XX,3) + 3.*XX - 3.*XX*np.power(YY,2)
ZZ = np.power(XX,2) - np.power(YY,2) - 1

fig,ax = plt.subplots()
#cs = ax.contour(XX,YY,ZZ,linewidths=3,levels=[-4,0,4], colors=['black','blue','green'])
cs = ax.contour(XX,YY,ZZ,linewidths=3,levels=[-2,-1,0], colors=['green','black','gray'])
ax.clabel(cs, fmt='%1.0f', fontsize=20)
plt.grid()
plt.show()
