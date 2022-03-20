
import requests
from imdb import IMDb
from urllib.parse import *
import os
from dotenv import load_dotenv

load_dotenv()

class MvFm():
    iw = IMDb()
    api_key = os.getenv("TMDBAPIKEY")

    def get_top_rated(self):
        res = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={self.api_key}")
        return res.json()["results"]

    def get_latest(self):
        res = requests.get(f"https://api.themoviedb.org/3/movie/latest?api_key={self.api_key}")
        return res.json()

    def get_popular(self):
        res = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={self.api_key}")
        return res.json()["results"]

    def get_by_keyword(self, keyword):
        iw = IMDb()
        movies = iw.get_keyword(keyword)
        return movies

    def get_trending(self):
        res = requests.get(f'https://api.themoviedb.org/3/trending/movie/day?api_key={self.api_key}')
        return res.json()["results"]
    

    def get_trending_tv(self):
        res = requests.get(f'https://api.themoviedb.org/3/trending/tv/day?api_key={self.api_key}')
        return res.json()["results"]
    
    def get_trending_week(self):
        res = requests.get(f'https://api.themoviedb.org/3/trending/movie/week?api_key={self.api_key}')
        return res.json()["results"]

    def get_trailer(title):
        import urllib.request
        import re

        html = urllib.request.url1open("https://www.youtube.com/results?search_query=" + title)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print("https://www.youtube.com/watch?v=" + video_ids[0])
    
    def get_details(self, title):
        title = str(title)
        if "(" in title:
            title = title[:title.index("(")]
        t = quote_plus(title)
        res = requests.get(f"https://api.themoviedb.org/3/search/movie/?api_key={self.api_key}&query={t}")
        return res.json()["results"][0]