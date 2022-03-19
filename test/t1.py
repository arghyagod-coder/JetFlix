import requests
akey = "7c59bd6bae71788bd0e1eee97b93cf58"

from urllib.parse import *

movie = "The Godfather"
data = {'query': 'The Godfather'}
# res = requests.get(f"https://api.themoviedb.org/3/search/movie/?api_key={akey}&query=The+Godfather")
res = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={akey}")
print(res.json()["results"][0:10])