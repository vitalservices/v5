```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.settings import Settings

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(Settings)

    def run_spider(self, spider):
        self.process.crawl(spider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider(RedditSpider)
```