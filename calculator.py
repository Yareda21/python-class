while True:
    num1 =input("num1: -")
    num2 =input("num2: -")
    operator =input("+, -, /, *: -")
    if operator =="+":
        print(num1+num2)
    elif operator =="-":
        print(num1-num2)
    elif operator =="/":
        print(num1/num2)
    elif operator =="*":
        print(num1*num2)
    else:
        print("invalid")

