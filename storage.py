import openai
import os

class PromptBuffer:
    buffer = []
    size = 10
        

    def add_prompt(self, prompt):
        if len(self.buffer) >= self.size:
            self.buffer.pop(0)
        self.buffer.append(prompt)

    def get_prompts(self):
        return self.buffer

    def clear_buffer(self):
        self.buffer = []

openai.api_key = ""

def chat_with_openai(user_input, prompt_buffer):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for prompt in prompt_buffer.get_prompts():
        messages.append({"role": "user", "content": prompt})
    messages.append({"role": "user", "content": user_input})
    
    print(messages)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0
    )
    return response.choices[0].message["content"]

def main():
    prompt_buffer = PromptBuffer()  # Create a buffer with a size of 10
    print("Chatbot is running. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        prompt_buffer.add_prompt(user_input)
        response = chat_with_openai(user_input, prompt_buffer)
        print(f"Assistant: {response}")
        
        
if __name__ == "__main__":
    main()