from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from dotenv import load_dotenv
import os
load_dotenv()


GOOGLE_TRENDS_URL = "https://trends.google.com/trends/trendingsearches/daily?geo=US&hl=iw"
MIN_SEARCH_COUNT = 100000


def get_top_google_trend_today():
    trend_wrapper_class_name = "details-wrapper"
    top_trend = None

    with webdriver.Chrome() as driver:
        driver.get(GOOGLE_TRENDS_URL)
        feed_items = driver.find_elements(By.CLASS_NAME, trend_wrapper_class_name)
        if len(feed_items) == 0:
            return None
        for item in feed_items:
            trend_item = get_trend_details(item)
            if trend_item:
                top_trend = trend_item
                break

        driver.close()
    return top_trend


def get_trend_details(trend_element: WebElement) -> dict[str, int | str | None] | None:
    subject_class_name = "details-top"
    search_count_class_name = "search-count-title"
    article_url_class_name = "summary-text"

    try:
        subject = trend_element.find_element(By.CLASS_NAME, subject_class_name).text.strip()
        search_count = int(trend_element.find_element(By.CLASS_NAME, search_count_class_name)
                           .text.strip()
                           .replace("+", "")
                           .replace("K", "000"))
        article_url = trend_element.find_element(By.CSS_SELECTOR, f".{article_url_class_name} a").get_attribute("href")
    except Exception as e:
        print("Failed to get item detalis")
        return None
    else:
        if search_count < MIN_SEARCH_COUNT:
            return None
        content = get_article_content(article_url)
        if not content:
            return None
        trend_item = {
            "subject": subject,
            "url": article_url,
            "content": content,
            "search_count": search_count
        }
        return trend_item


def get_article_content(article_url: str):
    with webdriver.Chrome() as driver:
        try:
            driver.get(article_url)
            article_content = driver.find_element(By.TAG_NAME, "article").text.strip()
        except Exception as e:
            print("Failed to get article content:")
            print(e)
            return None
        else:
            return article_content


def write_post_to_linkedin(post: str):

    linkedin_url = "https://www.linkedin.com/"
    email = os.environ.get("LINKEDIN_EMAIL")
    password = os.environ.get("LINKEDIN_PASSWORD")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    with webdriver.Chrome() as driver:
        driver.get(linkedin_url)
        try:
            # sign-in page
            driver.find_element(By.ID, "session_key").send_keys(email)
            driver.find_element(By.ID, "session_password").send_keys(password)
            signin_btn = driver.find_element(By.CSS_SELECTOR, '.sign-in-form__submit-btn--full-width')
            signin_btn.click()

            # feed page
            start_post_btn = driver.find_element(By.CLASS_NAME, 'share-box-feed-entry__trigger')
            start_post_btn.click()

            # editor_div = driver.find_element(By.CLASS_NAME, "ql-editor ql-blank")
            # editor_div.click()
            # editor_div.send_keys("First Automated Post!")

        except Exception as error:
            print(error)
            print("Error: Scrapper was blocked by Linkedin")
