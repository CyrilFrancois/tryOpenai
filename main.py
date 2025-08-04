from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI() #No need for OpenAI(api_key=os.getenv("OPENAI_API_KEY")) because already loaded with dotenv

prompt = "How to throw a unicorn into a crowed market? Write a really short medfan story."


def generate_chatgpt_response(prompt):
    response = client.chat.completions.create(
    model=os.getenv("SUMMARY_MODEL"),
    temperature=1, #0 to 1 ; A temperature of 0 means the responses will be very straightforward and predictable ; A temperature closer to 1 means the responses can vary wildly.
    messages=[
        {"role": "system", "content": "You are a fun storyteller assistant."},
        {"role": "user", "content": prompt}
    ],
    )
    return response.choices[0].message.content

# Usage example
if __name__ == "__main__":
    chatgpt_response = generate_chatgpt_response(prompt)
    print(f"ChatGPT says: {chatgpt_response}")
