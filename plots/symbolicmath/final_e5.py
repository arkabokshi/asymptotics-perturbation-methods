import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

k = sym.Symbol('k')
s = sym.Symbol('s')
u = sym.Symbol('u')
x = sym.Symbol('x')
eps = sym.Symbol('epsilon')

u = x**(k+s)


du  = sym.diff(u,x)
ddu = sym.diff(du,x)

eqn = x*ddu + du -x*u - eps/x*u

eqn = sym.simplify(eqn)

latexeqn = str(sym.latex(eqn))


plt.text(0.5,0.5,r'$%s$'%latexeqn,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


