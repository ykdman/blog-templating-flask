import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.url)
        self.all_posts = self.response.json()
        print(self.all_posts)
    

