import os

import openai

openai.api_key = os.environ.get("OPEN_API_KEY")


def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["."],
        )
        message = response.choices[0].text.strip()
    except Exception as e:
        message = f"Error: {str(e)}"

    return message


print("Hi, I'm a chatbot. How can I help you today?")
conversation_end = False
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI: "

while not conversation_end:
    user_input = input("> ")
    prompt += f"Human: {user_input}\nAI: "
    message = generate_response(prompt)
    prompt += message + "\n"
    print("Bot:", message)

    if "goodbye" in user_input.lower():
        conversation_end = True
