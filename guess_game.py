import random



balance=int(input("enter amount of money u want to deposit: -"))
def random_number_generetor():
      guess = random.randint(0,100)
      counter = 0
      while counter < 5:
            guess_2=int(input("your guess pls:- "))

            if guess == guess_2:
                  print("u r correct u win 10 birr") 
                  balance = balance + 10
                  break
            elif guess_2< guess: 
                  print("guess higher")
                  counter = counter + 1
                  balance=balance-10
            elif guess_2 > guess:
                  counter = counter + 1
                  print("guess lower")
                  balance=balance-10

            

            if counter == 5:
                  balance = balance - 10

random_number_generetor()

