# Simple chatbot using a dictionary

def chatbot_response(user_input):
    # Dictionary of responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just a program, but thanks for asking!",
        "what is your name": "I am a simple chatbot created in Python.",
        "bye": "Goodbye! Have a great day!",
        "how old are u":"sry i'm programming language i do not have age",
      
    }

    # Normalize user input to lower case
    user_input = user_input.lower()

    # Check for a response
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()