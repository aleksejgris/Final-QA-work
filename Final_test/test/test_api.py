import requests


def test_request_by_name():
   url ='https://www.kinopoisk.ru /api/v2.2/films/{id}'
   headers = {
                "Content-Type": "application/json",
                "id": "6"
   }
   response = requests.request("GET", url, headers=headers)
   assert (response.text)

def test_films_premieres():
   url = 'https://www.kinopoisk.ru /api/v2.2/films/premieres'
   headers = {
   "Content-Type": "application/json",
   "year":"2021",
   "month":"january"
   }
   response = requests.request("GET", url, headers=headers)
   assert (response.text)



def test_search_by_keyword():
   url = 'https://www.kinopoisk.ru /api/v2.2/films/search-by-keyword'
   headers = {
      "Content-Type": "application/json",
      "keyword":"Шрек"
   }
   response = requests.request("GET", url, headers=headers)
   assert (response.text)
