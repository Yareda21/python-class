symbols = ["\"", ",","!", " "]
def count_words(text):
    
    count=1
    # Split the text into words and filter out empty strings
    for letter in text:
        if letter in symbols:
            count = count + 1

    return count

def main():
    # Get user input
    text = input("Enter your text: ")
    
    # Count words
    word_count = count_words(text)
    
    # Print the result
    print(f"Word Count: {word_count}")


if __name__ == "__main__":
    main()