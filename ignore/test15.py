import sympy as sp
#import sympyMod as spM

#varibles = array
#values = array
#equation = sympy object

def spVar(variables):
    for var in variables:
        var = sp.symbols(var)
        print(var)

def spSolver1():
    pass
    

def spSolver(variables,values,equation):
    #Looping through variables array and converting variables to sympy objects 
    spVar(variables)

    #Generate sympy Equation
    eqn = sp.Eq(equation)

    #Finding the variable to solve for
    i,j = 0
    for val in values:
        if type(val) == str:
            missingVar = variables[i]
            j += 1
            if j != 0:
                print("More than one missing variable")
        else:
            i += 1

    #Solve Equation
    eqn1 =  sp.solve(eqn,missingVar)
    eqn2 = eqn1[0]
    #spM.solCheck(eqn1)            

    #Plug in values for numerical solution
    varPairs = []
    for i in range(len(variables)):
        if type(values[i]) != str:
            pair = (variables[i],equation[i])
            varPairs.append(pair)

    return eqn2.subs(varPairs)


if __name__ == "__main__":
    x = ["test1","test2","test3"]
    values = ["null",2,2]
    equation = "test1,test2/test3"
    spSolver(x,values,equation)