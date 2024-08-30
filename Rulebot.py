def chatbot_response(user_input):
    # Convert user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()

    # Define responses for specific queries
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I'm a chatbot created to help you. What can I do for you?"
    elif "how are you" in user_input:
        return "I'm just a program, so I don't have feelings, but I'm here to help you!"
    elif "help" in user_input:
        return "Sure, I can help you. What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you ask something else?"

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
