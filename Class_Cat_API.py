from requests import *
from pprint import pprint

class Random_cat_photo:
    def __init__(self):
        pass
    def Random_cat_url():
        url = 'https://cataas.com/cat?json=true'
        response = get(url).json()
        return 'https://cataas.com'+response['url']