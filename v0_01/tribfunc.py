import sympy as sp
import sympyMod as spM

#1.1 Friction Coefficent
def fric_coeff(vFric_coeff,vForce,vWeight):
    fric_coeff,force,weight=sp.symbols('fric_coeff force weight')
    eqn = sp.Eq(fric_coeff,force/weight)
    return var3(vFric_coeff,vForce,vWeight,eqn)
    
#3.1 Absolute Viscosity
def abs_visc(abs_visc,shear_stress,shear_strain):
    abs_visc = shear_stress/shear_strain

#3.2 Kinematic Visosity
def kin_visc(kin_visc,abs_visc,density):
    kin_visc = abs_visc/density

# #3 Variable solver Structure
# def var3(vx,vy,vz,eqnSym,eqn):
#     str_symbols = str(x) + " " + str(y) + " " + str(z)
#     x,y,z = sp.symbols(str_symbols) #can't suppress
#     #eqn = sp.Eq(x,y/z)
#     print(type(vx))
#     if type(vx) == str:    
#         eqn1 = sp.solve(eqn,x)
#         eqn2 = eqn1[0]
#         spM.solCheck(eqn1)
#         return eqn2.subs([(y,vy),(z,vz)])
 
#     elif type(vy) == str:
#         eqn1 = sp.solve(eqn,y)
#         eqn2 = eqn1[0]
#         spM.solCheck(eqn1)
#         return eqn2.subs([(x,vx),(z,vz)])

#     elif type(vz) == str:
#         eqn1 = sp.solve(eqn,z)
#         eqn2 = eqn1[0]
#         spM.solCheck(eqn1)
#         return eqn2.subs([(x,vx),(y,vy)])

#     else:
#         print("Fatal Error: Check Inputs")

#varibles = array
#values = array
#equation = sympy object

def varSolver(variables,values,equation):

    #Looping through variables array and converting variables to sympy objects 
    for var in variables:
        var = sp.symbols(var)
    
    

