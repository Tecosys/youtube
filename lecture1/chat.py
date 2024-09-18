from cerina import Completion

# Initialize the Completion model
completions = Completion()

# Function to generate assistant response based on user input and conversation history
def generate_response(history):
    # Build history string based on previous interactions
    history_prompt = " ".join([f'{item["role"]}: {item["content"]}' for item in history])

    # Extract the last user prompt
    last_user_prompt = history[-1]["content"] if history[-1]["role"] == "user" else ""

    # Create the full prompt for the assistant
    full_prompt = f"""
    You are a chat assistant.
    Previous conversation:
    {history_prompt}

    User's new input: {last_user_prompt}

    now as a chatbot read previous messages and then answer
    """

    # Get the assistant's response
    assistant_response = completions.create(full_prompt)
    
    # Return the response
    return assistant_response


# Function to run the chatbot in the terminal
def chatbot():

    # Initialize conversation history
    history = []
    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Add user input to history
        history.append({"role": "user", "content": user_input})

        # Generate assistant response
        assistant_response = generate_response(history)

        # Add assistant response to history
        history.append({"role": "assistant", "content": assistant_response})

        # Print assistant response
        print(f"Assistant: {assistant_response}\n")

        # Check if user wants to exit the chat
        if user_input.lower() in ["exit", "quit"]:
            break


# Run the chatbot
if __name__ == "__main__":
    chatbot()
