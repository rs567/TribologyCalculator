from sympy import *
x,y,z = symbols("x y z")

expr = x + y + 1
expr.subs([(x,1),(y,1)])
answer = solve(expr)
print(answer)

