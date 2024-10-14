### 3.	Guess the Number Game: 
#Implement a simple number guessing game where the computer generates a random number, and the player tries to guess it. Provide hints like "too high" or "too low" after each guess, and keep track of the number of attempts.

counter = 0

while counter < 4: 

    number = 7
    
    guess = int(input("enter your guess: _"))
    if number == guess:
        print("you guessed correct")
        break

        
    elif number != guess: 
        
        print("the guess is wrong") 
        counter += 1
        
                