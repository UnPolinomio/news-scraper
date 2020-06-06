import os
import datetime
from slugify import slugify
from scraper.utils.config import get_config

def save_to_file(scraped_article):
    today = get_config()['today']
    if not os.path.isdir('output'):
        os.mkdir('output')
    if not os.path.exists(f'output/{today}'):
        os.mkdir(f'output/{today}')

    filename = f'output/{today}/{slugify(scraped_article["title"])}'
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(scraped_article['title'])
        f.write('\n\n')
        f.write(scraped_article['summary'])
        f.write('\n\n')
        f.write(scraped_article['body'])