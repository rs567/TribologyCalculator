def solCheck(eqn):
    if len(eqn) != 1:
        x=[]
        print("solCheck: Potetial sympy issue, multiple solutions")
        print(eqn)
    else:
        print("solCheck: Successful")
        print(eqn)
