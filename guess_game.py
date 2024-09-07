import random

class GuessGame:
    def __init__(self):
        self._number_to_guess = random.randint(1, 100)
        self._attempts = 10

    @property
    def number_to_guess(self):
        return self._number_to_guess

    @number_to_guess.setter
    def number_to_guess(self, value):
        self._number_to_guess = value

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, value):
        if value > 0:
            self._attempts = value

    def make_guess(self, guess):
        if guess == self._number_to_guess:
            return "Congratulations! You guessed the number correctly!"
        elif guess < self._number_to_guess:
            return "Too low! Try again."
        else:
            return "Too high! Try again."

    def play(self):
        while self._attempts > 0:
            try:
                guess = int(input(f"You have {self._attempts} attempts left. Make a guess: "))
                result = self.make_guess(guess)
                print(result)
                if "Congratulations" in result:
                    break
                self._attempts -= 1
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if self._attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {self._number_to_guess}.")