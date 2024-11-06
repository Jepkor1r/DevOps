#!/bin/bash

echo "Hello! I am your chatbot. Type 'exit' to end the conversation."

while true; do
    # Read user input
    read -p "You: " user_input

    # Convert input to lowercase for easier matching
    user_input=$(echo "$user_input" | tr '[:upper:]' '[:lower:]')

    # Respond based on user input
    case "$user_input" in
        "hello"|"hi")
            echo "Bot: Hello! How can I help you today?"
            ;;
        "how are you?"|"how's it going?")
            echo "Bot: I'm doing great, thank you!"
            ;;
        "what's your name?"|"who are you?")
            echo "Bot: I am a Bash chatbot."
            ;;
        "bye"|"exit")
            echo "Bot: Goodbye! Have a great day!"
            break
            ;;
        *)
            echo "Bot: Sorry, I didn't understand that."
            ;;
    esac
done