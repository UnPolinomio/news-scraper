import yaml

_config = None

def get_config():
    global _config
    if not _config:
        with open('./scraper_config.yaml') as f:
            _config = yaml.safe_load(f)
    return _config