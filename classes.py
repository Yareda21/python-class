# this is where you declare all the class

from temperature import TemperatureConverter

def main():
    temp_converter = TemperatureConverter(celsius=25.0)

    print(f"Celsius: {temp_converter.celsius}")
    print(f"Fahrenheit: {temp_converter.to_fahrenheit()}")
    print(f"Kelvin: {temp_converter.to_kelvin()}")

    # Update Celsius value
    temp_converter.celsius = 30.0
    print(f"Updated Celsius: {temp_converter.celsius}")
    print(f"Updated Fahrenheit: {temp_converter.to_fahrenheit()}")
    print(f"Updated Kelvin: {temp_converter.to_kelvin()}")

if __name__ == "__main__":
    main()



from todo_list import ToDoList

def main():
    todo_list = ToDoList()

    # Add tasks
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Write code")

    print("To-Do List:")
    for i, task in enumerate(todo_list.tasks):
        print(f"{i}. {task}")

    # Remove a task
    todo_list.remove_task(1)
    print("\nUpdated To-Do List:")
    for i, task in enumerate(todo_list.tasks):
        print(f"{i}. {task}")

if __name__ == "__main__":
    main()


from word_counter import WordCounter

def main():
    wc = WordCounter(text="Hello world! This is a test.")

    print(f"Text: {wc.text}")
    print(f"Word count: {wc.count_words()}")

    # Update text and recount words
    wc.text = "New text with more words."
    print(f"\nUpdated Text: {wc.text}")
    print(f"Updated Word Count: {wc.count_words()}")

if __name__ == "__main__":
    main()