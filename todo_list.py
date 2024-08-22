database=[]
def  addtask():
    while True :
        taskName = input("please give me your first task:-   ")
        taskTime = input("Enter date:-")
        taskDate = input("Enter task Duration:-")

        singleTask = {
            "Task Name" : taskName,
            "Task Time" : taskTime,
            "Task date" : taskDate,
            "Task Status" : "Uncompleted"
        }
        database.append(singleTask)

        ask = input("do you want to continue:- ")
        if ask == "no":
            print("Thank you for logging!!")
            break



def status_update():
    viewtask()
    while True:
        taskname = input("Enter task name to update: - ")
        # for task in database:
        #     if taskname == task["Task Name"]:
        #         print("found")
        data = [task for task in database if taskname == task["Task Name"]]
        
        if len(data) == 0:
            print("No task found: ", taskname)
        else:
            mytask = data[0]
            break


    print("Task Found:", taskname)
    print("1. Update status to completed", "2. Delete")
    ask = input("Enter choice (1 or 2): - ")
    if ask == "1":
        mytask["Task Status"] = "Completed"
        print(f"Task '{taskname}' has been marked as Completed.")
    elif ask == "2":
        database.remove(mytask)
        print(f"Task '{taskname}' has been deleted.")
    else:
        print("Invalid choice. Please try again.")

     
    
            


def viewtask():
    if len(database) == 0:
        print("No task is saved")
    for index in range(len(database)) :
        print(index+1, "= ", database[index]["Task Name"])

if "__main__" == __name__:

    print("\t\t Wellcome to my task app")
    while True:
        
        print(
            "\tPlease select:\n"
            "1. Add Task\n"
            "2. View Task\n"
            "3. Status update\n"
            "4. Quit"
            )
        try:
            choice = int(input("Enter choice: - "))
        except ValueError:
            print("Please enter number only!!")
            continue
        if choice == 1: 
            addtask()
            continue
        elif choice == 2:
            viewtask()
            continue
        elif choice == 3:
            status_update()
            continue
        elif choice == 4:
            print("Thank you - goodbye")
            break
        else:
            print("Invaild input")
            continue