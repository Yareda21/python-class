#This is the dice rolling simiulator
import random


def Random_number_generator():
        guess = (random.randint(1,6))  
        chances = 2
       
        while chances > 0:
            guess_2 = int(input("your number please from (1-6) :- "))
            if guess_2 < 1 or guess_2 > 6:
                 print("pls enter a number between 1 and 6")
                 continue
            
            if guess == guess_2:
                print("You got it right")
                return
            elif guess_2 > guess:
                print("your number is too huge")
            else:
                print("your guess is too low")

            chances -=1
            # every time you dont get the number it cancel one chance.
            if chances > 0:
                print(f"You have {chances} chances left.")
            else:
                print(f"You have run out of chances. The number was {guess}.")


#this is my code not stolen
#  this the code to excute the random number generator
Random_number_generator()