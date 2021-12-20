import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

# Define kth term of series
def ak(k):
	return np.power(-1,k+1) / float(k)

# Partial sum of ak summing n terms = An
def partialsum_ak(n):
	an = 0.
	for ii in range(1,n+1):
		an += ak(ii)
	return an


# Shanks transform
def Shanks(Anmin,An,Anplus):
	S_An = (Anplus*Anmin - An*An) / ( Anplus + Anmin -2.*An )
	return S_An


## MAIN ##

NN = 37
ShanksOrder = 3
An = np.zeros([NN,ShanksOrder+2],dtype=np.longdouble)
Er = np.zeros([NN,ShanksOrder+2],dtype=np.longdouble)

An[:,0] = np.arange(1,NN+1)

# creating array with partial sums An
# NB: This is slowly convergent 
for ii in range(NN):
	An[ii,1] = partialsum_ak(ii+1)

# First Shanks S(An)
An[0,2] = An[-1,2] = np.nan
for ii in range(1,NN-1):
	An[ii,2] = Shanks(An[ii-1,1],An[ii,1],An[ii+1,1])

# Second Shanks S(S(An))
An[:2,3] = An[-2:,3] = np.nan
for ii in range(2,NN-2):
	An[ii,3] = Shanks(An[ii-1,2],An[ii,2],An[ii+1,2])

# Third Shanks S(S(S(An)))
An[:3,4] = An[-3:,4] = np.nan
for ii in range(3,NN-3):
	An[ii,4] = Shanks(An[ii-1,3],An[ii,3],An[ii+1,3])


# Error
AbsErr = np.abs(An-np.log(2))


# PRINTING & PLOTTING	
np.set_printoptions(precision=7)
print(An)

plt.rc('text', usetex=True)	# IMPORTANT FOR TEX
plt.plot(An[4:30,0],AbsErr[4:30,1],'-o',markerfacecolor="None", label=r'$|A_n - \log 2|$')
plt.plot(An[4:30,0],AbsErr[4:30,2],'-o',markerfacecolor="None", label=r'$|S(A_n)-\log 2|$')
plt.plot(An[4:30,0],AbsErr[4:30,3],'-o',markerfacecolor="None", label=r'$|S^2(A_n)-\log 2|$')
plt.plot(An[4:30,0],AbsErr[4:30,4],'-o',markerfacecolor="None", label=r'$|S^3(A_n)-\log 2|$')
plt.ylim([1e-13,1e-1])
plt.legend()
plt.loglog()
plt.show()
