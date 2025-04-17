import requests


def test_request_by_id():
   url = 'https://api.kinopoisk.dev/v1.4/movie/1000'
   params = {"id":"1000"
   }
   response = requests.get( url, headers= headers , params= params)
   assert response.status_code == 200

def test_films_random():
   url = 'https://api.kinopoisk.dev/v1.4/movie/random'
   params = {
   "year":"2021",
   "month":"january",
   "id":"666"
   }
   response = requests.get( url, headers=headers , params= params)
   assert response.status_code == 200



def test_search():
   url = 'https://api.kinopoisk.dev/v1.4/movie/search'
   params = {
      "query":"Шрек",
      "limit":"5",
      "page":"1"
   }
   response = requests.get( url, headers=headers, params=params)
   assert response.status_code == 200
   assert "Шрек" in response.tex
