oper1 = input("Please enter operator to user like(+ ,- .* , /) :")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
val1= str(num1) + oper1 + str(num2)
list1 = ['+','-','*','/']
if oper1 not in list1:
    print("Please enter the valid operator like(+, - ,* ,/)")
elif val1 == "45*3":
    print("The * of given two number is = 555")
elif val1 == "56+9":
    print("The + of given two number is = 77")
elif val1 == "56/6":
    print("The / of given two number is = 4")
elif(oper1 == "+"):
    print("The + of given two number is = ", num1 + num2)
elif(oper1 == "-"):
    print("The - of given two number is = " , num1 - num2)
elif(oper1 == "*"):
    print("The * of given two number is = " , num1 * num2)
else:
    print("The / of given two number is = " , num1 / num2)

import  arcpy
