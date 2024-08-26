while True:
    num=6
    guess =input("guess a num 1-10: -")
    if guess <num:
        print("guess higher")
    elif guess>num:
        print("guess lower")
    else guess==num:
        print("correct")