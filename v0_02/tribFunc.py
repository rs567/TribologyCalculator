import sympy as sp
import spCalc as spC

#1.1 Friction Coefficent
def fric_coeff(vFric_coeff,vForce,vWeight):
    variables = ["fric_coeff","force","weight"]
    values = [vFric_coeff,vForce,vWeight]
    missingVar = spC.spNull(variables,values)

    fric_coeff,force,weight \
        =sp.symbols('fric_coeff force weight')
    spEqn = sp.Eq(fric_coeff,force/weight)

    return spC.spSolver(variables,values,spEqn,missingVar)

#3.1 Absolute Viscosity
def abs_visc(vabs_visc,vshear_stress,vshear_strain):
    variables = ["abs_visc","shear_stress","shear_strain"]
    values = [vabs_visc,vshear_stress,vshear_strain]
    missingVar = spC.spNull(variables,values)

    abs_visc,shear_stress,shear_strain \
        =sp.symbols("abs_visc shear_stress shear_strain")
    spEqn = sp.Eq(abs_visc,shear_stress/shear_strain)

    return spC.spSolver(variables,values,spEqn,missingVar)