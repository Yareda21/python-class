# To-Do List in Python

# Initialize an empty list to store the tasks
tasks = []

def display_menu():
    """Print the main menu options"""
    print("Welcome to the To-Do List!")
    print("1. Add a new task")
    print("2. View the task list")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    """Prompt the user to enter a new task and add it to the list"""
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f"'{new_task}' has been added to the list.")

def view_tasks():
    """Display the current list of tasks"""
    if not tasks:
        print("The task list is empty.")
    else:
        print("Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_completed():
    """Prompt the user to select a task to mark as completed"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                print(f"'{completed_task}' has been marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def remove_task():
    """Prompt the user to select a task to remove from the list"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()