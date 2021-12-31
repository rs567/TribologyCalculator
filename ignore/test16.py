import sympy as sp
#import sympyMod as spM

##Convert cariables to sympy objects
#    #Input: Variables (array)
#def spVar(variables):
#    global var
#    for var in variables:
#        var = sp.symbols(var)
#        print(var)
#        return var
    

#Finding the variable to solve for
    #Checks for more than one missing variable
def spNull(variables,values):
    i,j = 0
    for val in values:
        if type(val) == str:
            missingVar = variables[i]
            j += 1
            if j != 0:
                print("More than one missing variable")
        else:
            i += 1
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
    variables = ["Fric_coeff","Force","Weight"]
    values = [vFric_coeff,vForce,vWeight]

    fric_coeff,force,weight=sp.symbols('fric_coeff force weight')
    eqn = sp.Eq(fric_coeff,force/weight)

    


#def fric_coeff(vFric_coeff,vForce,vWeight):
#    variables = ["Fric_coeff","Force","Weight"]
#    spVar(variables)
#    eqn = sp.Eq(Fric_coeff,Force/Weight)
#
#fric_coeff(1,1,1)