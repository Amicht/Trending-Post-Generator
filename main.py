from selenium_helper import get_top_google_trends_today
from chat_gpt_helper import create_new_prompt, chat_with_gpt3

search_results = get_top_google_trends_today()

for trend in search_results:
    with open(f"./linkedin-posts/{trend['subject']}.txt", "w", encoding="utf-8") as file:
        prompt_content = create_new_prompt(trend["content"])
        linkedin_post = chat_with_gpt3(prompt_content)
        file.write(linkedin_post)

