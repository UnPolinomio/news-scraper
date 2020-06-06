from .news_list import get_links
from .news_detail import news_detail_by_link
from scraper.utils.output import save_to_file

def normal_pipeline():
    for news_link in get_links():
        news = news_detail_by_link(news_link)
        if news:
            save_to_file(news)