# output

# print("Hello world!!!")

# name = input("Enter your name: ")

# print("Hello", name)

# age = input("plesae tell me your age ")
# print("your age is ", age)

# # data structure 
#         name   fname   age   course   schedule pay
# list      0           1       2       3       4
# yoram1 = ["Yoram", "Simon", "Python", "MWF", 7400]

# yoram2 = {
#     "Name" : "Yoram", 
#     "Father Name" : "Simon"
# }



# for data in yoram1:
#     print(data)
    
# print(len(yoram1))

# for number in range(10):
#     print(number)

# for index in range(len(yoram1)):
#     print(index+1, " - ",  yoram1[index])

# NEW
store = []

# for number in range(3):
#     name = input("Enter name: - ")
#     print("Name Submited: ")
#     store.append(name)



# print("List of names: ")
# for x in range(len(store)):
#     print(x+1, " - ", store[x])

while (True):
    name = input("Enter name: - ")
    print("Name Submited: ")
    store.append(name)

    ask = input("Do you want to quit?")
    if ask == "yes":
        break
    else:
        continue


# NEW

# conditional - decision making 


email = input("enter email: ")
password = input("Enter password: ")
Original = "1234"
originalEmail = "abc@abc.com"


if password == Original and email == originalEmail:
    print("Good Morning", originalEmail[0:3])
elif password != Original and email == originalEmail:
    print("Wrong password: ", originalEmail[0:3])
elif password == Original and email != originalEmail:
    print("Wrong email: ")
else:
    print("You are not registered!")
    # NEW 
    databse = []
while True:
    print(
        "1. Register\n"
        "2. Login\n"
        "3. Quit\n"
    )
    choice = input("Enter choice: ")
    # NEW
    while True:
        num1 = int(input("Enter number: "))
        opr = input("Enter Operator: ")
        num2 = int(input("Enter sec number: "))


        if opr == "+":
            print(num1 + num2)
        elif opr == "-":
            print(num1 - num2)
        elif opr =="*":
            print (num1 * num2)
        elif opr =="/":
            print(num1 / num2)
        continue
    # letter count

print("hey, enter as many as words below")

user = input("enter:_ ")

counter = 0
for x in user:
    if x == " ":
        counter += 1
    

print("Number of words: ",counter)

import random 
while True:
    print("star the game")
    number = random.randint(0, 100)
    conuter = 0
    while conuter < 5:
        guess = int(input ("Enter your guess:_"))
        if number == guess:
            print("your guess is correct")
            break

        elif number < guess :
            print("guess lower") 
            conuter += 1
            
        elif number > guess :
            print("guess higher")    
            conuter += 1

    print("Game over!!")
    
