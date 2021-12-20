import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

n = sym.Symbol('n')
y = sym.Symbol('y')
z = sym.Symbol('z')
beta = sym.Symbol('beta')

a = sym.Rational(1,4)
b = sym.Rational(2,3)


y = sym.exp(-z)*z**(-n)


dy  = sym.diff(y,z)
ddy = sym.diff(dy,z)

eqn = ddy + dy + dy/z + beta*dy/z**2

eqn = sym.simplify(eqn)

latexeqn = str(sym.latex(eqn))


plt.text(0.5,0.5,r'$%s$'%latexeqn,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


