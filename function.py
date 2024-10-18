
print("yoram")
def temp_converter():
    # 1 degrees Celsius to Fahrenheit	F = ( 9 5 × 1 ) + 32
    print("welcome to temperture converter")

    custemer = input("Enter your unit f or c:_")
    if custemer == "f":
        temp = int(input("enter the number:_"))
        c =33.8 + temp
        print(c,"°c")

            
        
    else: custemer == "c"

    tempc = int(input("enter number:_"))
    f =9.5 + tempc
    print(f,"°f")

def calculator():
        
    while True:
        num1 = int( input("enter num : _"))
        opr = input("enter your symbol: _")
        num2 = int(input("enter your num:_"))



        if opr == "+":
            print(num1 + num2)
        elif opr == "-":
            print(num1 - num2)
        elif opr =="*":
            print (num1 * num2)
        elif opr =="/":
            print(num1 / num2)
        continue



print("\t\tWellcome to my applications:\n"
      "1. Temprature converter \n"
      "2. Calculator\n"
      )
choice = int(input("Enter: "))
if choice == 1:
    temp_converter()
elif choice == 2:
    calculator()
else:
    print("Wrong choice")
