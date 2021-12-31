#WORKING VERSION
import sympy as sp

def spNull(variables,values):
    i,j = 0,0
    for val in values:
        if type(val) == str:
            missingVar = variables[i]
            j += 1
            if j != 1:
                print("More than one missing variable")
        else:
            i += 1
        if j >= 2:
            print("Over defined")
    return missingVar    

#Main Solver
def spSolver(variables,values,spEqn,missingVar):
    eqn1 = sp.solve(spEqn,missingVar)
    eqn2 = eqn1[0]

    varPairs = []
    for i in range(len(variables)):
        if type(values[i]) != str:
            pair = (variables[i],values[i])
            varPairs.append(pair)

    return eqn2.subs(varPairs)

#1.1 Friction Coefficent
def fric_coeff(vFric_coeff,vForce,vWeight):
    variables = ["fric_coeff","force","weight"]
    values = [vFric_coeff,vForce,vWeight]
    missingVar = spNull(variables,values)

    fric_coeff,force,weight=sp.symbols('fric_coeff force weight')
    spEqn = sp.Eq(fric_coeff,force/weight)

    return spSolver(variables,values,spEqn,missingVar)

if __name__ == "__main__":

    #Check Null Location
    print("#### Case 1.1 ####")
    assert fric_coeff("null",1,1) == 1
    print("#### Case 1.2 ####")
    assert fric_coeff(1,"null",1) == 1
    print("#### Case 1.3 ####\n")
    assert fric_coeff(1,1,"null") == 1

    #Fractions
    print("#### Case 2.1 ####")
    assert fric_coeff("null",1,2) == 0.5
    print("#### Case 2.2 ####")
    assert fric_coeff("null",1,3) == sp.Rational(1,3)
