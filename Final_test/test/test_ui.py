from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Final_test.test.ui_methods import MainPage
from test.ui_methods import MainPage

@allure.title("Проверка сайта кинопоиск")
@allure.description("Авторизация на сайте ,поиск фильма по названию,получения нужного результата")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_open_kinopoisk():
     with allure.step("Открыть сайт кинопоиск"):
     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
     main_page = MainPage(browser)
     with allure.step("Кликнуть кнопку войти"):
     main_page.authorization()
     with allure.step("Выбрать аккаунт А-1007.А"):
     main_page.account()
     with allure.step("Ввести пароль" ,'10071009al'):
     main_page.password()
     with allure.step("Кликнуть кнопку Продолжить"):
     main_page.button_continue()
     with allure.step("В поле поиск ввести Шрек"):
     main_page.button_continue()