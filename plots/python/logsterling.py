import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
import math
plt.rc('text', usetex=True)	# IMPORTANT FOR TEX


n = np.arange(1,4)
x = np.linspace(0.2,3.2,40)




gammafunc = np.zeros(len(x))
factorial = np.zeros(len(n))


for i in range(len(n)):
	factorial[i] = math.factorial(n[i])
for j in range(len(x)):
	gammafunc[j] = math.gamma(x[j]+1)

sterling  = np.sqrt(2.*np.pi*x) * np.power(x/np.exp(1.),x)


# FUNCTION

plt.plot(x,sterling,label=r'$\sqrt{2\pi n} (n/e)^n$')
plt.plot(x,gammafunc, label=r'$\Gamma(n+1)$')
plt.plot(n,factorial,'o', label=r'$n !$')
plt.grid()
plt.legend()
plt.show()
