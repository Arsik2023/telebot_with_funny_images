from requests import *
from pprint import pprint

class Random_cat_animation:
    def __init__(self):
        pass
    def Random_cat_animation_url():
        url ='https://cataas.com/cat/gif?json=true'
        response = get(url).json()
        return 'https://cataas.com/'+response['url']
""" a = Random_cat_animation
print(a.Random_cat_animation_url()) """