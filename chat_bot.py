import random

responses = [
    {
        1: "hello",
        2: "hi",
        3: "how are you"
    },
    {
        1: "I am fine, thank you, and you?",
        2: "I am fine, bro.",
        3: "Fine, fine."
    },
    {
        1:"Thats good",
        2:"I am glad to hear that",
    }
]

def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return responses[0][random.randint(1, 3)]
    elif "how are you" in user_input or "how r u" in user_input:
        return responses[1][random.randint(1, 3)]
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you!" in user_input:
        return "You're welcome!"
    elif "Fine" in user_input or "i am good " in user_input:
        return responses[2][random.randint(1,2)]
    else:
        return "I'm sorry, I don't understand that."

def chat():
    print("Chatbot: Hi! I'm here to help. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        bot_response = get_response(user_input)
        print("Chatbot:", bot_response)

if __name__ == "__main__":
    chat()