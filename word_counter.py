def count_words(text):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): The input text to be analyzed.
        
    Returns:
        int: The number of words in the input text.
    """
    # Split the text into a list of words
    words = text.split()
    
    # Return the length of the words list
    return len(words)

def main():
    """
    The main function prompts the user to enter some text,
    calls the count_words function to count the number of words,
    and prints the result.
    """
    text = input("Enter some text: ")
    word_count = count_words(text)
    print(f"The text contains {word_count} words.")

if __name__ == "__main__":
    main()