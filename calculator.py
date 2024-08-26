num1=int(input("num1: - "))
num2=int(input("num2: - "))
operator= input("+,/,-,*")
if operator == "+":
    print(num1+num2)
elif operator == "/":
    print(num1/num2)
if operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
else:
    print("invalid")

