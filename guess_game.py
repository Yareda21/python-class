import random
import time
def Random_number_generator():
        guess = (random.randint(0,100))  
        chances = 5
       
        while chances > 0:
            guess_2 = int(input("your guess pls:- "))
            print("You have a comfort all right dont quit.its for my teacher.sacrifie to me")
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
                time.sleep(2)
        
            chances -=1
        
            if chances > 0:
                print(f"You have {chances} chances left.")
            elif chances== 0:
                print("*"*70)
                print(f"You have run out of chances. The number was {guess}.")
            if chances == 0:
                (budjet - 10)
                print( budjet - 10,"birr you have left")



if  __name__=="__main__":
    print("\t\tWelcome to my batting app\n")
    print("\n every time you lose you will lose 10 birr"
        "\n if you win well you will get the money")
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
