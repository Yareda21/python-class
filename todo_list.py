database =[]
while True:
    name =input("name: - ")
    age =int(input("age: - "))
    course =input("course: - ")
    time =input("time: - ")
    schedule =input("schrdule: - ")
    payment =8,000
    student =[name,age,course,time,schedule,payment]
    ask =input("do you want to continue:y/n - ")
    if"y":
        continue
    else:
        break
for data in database:
    print(data)
    database.append(student)