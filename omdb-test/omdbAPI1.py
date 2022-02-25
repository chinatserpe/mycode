#!/usr/bin/env python3
import requests

api_key = 53718335
search_title = "Titanic"
api = f"http://www.omdbapi.com/?apikey={api_key}&s={search_title}"

omdb_resp = requests.get(api)

movie_json = omdb_resp.json()

print(movie_json)
print(movie_json.get('totalresults', 'Sorry, can\'t find that key!'))
print(movie_json['totalResults'])




