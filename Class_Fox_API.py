from requests import *
from pprint import pprint

class Random_fox_photo:
    def __init__(self):
        pass
    def Random_fox_url():
        return get('https://randomfox.ca/floof/').json()['image']