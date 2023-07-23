from selenium_helper import get_top_google_trend_today
from chat_gpt_helper import create_new_prompt, chat_with_gpt3
from datetime import datetime


def generate_daily_post():
    try:
        top_trend = get_top_google_trend_today()
        if not top_trend:
            return print("Error: No matching trend found")

        date = datetime.now().date()
        prompt_content = create_new_prompt(top_trend["content"])
        with open(
                f"./linkedin-posts/{top_trend['subject'].replace(' ', '_')}_{date}.txt",
                "w",
                encoding="utf-8"
        ) as file:
            linkedin_post = chat_with_gpt3(prompt_content)
            if (type(linkedin_post) == str) and linkedin_post:
                file.write(linkedin_post)
                print("Post send Successfully")
    except:
        print("Error: Process incomplete")


generate_daily_post()
