while True:
    num=5
    guess =input("guess a num1-10: - ")
    if guess<num:
        print("guess higher") 
    elif guess>num:
        print("guess lower")
        