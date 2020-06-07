import re
from pathlib import Path
from urllib.parse import urlparse, urlunparse
from urllib.request import urlretrieve

def cached_file(*,url):
    cache_path = url_to_path(url)
    if not cache_path.is_file():
        cache_path.parents[0].mkdir(parents=True, exist_ok=True)
        print(f"fetching {url}")
        urlretrieve(url, cache_path)
    return cache_path

def url_to_path(url):
    cleaned_url = re.sub('^http(s)?://', '', url)
    return Path('./data') / Path(cleaned_url)