import scipy as sp
import sympy as sym
import matplotlib.pyplot as plt
from sympy.abc import a,b,c,t,tau
plt.rc('text',usetex=True)

# We have log(t)-t+1=-tau^2. If we want to solve for t, 
# we attempt a series solution
t = 1 + a*tau + b*tau**2 + c*tau**3 

# i.e. we want to expand
f = sym.log(t) - t + 1
expand = sym.series( f , tau, n=5 ).removeO()

# Finally we wish to equate the coefficients of tau
# to determine a,b,c
solution = sym.solve( expand+tau**2,(a,b,c) )

plt.text(0.5,0.5,r'$%s$'%sym.latex(solution), fontsize=25, \
	ha = 'center',va='center')
plt.show() 
