import os
import datetime
from slugify import slugify
from scraper.utils.config import get_config

def save_to_file(scraped_article, config):
    today = get_config()['today']
    if not os.path.isdir('output'):
        os.mkdir('output')
    if not os.path.exists(f'output/{config["sitename"]}'):
        os.mkdir(f'output/{config["sitename"]}')
    if not os.path.exists(f'output/{config["sitename"]}/{today}'):
        os.mkdir(f'output/{config["sitename"]}/{today}')

    filename = f'output/{config["sitename"]}/{today}/{slugify(scraped_article["title"])}'
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(scraped_article['title'])
        f.write('\n\n')
        f.write(scraped_article['summary'])
        f.write('\n\n')
        f.write(scraped_article['body'])