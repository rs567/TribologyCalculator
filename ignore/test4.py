
import sympy as sp

x,y = sp.symbols('x y')

eqn = sp.Eq(x+13,y)
eqn.subs(y,0)
ans = sp.solve(eqn)
print(ans) #Output => [{x: y - 13}]
print(eqn) #Output => Eq(x + 13, y)
print(y) #Output => y

#I need to replace Y with a numbwer
#Then solve for X
#Then get a number output