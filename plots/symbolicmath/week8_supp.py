import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

n = sym.Symbol('n')
i = sym.Symbol('i')
z = sym.Symbol('z')
s = sym.Symbol('s')
phi = sym.Symbol('phi')


phi = z**(-n-s)


dphi  = sym.diff(phi,z)
ddphi = sym.diff(dphi,z)

eqn = z*ddphi - 2*i*z*dphi + 2*i*phi

eqn = sym.simplify(eqn)

latexeqn = str(sym.latex(eqn))


plt.text(0.5,0.5,r'$%s$'%latexeqn,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


