import random
greet = {
    "hi" : ["hi", "how are you"],
    "How are you" : ["great wbu" , "Doing better"] ,
}

rand = random.randint(0,1)
print(greet["hi"][rand])

