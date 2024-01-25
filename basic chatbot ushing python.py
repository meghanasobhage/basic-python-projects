import random

def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm doing well, thank you.",
        "bye": "Goodbye! Have a great day.",
        "name": "I am a chatbot. You can call me ChatGPT.",
        "default": "I'm not sure how to respond to that. Can you ask me something else?"
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user's input matches any predefined responses
    return responses.get(user_input, responses["default"])

def main():
    print("Welcome to the Chatbot!")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
