while True:
    num1=int(input("Enter number:"))
    num2=int(input("Enter number:"))
    operator=input("Enter operator:")

    if operator=="+":
        addition=num1+num2
        print(addition)
    elif operator=="-":
        subtraction=num1-num2
        print(subtraction)
    elif operator=="*":
        multiply=num1*num2
        print(multiply)
    elif operator=="/":
        division=num1/num2
        print(division)
    elif operator=="%":
        remainder=num1%num2
        print(remainder)
    quit=input("continue(y/n):")
    if quit=="y":
        continue
    else :
        break
