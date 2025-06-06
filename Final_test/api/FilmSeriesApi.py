import requests
from typing import List, Dict, Any, Tuple
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_api = config.get("base_url_api")
token_info = config.get("token_info")


class FilmSeriesApi:

    def __init__(self, url):
        self.url = url

    def search_film_tv_series_by_name(
            self, name_to_search: str
    ) -> Tuple[Dict[str, Any], int]:
        """Метод для поиска фильма/сериала по названию
        Args:
            name_to_search (str): название фильма/сериала
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией\
                  о фильме/сериале, статус коде
        """
        result_search_by_name = requests.get(
            base_url_api + "movie/search"
                           "?query=" + name_to_search, headers=token_info
        )
        return result_search_by_name.json(), result_search_by_name.status_code

    def search_film_tv_series_by_id(
            self, id: int) -> Tuple[Dict[str, Any], int]:
        """Метод для поиска фильма/сериала по id
        Args:
            id (int): id фильма/сериала
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией\
                  о фильме/сериале, статус коде
        """
        result_search_by_id = requests.get(
            base_url_api + "movie/" + str(id), headers=token_info
        )
        return result_search_by_id.json(), result_search_by_id.status_code

    def search_by_fields(self, field: str) -> Tuple[List[Dict[str, str]], int]:
        """Метод для поиска по полям
        Args:
            field (str): genres.name, countries.name, type, typeNumber, status
        Returns:
            Tuple[List[Dict[str, str]], int]: json ответ с информацией\
                  по искомым данным, статус коде
        """
        result_search_fields = requests.get(
            "https://api.kinopoisk.dev"
            "/v1.4/movie/possible-values-"
            "by-field?field="
            + field,
            headers=token_info,
        )
        return result_search_fields.json(), result_search_fields.status_code