def test(vkin_visc,vtemp):
    print(vkin_visc-0.7 <= 0)
    print(vtemp <= 0)
    print(vkin_visc-0.7 <= 0 or vtemp <= 0)

    if vkin_visc-0.7 or vtemp <= 0:
       print(vkin_visc,vtemp) 
       print("Error: Values are negative")
       print("\n")
    else:
        print("pass")
        print("\n")

    #print("program run")
    #print(vkin_visc-0.7 <= 0)
    #print(vtemp <= 0)
    #print(vkin_visc-0.7 <= 0 or vtemp <= 0)

test(0.7,-1)#Fail,Fail
test(0.8,-1)#Fail,Fail
test(0.7,1)#Fail,Pass
test(0.8,1)#Fail,Pass

print(0.8-0.7)
print("good")