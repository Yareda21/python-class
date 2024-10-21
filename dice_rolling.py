import random
while True:
    print("Welcome to dice game")
    number = random.randint(1 , 14)
    gamer = int(input("Enter the number your betting on:_"))
   
    if gamer == number:
        print("You won the bet")
        break

    elif gamer != number:
       print("U lost the bet")           
       break

    gamer = input("Do you want to continue:_")    
    if gamer == "no":
        quit()  
    elif gamer == "yes":
        continue 