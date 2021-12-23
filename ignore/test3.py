# import sympy
from sympy import *

x = symbols('x')
exp = cos(x) + 7
print("Before Substitution : {}".format(exp)) 
    
# Use sympy.subs() method
res_exp = exp.subs(x, 0) 
    
print("After Substitution : {}".format(res_exp)) 