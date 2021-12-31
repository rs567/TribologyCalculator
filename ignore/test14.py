import sympy as sp

## From this 
x,y,z = sp.symbols("x y z")
sp.Ep(x,y/z)

## To this 

#varibles = array
#equation = ????
def solver(variables,equation):
    #Looping through variables array and converting variables to sympy objects 
    for var in variables:
        var = sp.symbols(var)
    
    #Generate sympy Equation
    equation = sp.Ep(equation)

