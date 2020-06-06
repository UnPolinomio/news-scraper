import requests
from lxml import html
from scraper.utils.config import get_config
import logging

logging.getLogger().setLevel(logging.INFO)

XPATH_EXPRESSIONS = get_config()['xpath_expressions']['news_detail']

def news_detail_by_link(link):
    try:
        # Config
        title_xpath = XPATH_EXPRESSIONS['title']
        summary_xpath = XPATH_EXPRESSIONS['summary']
        body_paragraphs_xpath = XPATH_EXPRESSIONS['body_paragraphs']

        logging.info(f'\t* Scraping {link}')

        # Get response
        response = requests.get(link)
        if not response.status_code == 200:
            raise Exception(f'\tError: {link} didn\'t returned 200 status code.')

        # Parse
        content = response.text
        parsed = html.fromstring(content)

        title = parsed.xpath(title_xpath)[0]
        title = title.replace('"', '')
        summary = parsed.xpath(summary_xpath)[0]
        body_paragraphs = parsed.xpath(body_paragraphs_xpath)

        logging.info(f'\tOk')

        return {
            'title': title,
            'summary': summary,
            'body': '\n'.join(body_paragraphs)
        }
    except Exception as error:
        logging.error(error)
        return None

