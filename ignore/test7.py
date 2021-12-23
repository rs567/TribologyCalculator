import sympy as sp
x,y = sp.symbols('x y')
eqn = sp.Eq(x+10,y)

#if conditions (choose what variable to solve for)
eqn1 = sp.solve(eqn)[0][x]
print(eqn1.subs(y,0))
#returns -10