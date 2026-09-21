# ChatBuddy 🤖 — Rule-Based AI Chatbot

A simple command-line chatbot built in Python using rule-based (pattern matching) logic. ChatBuddy responds to greetings, basic questions, and common conversational inputs through predefined rules — no machine learning required.

## Features

- 💬 Simple, interactive command-line interface
- 🧠 Rule-based response matching for common queries (greetings, "how are you", "what is your name", etc.)
- ❓ Built-in `help` command to guide users
- 👋 Graceful exit with `bye`, `exit`, or `quit`
- 🪶 Lightweight — no external libraries or dependencies required

## Demo

```
=== Rule-Based AI Chatbot ===
Type 'bye', 'exit', or 'quit' to end the chat.

You: Hi
Bot: Hello! How can I help you today?
You: How are you?
Bot: I'm just a bot, but I'm doing great! How about you?
You: What is your name?
Bot: My name is ChatBuddy!
You: Exit
Bot: Goodbye! Have a great day.
```

## Requirements

- Python 3.x (no additional packages needed)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/chatbuddy.git
   cd chatbuddy
   ```
2. Run the chatbot:
   ```bash
   python chatbot2.py
   ```

## Usage

- Start the script and type your message at the `You:` prompt.
- Type `help` at any time to see what the bot can do.
- Type `bye`, `exit`, or `quit` to end the conversation.

## How It Works

ChatBuddy uses simple string/pattern matching to detect keywords in user input and returns a predefined response. If no matching rule is found, it responds with a fallback message asking the user to type `help`.

## Future Improvements

- [ ] Add more conversational patterns and responses
- [ ] Integrate NLP (e.g., NLTK or spaCy) for smarter intent recognition
- [ ] Add a GUI or web interface
- [ ] Store conversation history/logs

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Made with ❤️ for learning purposes.
