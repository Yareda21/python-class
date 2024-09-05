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