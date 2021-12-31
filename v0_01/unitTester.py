import sympy as sp

import tribfunc as trib
import sympyMod as spM

#fric_coeff = trib.fric_coeff(5,2,2)

def testVar3():
    x,y,z = sp.symbols('x y z')
    eqn = sp.Eq(x,y/z)

    a = trib.var3("n",1,1,eqn)
    print("n,1,1: " + str(a==1))
    b = trib.var3(1,"n",1,eqn)
    print("1,n,1: " + str(b==1))
    c = trib.var3(1,1,"n",eqn)
    print("1,1,n: " + str(c==1))

    print(a,b,c)

def testsolcheck():
    spM.solCheck([1]) #Pass
    spM.solCheck(["a"]) #Pass
    spM.solCheck([1,1]) #Fail
    spM.solCheck([1,1,1]) #Fail
    
def testFric_coeff():
    a = trib.fric_coeff("str",1,2)

######### CALLS ######### 
pageBreak = "########################################### Page Break ###########################################"
print(pageBreak)
print("##### testVar3")
testVar3()
print(pageBreak)
print("##### testsolcheck")
testsolcheck()
print(pageBreak)
print("##### testFric_coeff")
testFric_coeff()

