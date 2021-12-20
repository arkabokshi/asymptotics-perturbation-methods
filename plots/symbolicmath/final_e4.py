import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

x = sym.Symbol('x')
y = sym.Function('y')(x)
p = sym.Function('p')(x)
i = sym.Symbol('i')
eps = sym.Symbol('epsilon')

dy = (i/eps)*y*p

ddy = sym.diff(dy,x)
ddy_sub = ddy.subs(sym.diff(y,x),(i/eps)*y*p)

dddy = sym.diff(ddy_sub,x)
dddy_sub = dddy.subs(sym.diff(y,x),(i/eps)*y*p)

eqn = (eps**3)*dddy_sub + 3*eps*dy - i*x*y

eqn = sym.limit(eqn,eps,0)
eqn = sym.simplify(eqn)

latexeqn = str(sym.latex(eqn))


plt.text(0.5,0.5,r'$%s$'%latexeqn,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


