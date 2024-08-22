op=["+","-","/","*"]
def cal(expression):
      for index in range(len(expression)):
            if expression[index] in op:
                  op=expression[index]
                  num1=expression[0:index]
                  num2=expression[index+1]


      if op=="+":
            return num1+num2
      if op=="-":
            return num1+num2
      if op=="*":
            return num1*num2 
      if op=="/":
            return num1/num2

      cal(expression)
