import sympy as sp

import tribfunc as trib
import sympyMod as spM

#fric_coeff = trib.fric_coeff(5,2,2)

def testVar3():
    x,y,z = sp.symbols('x y z')
    eqn = sp.Eq(x,y/z)

    a = trib.var3("n",1,1,eqn)
    b = trib.var3(1,"n",1,eqn)
    c = trib.var3(1,1,"n",eqn)

    print(a,b,c)

def testsolcheck():
    spM.solCheck([1])
    spM.solCheck([1,1])
    spM.solCheck([1,1,1])
    spM.solCheck(["a"])


######### CALLS ######### 
pageBreak = "########################################### Page Break ###########################################"
print(pageBreak)
testVar3()
print(pageBreak)
testsolcheck()
print(pageBreak)