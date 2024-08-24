#This is the dice rolling simiulator
import random

def Random_number_generator():
        guess = (random.randint(1,6))  
        chances = 2
       
        while chances > 0:
            guess_2 = int(input("your number please:- "))
            if guess == guess_2:
                print("YOu got it right")
                return
            elif guess_2 > guess:
                print("your number is too huge")
            else:
                print("your guess is too low")
# this is the codes that will happen if you dont get the number.
            chances -=1
# every time you dont get the number it cancel one chance.
            if chances > 0:
                print(f"You have {chances} chances left.")
            else:
                print(f"You have run out of chances. The number was {guess}.")
# this the code to excute the random number generator
Random_number_generator()