# the given operartors in which the user have to input
given_operators = ["+","-","*","/"]
# intordution
expression_two = input("\t Welcome to my calculator app.\n "
                   "pls use these sign other than this the app will crash so use this signs.\n"
                   "+,/,*,-,** \n"
                   "pls give me your number and the operator with it:-")


def cal(expression: str) -> int:
    for index in range (len(expression)):
        if expression[index] in given_operators:
                operators = expression[index]
                num1 = float(expression[0:index])
                num2 = float(expression[index+1:])
    # the operators how to fucnction
    if operators== "+":
        return num1 + num2
    elif operators=="-":
         return num1-num2
    elif operators=="*":
        return num1*num2
    elif operators== "/":
        return num1/num2
    elif operators=="**":
        return num1**num2
    else: 
        return "Invalid input"
    
# to run the calculator
result= cal(expression_two)
print(result)
