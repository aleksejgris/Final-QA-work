import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

   class MainPage:
       def __init__(self,browser):
          self._browser = browser
          self._browser.get('https://www.kinopoisk.ru/')
          self._browser.implicitly_wait(5)
          self._browser.maximize_window()

       def authorization(self):
          self._browser.find_element(XPath , '//button[contains(text(),"Войти")]'.click()

       def account(self):
           self._browser.find_element(By.CSS_SELECTOR, '[class="AuthaccountListItem-displayName"]').click()

       def password(self):
           self._browser.find_element(By.CSS_SELECTOR,"[class=Textinput Textinput_iconRight Textinput_view_conteast Textinput_asze_1]").send_keys("10071009al")

       def button_continue(self):
           self._browser.find_element(By.CSS_SELECTOR, '[class="Button2-Text"]').click()

       def data_entry(self):
           self._browser.find_element(By.NAME, 'kp_query').send_keys('Шрек')