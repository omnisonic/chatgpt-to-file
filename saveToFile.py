import json
import os

import openai
import requests

# Replace 'your_api_key' with your actual API key
openai.api_key = os.environ.get("OPEN_API_KEY")

prompt = input("What is the prompt? >")
print(prompt)


def call_openai_api(prompt, model="gpt-3.5-turbo", max_tokens=100):
    response = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]


def save_response_to_text_file(response):
    file_name = "".join(c for c in response[:20] if c.isalnum())
    with open(file_name, "w") as text_file:
        # Strip non-alphanumeric characters from the output
        text_file.write(response)


if __name__ == "__main__":
    response = call_openai_api(prompt)
    print("reply: ", response)
    # Replace 'output.txt' with your desired file name
    save_response_to_text_file(response)
