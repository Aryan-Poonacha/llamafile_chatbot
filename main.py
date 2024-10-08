#!/usr/bin/env python3
from openai import OpenAI

def run_chatbot(user_input, port=8080, instructions="You are a helpful AI assistant."):
    """
    Runs the chatbot. This function is NOT directly tested in unit tests 
    as it requires a live server. 
    """
    try:
        client = OpenAI(
            base_url=f"http://localhost:{port}/v1",  
            api_key="sk-no-key-required" 
        )

        completion = client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": user_input} 
            ]
        )
        return completion.choices[0].message.content 

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred."

def process_user_input(user_input):
    """
    Processes user input, handling 'exit' and returning a response.
    This function can be unit tested as it doesn't directly call 
    the external API.
    """
    if user_input.lower() == "exit":
        return "Exiting..."
    else:
        return user_input

def process_user_input_test(user_input):
    """
    Processes user input, handling 'exit' and returning a response.
    This function can be unit tested as it doesn't directly call 
    the external API.
    """
    if user_input.lower() == "exit":
        return "Exiting..."
    else:
        # In a real application, you would call run_chatbot here, 
        # but we'll return a placeholder for testing.
        return "Chatbot response (mocked)" 

if __name__ == "__main__":
    instructions = input("Enter custom system instructions(blank for default):")
    if not instructions:
        instructions = "You are a helpful AI assistant."

    while True:
        port = input("Enter port no of local server to use (default is 8080):")
        if not port:
            port = 8080
        else:
            try:
                port = int(port)
            except ValueError:
                print("Invalid port number. Please enter a valid integer.")
                continue

        user_input = input("You: ")
        processed_user_input = process_user_input(user_input)
        response = run_chatbot(processed_user_input, port, instructions)
        print(f"Chatbot: {response}")
        if response == "Exiting...":
            break
