import random

def roll_dice():
    return random.randint(1, 6)

# Main program
if __name__ == "__main__":
    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}")
        
        # Ask the user if they want to roll again
        roll_again = input("Roll again? (y/n): ").lower()
        if roll_again != 'y':
            break
