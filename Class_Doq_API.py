from requests import *
from pprint import pprint

class Random_dog_photo:
    def __init__(self):
        pass
    def Random_dog_url():
        url = 'https://dog.ceo/api/breeds/image/random'
        response = get(url).json()
        return response['message']