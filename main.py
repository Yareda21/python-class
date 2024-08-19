# this is a module to write the function
def calculator():
    user_input = input("Enter a calculation (e.g. 2+2): ")
    num1, operator, num2 = user_input.split()
    num1, num2 = float(num1), float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Error: Invalid operator!")
        return

    print("Result:", result)




def todo_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome to the To-Do List App!")
        func(*args, **kwargs)
        print("Goodbye!")
    return wrapper

@todo_decorator
def todo_list_app():
    tasks = {}

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Remove task")
        print("4. View tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            tasks[task_name] = False
            print("Task added!")
        elif choice == "2":
            task_name = input("Enter task name: ")
            if task_name in tasks:
                tasks[task_name] = True
                print("Task marked as completed!")
            else:
                print("Task not found!")
        elif choice == "3":
            task_name = input("Enter task name: ")
            if task_name in tasks:
                del tasks[task_name]
                print("Task removed!")
            else:
                print("Task not found!")
        elif choice == "4":
            print("Tasks:")
            for task, completed in tasks.items():
                status = "Completed" if completed else "Not completed"
                print(f"{task}: {status}")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


def temperature_converter():
    while True:
        print("\nOptions:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def word_count_tool():
    with open("input.txt", "r") as file:
        text = file.read()

    words = text.split()
    word_counts = {}

    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print("Word counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    most_common_word = max(word_counts, key=word_counts.get)
    print(f"Most common word: {most_common_word}")


import random

def chatbot():
    responses = {
        "hello": ["Hi!", "Hello!", "Hey!"],
        "how are you": ["I'm good, thanks!", "I'm doing well!", "I'm great!"],
        "what is your name": ["I'm Chatty!", "My name is Chatty!", "I'm your friendly chatbot!"],
        "default": ["I didn't understand that.", "Can you please rephrase?", "Sorry, I'm not sure what you mean."]
    }

    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        user_input = user_input.lower()

        for key in responses.keys():
            if key in user_input:
                response = random.choice(responses[key])
                print("Chatty:", response)
                break
        else:
            response = random.choice(responses["default"])
            print("Chatty:", response)


import random

def dice_rolling_simulator():
    while True:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        results = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(results)

        print("Results:")
        for i, result in enumerate(results, start=1):
            print(f"Die {i}: {result}")
        print(f"Total: {total}")

        play_again = input("Do you want to roll again? (y/n): ")
        if play_again.lower() != "y":
            break



def budget_tracker():
    income = float(input("Enter your monthly income: "))
    expenses = {}

    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. View budget")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            expenses[category] = amount
            print("Expense added!")
        elif choice == "2":
            total_expenses = sum(expenses.values())
            balance = income - total_expenses
            print("Budget:")
            for category, amount in expenses.items():
                print(f"{category}: ${amount:.2f}")
            print(f"Total expenses: ${total_expenses:.2f}")
            print(f"Balance: ${balance:.2f}")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")





