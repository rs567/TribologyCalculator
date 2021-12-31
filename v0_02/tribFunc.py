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