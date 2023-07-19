import openai
from dotenv import load_dotenv
import os
load_dotenv()


def chat_with_gpt3(prompt):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Junior Dev Job Hunt"},
            {"role": "user", "content": prompt}
        ]
    )

    return gpt_response['choices'][0]['message']['content']


def create_new_prompt(additional_content: str):
    with open("base_linkedin_post_prompt.txt") as file:
        base_prompt_text = file.read()
        prompt = f"{base_prompt_text}\n\n{additional_content}"
    return prompt
