from transformers import pipeline, Conversation

# For the conversation, we will be using Gemma-2B
chatbot = pipeline("conversational", model="google/gemma-2b-it")

# Initializing the conversation
initial_input = input("[USER] ")
conv_1 = Conversation(initial_input)

# Generating the output and printing it
overall_conversation = chatbot(conv_1)
print("[ASSISTANT] ", end="")
print(overall_conversation.messages[-1]["content"])

# Taking user input until the user says "quit"
while True:
    user_input = input("[USER] ")
    if user_input.lower() == "quit":
        break
        
    # Adding the new message to the conversation
    overall_conversation.add_message({"role": "user", "content": user_input})
    # Prompting the chatbot
    overall_conversation = chatbot(overall_conversation)
    # Printing the new output
    print("[ASSISTANT] ", end="")
    print(overall_conversation.messages[-1]["content"])
