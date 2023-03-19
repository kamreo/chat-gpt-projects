import openai

openai.api_key = "<YOUR_API_KEY>"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def chat():
    while True:
        user_input = input("You: ")
        if user_input.strip() == "":
            print("Please enter a valid input")
            continue
        
        prompt = f"User: {user_input}\nChatGPT:"
        response = generate_response(prompt)
        response += "\n"
        
        while True:
            if response.endswith("...\n"):
                print(f"ChatGPT: {response[:-1]}")
                user_prompt = input("Please continue: ")
                prompt += user_prompt + "\n"
                response = generate_response(prompt)
                response += "\n"
            else:
                print(f"ChatGPT: {response[:-1]}")
                break
        

chat()