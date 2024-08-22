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
            chances -=1
        
            if chances > 0:
                print(f"You have {chances} chances left.")
            else:
                print(f"You have run out of chances. The number was {guess}.")
Random_number_generator()