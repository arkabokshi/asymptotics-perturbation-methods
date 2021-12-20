import sympy as sym
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)

t = sym.Symbol('t')

a = sym.Rational(-1,8)


j = sym.I
y = sym.exp(a*t*j)

r = a*( sym.exp(3*j*t) + sym.exp(-3*j*t) + 3*sym.exp(j*t) + 3*sym.exp(-j*t)  )
y1 = sym.exp(j*t)
y2 = sym.exp(-j*t)
W  = -2*j 

u = -1/W*sym.integrate(r*y2,t)
v = +1/W*sym.integrate(r*y1,t)

Yp = u*y1 + v*y2
#Yp = sym.simplify( Yp )
dYp = sym.diff( Yp,t )
dYp = sym.simplify(dYp)

latexOp = str(sym.latex(Yp))


plt.text(0.5,0.5,r'$%s$'%latexOp,fontsize=25, \
	horizontalalignment='center',verticalalignment='center')
plt.tick_params(axis='both',\
		bottom=False,left=False,\
		labelbottom=False,labelleft=False)
plt.show()


