import requests


bacon_ipsum_url = "https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text"
quotable_url = "https://quotable.io"
metaphorpsum_url = "http://metaphorpsum.com"


class ApiClient:

    def __init__(self):

        url = bacon_ipsum_url
        response = requests.get(url=bacon_ipsum_url)


        self.easy_text = response.text