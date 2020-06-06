from .news_list import get_links
from .news_detail import news_detail_by_link
from scraper.utils.output import save_to_file
from scraper.utils.config import get_config

def normal_pipeline():
    for config in get_config()['xpath_expressions']:
        for news_link in get_links(config=config):
            news = news_detail_by_link(news_link, config=config)
            if news:
                save_to_file(news, config=config)