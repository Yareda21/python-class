# imported numbers and time to do in my code
import random
import time


# this is the function to operate
def Random_number_generator():
        # i gave thenumber limit and the chances to play
        guess = (random.randint(0,100))  
        chances = 5
       
        # this is the hile loop to rep 
        while chances > 0:
            guess_2 = int(input("your guess pls:- "))
            print("You have a comfort all right dont quit.its for my teacher.sacrifie to me")
            
             # this is the conition about the functions 
            if guess == guess_2:
                print("YOu got it right")
                time.sleep(2)
                print(budjet+10 ,"birr you have left")
                return
            
            
            elif guess_2 > guess:
                print("your number is too huge")
                print("*"*70)

                time.sleep(2)
            
            
            else:
                print("your guess is too low")
                print("*"*70)
                # this is the code that counts 2 secound  
                time.sleep(2)
        
            
            # this is the code that deductes the chances if you miss
            chances -=1
        

            if chances > 0:
                print(f"You have {chances} chances left.")
        
        
            elif chances== 0:
                print("*"*70)
                print(f"You have run out of chances. The number was {guess}.")
        
        
            if chances == 0:
                (budjet - 10)
                print( budjet - 10,"birr you have left")


# this the code which do the code
if  __name__=="__main__":
    print("\t\tWelcome to my batting app\n")
    print("\n every time you lose you will lose 10 birr"
        "\n if you win well you will get the money")
    # this is the part which asks the user to input its budjet 
    budjet= int (input("\n enter you budget you want to bet?"))

    
    while True:
        print(
                print("*"*70),
            time.sleep(2),
            "\t do you want to continue?\n"
            "\tPlease select:\n"
            "1. yes\n"
            "2. No \n"
            )
    
    
        try:
            choice = int(input("Enter choice: - "))
    
    
        except ValueError:
            print("Please enter number only!!")
    
    
        if choice == 1:
            print("\tyou have joined the game\n")
            Random_number_generator()
            continue
    
    
        if choice == 2:
            print("Good bye")
            break


     
     
