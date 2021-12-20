import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

n = sym.Symbol('n')
y = sym.Symbol('y')
z = sym.Symbol('z')

a = sym.Rational(1,4)
b = sym.Rational(2,3)


w = z**(-a)*sym.exp(b*z**(1/b))
y = w*z**(-n/b)


dy  = sym.diff(y,z)
ddy = sym.diff(dy,z)
ddy -= z*y
ddy = sym.simplify(ddy)

latexddy = str(sym.latex(ddy))


plt.text(0.5,0.5,r'$%s$'%latexddy,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


