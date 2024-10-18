# this is where you declare all the class
import random
counter = 0
print("wellcome to chatbot:_")
while counter < 7:
    greeting = {
        "hi": [ "heyy" , "hello there"] ,
        "how are you": ["I am fine " , " doing good"],
        "what is your name" :["my name is Dello" , " you can call me Ahmed"],
        "what country is the best for studying I.T": ["America", "Spain", "UAE" ,"Ehtopia","any but not in africa"],
        "thanks":[ "welcome", "Anytime"]
    }

    talk = input(" : ")
    if talk == "hi":
        rand = random.randint(0,1)
        print(greeting ["hi"][rand])
        counter < 5   
    elif talk == "what is your name":
        rand = random.randint(0,1)
        print(greeting["what is your name"][rand])
        counter < 5
    elif talk == "how are you":
        rand = random.randint(0,1)
        print(greeting["how are you"][rand])
        counter < 5
    elif talk == "what country is the best for studying I.T":
        rand = random.randint(0,4)
        print(greeting["what country is the best for studying I.T"][rand])
        counter < 5 
    elif talk == "thanks":
        rand == random.randint(0,1)
        print(greeting["thanks"][rand])
        break
    