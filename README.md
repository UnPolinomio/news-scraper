# News Web scraper
This is a news site python-based web scraper.

## Use
1. Clone this repo and move to repo folder.
2. `python -m venv .env`
3. `source .env/bin/activate`
4. `pip install -r requirements.txt`
5. `python main.py` and wait some minutes.

## Settings file
Settings file is scraper_config.yaml.

There is a news-sites list. Follow the current file structure.

For every site, config is:
### General
- sitename: Folder name where scraped news will be saved.

### news_list
- site: Url where news-site lists its news.
- links: Xpath for news articles urls.

### news_detail
- title: Xpath for news article title text.
- summary: Xpath for news article summary text.
- body_paragraphs: Xpath for body paragraphs text
