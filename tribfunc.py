import sympy as sp
import sympyMod as spM

#1.1 Friction Coefficent
def fric_coeff(fric_coeff,force,weight):
    eqn = sp.Eq(fric_coeff,force/weight)

#3.1 Absolute Viscosity
def abs_visc(abs_visc,shear_stress,shear_strain):
    abs_visc = shear_stress/shear_strain

#3.2 Kinematic Visosity
def kin_visc(kin_visc,abs_visc,density):
    kin_visc = abs_visc/density


#Sample Function Structure
def var3(x1,y1,z1,eqn):
    x,y,z = sp.symbols('x y z') #can't suppress
    #eqn = sp.Eq(x,y/z)
    if type(x1) == str:    
        eqn1 = sp.solve(eqn,x)
        eqn2 = eqn1[0]
        spM.solCheck(eqn1)
        return eqn2.subs([(y,y1),(z,z1)])
 
    elif type(y1) == str:
        eqn1 = sp.solve(eqn,y)
        eqn2 = eqn1[0]
        spM.solCheck(eqn1)
        return eqn2.subs([(x,x1),(z,z1)])

    elif type(z1) == str:
        eqn1 = sp.solve(eqn,z)
        eqn2 = eqn1[0]
        spM.solCheck(eqn1)
        return eqn2.subs([(x,x1),(y,y1)])

    else:
        print("Fatal Error: Check Inputs")

