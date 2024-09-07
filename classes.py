from calculator import Calculator
from guess_game import GuessGame
from dice_rolling import DiceRoller

def run_calculator():
    calc = Calculator()
    print("Calculator Operations:")
    print(calc.add(5, 3))        # Output: 8
    print(calc.subtract(10, 4))  # Output: 6
    print(calc.multiply(3, 7))   # Output: 21
    print(calc.divide(10, 2))    # Output: 5.0
    print(calc.last_result)      # Output: 5.0

def run_guess_game():
    game = GuessGame()
    game.play()

def run_dice_roller():
    dice = DiceRoller()
    print(f"Rolling a {dice.sides}-sided dice: {dice.roll()}")

if __name__ == "__main__":
    print("Select a game or calculator:")
    print("1. Calculator")
    print("2. Guess Game")
    print("3. Dice Roller")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        run_calculator()
    elif choice == '2':
        run_guess_game()
    elif choice == '3':
        run_dice_roller()
    else:
        print("Invalid choice!")


from temp_converter import TemperatureConverter
from budget_tracker import BudgetTracker

def run_temperature_converter():
    temp_converter = TemperatureConverter(25)  # Initial temperature in Celsius
    print(f"Temperature in Fahrenheit: {temp_converter.fahrenheit}")  # Output: 77.0
    print(f"Temperature in Kelvin: {temp_converter.kelvin}")  # Output: 298.15

    temp_converter.fahrenheit = 32  # Set to freezing point in Fahrenheit
    print(f"Updated temperature in Celsius: {temp_converter.celsius}")  # Output: 0.0

def run_budget_tracker():
    budget = BudgetTracker()
    budget.add_income(5000)  # Add income
    budget.add_expense(1500)  # Add expense
    print(f"Current balance: ${budget.balance}")  # Output: 3500

if __name__ == "__main__":
    print("Select an option:")
    print("1. Temperature Converter")
    print("2. Budget Tracker")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        run_temperature_converter()
    elif choice == '2':
        run_budget_tracker()
    else:
        print("Invalid choice!")
