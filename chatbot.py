"""
Project 1: Rule-Based AI Chatbot
Goal: A simple rule-based chatbot that responds to predefined user inputs
using if-else logic and runs in a continuous loop.
"""

def get_response(user_input):
    text = user_input.lower().strip()
    if text in ["hi", "hello", "hey", "salam", "assalam o alaikum"]:
        return "Hello! How can I help you today?"

    elif text in ["how are you", "how are you?"]:
        return "I'm just a bot, but I'm doing great! How about you?"

    elif text in ["what is your name", "what's your name", "who are you"]:
        return "I am a simple rule-based chatbot created for Project 1."

    elif "name" in text and "your" in text:
        return "My name is ChatBuddy!"

    elif text in ["help", "what can you do"]:
        return "I can greet you, chat a little, and say goodbye when you're done. Try saying 'hi' or 'bye'!"

    elif text in ["thank you", "thanks", "shukriya"]:
        return "You're welcome!"

    # Exit commands
    elif text in ["bye", "exit", "quit", "goodbye", "khuda hafiz"]:
        return "EXIT"

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    print("=== Rule-Based AI Chatbot ===")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:  # Continuous loop
        user_input = input("You: ")

        if user_input.strip() == "":
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day. 👋")
            break  # exits the continuous loop
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()
