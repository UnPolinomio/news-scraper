import requests
from lxml import html
from scraper.utils.config import get_config
import logging

logging.getLogger().setLevel(logging.INFO)

XPATH_EXPRESSIONS = get_config()['xpath_expressions']['news_list']

def get_links():
    try:
        # Config
        site = XPATH_EXPRESSIONS['site']
        links_xpath = XPATH_EXPRESSIONS['links']

        logging.info(f'- Scraping {site}')

        # Get response
        response = requests.get(site)
        if not response.status_code == 200:
            raise Exception(f'Error: {site} didn\'t returned 200 status code.')

        # Parse content
        content = response.text
        parsed = html.fromstring(content)
        links = parsed.xpath(links_xpath)

        logging.info(f'\tOk')

        return links
    except Exception as error:
        logging.error(error)
        return []