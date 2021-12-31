import sympy as sp
import sympyMod as spM

#1.1 Friction Coefficent
def fric_coeff(vFric_coeff,vForce,vWeight):
    fric_coeff,force,weight=sp.symbols('fric_coeff force weight')
    eqn = sp.Eq(fric_coeff,force/weight) 
    
    #I need this to be in this form 
    # x = fric_coeff,force/weight
    # eqn = sp.Eq(x)

    return var3(vFric_coeff,vForce,vWeight,eqn)