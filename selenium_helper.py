from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

GOOGLE_TRENDS_URL = "https://trends.google.co.il/trends/trendingsearches/daily?geo=IL&hl=iw"
MIN_SERACH_COUNT = 4000

def get_top_google_trends_today():
    trend_wrapper_class_name = "details-wrapper"

    with webdriver.Chrome() as driver:
        driver.get(GOOGLE_TRENDS_URL)
        feed_items = driver.find_elements(By.CLASS_NAME, trend_wrapper_class_name)
        if len(feed_items) == 0:
            return None
        top_searches = []
        for item in feed_items:
            trend_item = get_trend_details(item)
            if not trend_item:
                continue
            top_searches.append(trend_item)

        driver.close()
    return top_searches


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
    except:
        print("Failed to get item detalis")
        return None
    else:
        if search_count < MIN_SERACH_COUNT:
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
        except:
            print("Failed to get content")
            return None
        else:
            return article_content
