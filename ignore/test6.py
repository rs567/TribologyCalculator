
import sympy as sp

x,y = sp.symbols('x y')

eqn = sp.Eq(x+13,y)
#eqn.subs(y,0)
ans = sp.solve(eqn)
#print(ans) #Output => [{x: y - 13}]
#print(eqn) #Output => Eq(x + 13, y)
#print(y) #Output => y
#
#print(ans[0][x])

eqn1 = ans[0][x]
eqn1.subs(y,0)
print(eqn1.subs(y,0))