class TrendItem:
    def __init__(self, subject: str, search_count: int, url: str, article_content):
        self.subject = subject
        self.search_count = search_count
        self.article_url = url
        self.article_content = article_content

