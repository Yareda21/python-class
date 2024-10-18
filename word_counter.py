user = input("Heollo tell me about your day: _")
counter = 0



for x in user:
    if x == " ":
       counter += 1
    
    
print("Number of words: ", counter)

