from urllib.parse import urljoin

def urljoin_for_urls_list(site: str, urls: list):
    final_urls = map(lambda url: urljoin(site, url), urls)
    final_urls = list(final_urls)
    return final_urls