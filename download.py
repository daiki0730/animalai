from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報
key = "13d0b558fde46ff8ba0424f33e823dcd"
secret = "2a291ba9306c54cb"
wait = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

photos = result['photos']
pprint(photos)
