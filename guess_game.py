import random 
while True:
    print("Welcome & lets start the game")
    number = random.randint(1 , 100)
    counter = 0
    while counter < 100:
                    guess = int(input("enter your guess: _"))
                    if number == guess:
                        print("You guess correct")
                        break

                    elif number < guess:
                        print("Guess lower:")
                        counter += 1
                    
                    elif number > guess:
                        print("Guess higher:")    
                        counter += 1
    print("Game over!!!")                       
    gamer = input("do want to continue:_")
    if gamer == "no":
          quit()
    elif gamer == "yes":
          continue 