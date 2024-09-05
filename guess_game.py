while True:
    num=5
    guess =input("guess a num1-10: - ")
    if guess<num:
        print("guess higher") 
    elif guess>num:
        print("guess lower")
        print("*try again*")
        counter= counter+1
    elif guess<num:
        print("guess higher")
        print("*try again*")
    ask =input("do youwant to continue:y/n - ")
    if ask == "y":
        continue
    else:
        break
        