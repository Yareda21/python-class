database =[]
while True:
    name =input("name: -")
    age =int(input("age: -"))
    course =input("which course do you want to take: -")
    schedule =input("which days can you take the course: -")
    time =input("when can you take the course: -")
    payment =7500
    print("the total fee to take the course is 7500")
    student =[name, age, course, schedule, time, payment]
    ask =input("do you want to continue:y/n-")
    if "y":
        continue
    else:
        break
for data in database:
    print(data)
database.append(student)

