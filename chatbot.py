from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="")

def chatbot():
    conversation = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."}
    ]

    while True:
        user_input = input("You: ")
        
        conversation.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        message = response['choices'][0]['message']['content']
        print("Chatbot: " + message)

        conversation.append({"role": "assistant", "content": message})
    print(messages)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
 