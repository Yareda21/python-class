word=input("pls tell me ur word:- ")
count=0
symbols=["/"]


for letter in word:
      if letter in symbols:
            continue
else:
      count=count+1 

print("word count:",count)