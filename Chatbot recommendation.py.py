def chatbot_response(user_input):
    user_input = user_input.lower() #Convert input to lowercase for easier matching

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I help you?"
    elif "what is your name" in user_input:
        return "I am a simple rule-based chatbot created to assist you."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"
    
def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input or "exit" in user_input:
            break

if __name__ == "__main__":
    main()