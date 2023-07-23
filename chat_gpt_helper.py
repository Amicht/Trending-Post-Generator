import openai
from dotenv import load_dotenv
import os
load_dotenv()


def chat_with_gpt3(prompt):
    print("Connecting to GPT...")
    try:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Junior Dev Job Hunt"},
                {"role": "user", "content": prompt}
            ]
        )
    except Exception as e:
        print("Failed to interact with chat-gpt")
        return None
    else:
        return gpt_response['choices'][0]['message']['content']


def create_new_prompt(article_content: str):
    print("creating prompt...")
    with open("./base_linkedin_post_prompt.txt", "r") as file:
        base_prompt_text = file.read()
        prompt = base_prompt_text.replace("[scraped-article]", article_content)
    return prompt
