import requests
from typing import Dict, Any, Tuple
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_api = config.get("base_url_api")
token_info = config.get("token_info")


class PersonApi:

    def __init__(self, url):
        self.url = url

    def search_person_by_name(
            self, name_to_search: str) -> Tuple[Dict[str, Any], int]:
        """Метод для поиска персоны по имени и фамилии
        Args:
            name_to_search (str): имя и фамилия персоны
        Returns:
            Tuple[Dict[str, Any], int]: json ответ\
                  с информацией о персоне, статус коде
        """
        result_search_by_name = requests.get(
            base_url_api + "person/search"
                           "?query=" + name_to_search, headers=token_info
        )
        return result_search_by_name.json(), result_search_by_name.status_code

    def search_person_by_id(self, ind_id: str) -> Tuple[Dict[str, Any], int]:
        """Метод для поиска персоны по id
        Args:
            ind_id (int): id персоны
        Returns:
            Tuple[Dict[str, Any], int]: json ответ\
                  с информацией о персоне, статус коде
        """
        result_search_by_id = requests.get(
            base_url_api + "person/" + ind_id, headers=token_info
        )
        return result_search_by_id.json(), result_search_by_id.status_code