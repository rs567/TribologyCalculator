import sympy as sp
import spCalc as spC

#1.1 Friction Coefficent
def fric_coeff(vFric_coeff,vForce,vWeight):
    variables = ["fric_coeff","force","weight"]
    values = [vFric_coeff,vForce,vWeight]
    missingVar = spC.spNull(variables,values)

    fric_coeff,force,weight \
        = sp.symbols('fric_coeff force weight')
    spEqn = sp.Eq(fric_coeff,force/weight)

    return spC.spSolver(variables,values,spEqn,missingVar)

#3.1 Absolute Viscosity
def abs_visc(vAbs_visc,vShear_stress,vShear_strain):
    variables = ["abs_visc","shear_stress","shear_strain"]
    values = [vAbs_visc,vShear_stress,vShear_strain]
    missingVar = spC.spNull(variables,values)

    abs_visc,shear_stress,shear_strain \
        = sp.symbols("abs_visc shear_stress shear_strain")
    spEqn = sp.Eq(abs_visc,shear_stress/shear_strain)

    return spC.spSolver(variables,values,spEqn,missingVar)

#3.2 Kinematiic Viscosity
def kin_visc(vKin_visc,vAbs_visc,vDensity):
    variables = ["kin_visc","abs_visc","density"]
    values = [vKin_visc,vAbs_visc,vDensity]
    missingVar = spC.spNull(variables,values)

    kin_visc,abs_visc,density \
        =sp.symbols('kin_visc abs_visc density')
    spEqn = sp.Ep(kin_visc,abs_visc/density)

    return spC.spSolver(variables,values,spEqn,missingVar)

#3.3 ASTM D341 Viscosity-Temperature
def ASTM_D341(vkin_visc,vA,vB,vtemp):
    variables = ["kin_visc","A","B","temp"]
    values = [vkin_visc,vA,vB,vtemp]
    missingVar = spC.spNull(variables,values)

    #Check for negative inputs
    if vkin_visc-0.7 <= 0 or vtemp <= 0:
        print("Error: Values are negative")

    kin_visc,a,b,temp \
        =sp.symbols("kin_visc A B temp")
    spEqn = sp.Ep(sp.log(sp.log(kin_visc+0.7,10),10),
        a-b*sp.log(temp,10))

    return spC.spSolver(variables,values,spEqn,missingVar)



