database=("database")

while True:
      task = float(input("task -"))
      data = int(input("data -"))
      time = input("time -")
      taskelement = {
            "1:task":task ,
            "2:data":data ,
            "3:time":time 
      }

      database.append (taskelement)

      ask = input("do you want to contineu:yes/not -")
      if ask == "yes":
            continue
      else:
            break 

for index in range(len(database)):
            print(index +1,database[index])
            
