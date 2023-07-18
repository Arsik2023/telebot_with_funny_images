from requests import *
from pprint import pprint

class Random_cat_photo_text:
    def __init__(self, text):
        self.text = text
    def Random_cat_photo_text_url(self):
        url = 'https://cataas.com/cat/says/'+self.text+'?json=true'
        response = get(url).json()
        return 'https://cataas.com/'+response['url']
