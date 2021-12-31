import sympy as sp
RHS = sp.sympify("gay+yesrser")
LHS = sp.sympify("y/yesy")

eqn = sp.Eq(RHS,LHS)
eqn1 = eqn.subs()
print(eqn)

