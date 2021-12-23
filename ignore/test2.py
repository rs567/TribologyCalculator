# import sympy
from sympy import *
  
x, y = symbols('x y')
exp = x**2 + 1
print("Before Substitution : {}".format(exp)) 
    
# Use sympy.subs() method
res_exp = exp.subs(x, y) 
    
print("After Substitution : {}".format(res_exp))