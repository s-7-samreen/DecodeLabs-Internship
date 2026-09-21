# ChatBuddy — Project Documentation

## 1. Introduction

ChatBuddy is a **rule-based AI chatbot** developed in Python. It simulates a basic conversational agent by matching user input against a set of predefined rules (keywords/patterns) and returning an appropriate response. Unlike machine learning–based chatbots, ChatBuddy does not learn from data — its "intelligence" comes entirely from hardcoded logic, making it a good introductory project for understanding the fundamentals of conversational AI and natural language pattern matching.

## 2. Objective

The objective of this project is to:
- Demonstrate the working of a simple rule-based chatbot system.
- Understand how user input can be parsed and matched to generate relevant responses.
- Build a foundation for more advanced chatbot systems (e.g., NLP-based or ML-based).

## 3. System Overview

| Attribute | Detail |
|---|---|
| Language | Python 3.x |
| Interface | Command-Line Interface (CLI) |
| Approach | Rule-based / pattern matching |
| Dependencies | None (uses Python standard library only) |
| Entry point | `chatbot2.py` |

## 4. System Architecture

The chatbot follows a simple **input → match → response** loop:

1. **Input Collection** — The program continuously prompts the user for text input via the console.
2. **Preprocessing** — The input is typically normalized (e.g., converted to lowercase, stripped of extra whitespace) to improve matching accuracy.
3. **Rule Matching** — The processed input is compared against a set of predefined keywords or patterns (e.g., "hi", "how are you", "your name").
4. **Response Generation** — If a match is found, the corresponding predefined response is returned. If no match is found, a fallback/default response is shown, prompting the user to type `help`.
5. **Exit Condition** — The loop terminates when the user types `bye`, `exit`, or `quit`.

```
 ┌─────────────┐
 │  User Input  │
 └──────┬──────┘
        ▼
 ┌─────────────────┐
 │  Preprocessing   │  (lowercase, trim, etc.)
 └──────┬──────────┘
        ▼
 ┌─────────────────┐
 │   Rule Matching   │  (keyword/pattern lookup)
 └──────┬──────────┘
        ▼
 ┌─────────────────┐         ┌───────────────────┐
 │  Match Found?    │── No ──▶  Fallback Response  │
 └──────┬──────────┘         └───────────────────┘
        │ Yes
        ▼
 ┌─────────────────┐
 │ Return Response  │
 └─────────────────┘
```

## 5. Features

- Greets the user and responds to common conversational phrases.
- Answers simple questions such as "How are you?" and "What is your name?"
- Provides a `help` command listing available interactions.
- Handles unrecognized input gracefully with a fallback message.
- Exits cleanly on `bye`, `exit`, or `quit`.

## 6. Sample Interaction

```
=== Rule-Based AI Chatbot ===
Type 'bye', 'exit', or 'quit' to end the chat.

You: Hi
Bot: Hello! How can I help you today?
You: How are you?
Bot: I'm just a bot, but I'm doing great! How about you?
You: Who are you?
Bot: Sorry, I didn't understand that. Type 'help' to see what I can do.
You: What is your name?
Bot: My name is ChatBuddy!
You: Exit
Bot: Goodbye! Have a great day.
```

## 7. Limitations

- The chatbot cannot understand context or maintain conversation history.
- Responses are limited to exact/keyword-based matches — rephrased or unlisted queries trigger the fallback response (as seen with "Who are you?" in the sample run above).
- No natural language understanding (NLU); it is purely pattern-based.
- Cannot handle spelling mistakes, synonyms, or complex sentence structures.

## 8. Future Enhancements

- Integrate NLP libraries (e.g., NLTK, spaCy) for intent recognition and synonym handling.
- Add context/memory so the bot can handle multi-turn conversations.
- Build a graphical or web-based interface instead of CLI.
- Expand the rule set or migrate to a machine learning–based model for broader understanding.
- Add logging to record and review past conversations.

## 9. Conclusion

ChatBuddy demonstrates the core principles behind rule-based conversational systems. While limited in scope, it serves as a practical starting point for understanding chatbot design before progressing to more sophisticated NLP or ML-driven approaches.
