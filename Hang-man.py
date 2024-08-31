import random

def choose_word():
    words = ["python", "programming", "computer", "science", "algorithm", "database","hailu","apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "ugli",
    "vanilla",
    "watermelon",
    "zucchini",
    "avocado",
    "blackberry",
    "cantaloupe",
    "dragonfruit",
    "eggplant",
    "fennel",
    "grapefruit",
    "jalapeno",
    "kale",
    "lime",
    "mushroom",
    "nutmeg",
    "onion",
    "pepper",
    "pumpkin",
    "spinach",
    "tomato",
    "asparagus",
    "broccoli",
    "carrot",
    "cucumber",
    "radish",
    "sweetpotato",
    "turnip",
    "artichoke",
    "beet",
    "cauliflower",
    "dill",
    "endive",
    "garlic",
    "horseradish",
    "leek",
    "parsnip",
    "quinoa",
    "sorrel",
    "tarragon",
    "zucchini",
    "basil",
    "cilantro",
    "chives",
    "oregano",
    "rosemary",
    "thyme",
    "sage",
    "peppermint",
    "parsley",
    "curry",
    "cinnamon",
    "clove",
    "cumin",
    "nutmeg",
    "paprika",
    "vanilla",
    "wasabi",
    "chili",
    "saffron",
    "sesame",
    "walnut",
    "almond",
    "cashew",
    "pecan",
    "hazelnut",
    "pistachio",
    "macadamia",
    "peanut",
    "pumpkinseed",
    "sunflower",
    "chia",
    "flaxseed",
    "coconut",
    "cacao",
    "chocolate",
    "caramel",
    "marshmallow",
    "toffee",
    "jelly",
    "gelatin",
    "syrup",
    "sauce",
    "ketchup",
    "mustard",
    "mayonnaise",
    "vinaigrette",
    "salsa",
    "hummus",
    "guacamole",
    "dip",
    "spread",
    "sourdough",
    "baguette",
    "ciabatta",
    "focaccia",
    "pita",
    "tortilla",
    "croissant",
    "biscuit",
    "cookie",
    "brownie",
    "cake",
    "pie",
    "pudding",
    "tart",
    "muffin",
    "scone",
    "donut",
    "pancake",
    "waffle",
    "crepe",
    "fritter",
    "cobbler",
    "strudel",
    "cheesecake",
    "flan",
    "tiramisu",
    "gelato",
    "sorbet",
    "icecream",
    "sundae",
    "smoothie",
    "shake",
    "milkshake",
    "cocktail",
    "mocktail",
    "punch",
    "juice",
    "lemonade",
    "tea",
    "coffee",
    "espresso",
    "latte",
    "cappuccino",
    "hotchocolate",
    "chai",
    "matcha",
    "herbaltea",
    "icedtea",
    "icedcoffee",
    "sparklingwater",
    "mineralwater",
    "soda",
    "energydrink",
    "smoothiedrink",
    "sportsdrink"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

hangman()