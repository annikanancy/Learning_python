num1=int(input("enter operand1: "))
num2=int(input("enter opearnd2: "))
operator=str(input("enter operator: "))
if operator=="+":
    print("result= ", num1+num2)
elif operator=="-":
    print("result= ", num1-num2)
elif operator=="*":
    print("result= ", num1*num2)
elif operator=="/":
    print("result= ", num1/num2)
elif operator=="%":
    print("result= ", num1%num2)    
else: print("INVALID OPERATION")
