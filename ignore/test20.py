import sympy as sp

[x,
y,z] = sp.symbols("x,y,z")
eqn = sp.Eq(x,y*z)
print(eqn.subs([(y,1),(z,2)]))
print(x,y,z)