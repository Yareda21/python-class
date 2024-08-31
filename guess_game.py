import random
neme = input("name: ")
conter = 0
while True:
      number =random.randint(0,50)
      while conter < 6:          
            guess = int(input("Enter guess: "))
            if number == guess:     
                  print("correct!!!")
                  print("congraguleion!!!" , neme)
                  
                  break
            elif number > guess:
                  print(" guess higer ")
                  conter = conter + 1
                  print("*" * 40)
                  print(conter)
            elif number < guess:
                  print("guess lower")
                  print("*" * 40)
                  conter = conter + 1
                  print(conter)
