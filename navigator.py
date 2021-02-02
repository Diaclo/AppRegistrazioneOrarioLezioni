
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class loginBot:
    def __init__(self, username, password):
      self.username = username
      self.password = password
      self.caps = webdriver.DesiredCapabilities.CHROME.copy()
      self.caps['acceptInsecureCerts'] = True
      self.bot = webdriver.Chrome(desired_capabilities=self.caps)     
      self.bot.maximize_window()

    def goToPage(self):
        bot = self.bot
        bot.get('https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/461145/orariolezioni')
        elearning = bot.find_element_by_class_name('elearning a')
        elearning.send_keys(Keys.RETURN)

        # Non trova l'alert dell'apertura di teams
        bot.switch_to_alert('Aprire Microsoft Teams?')
        bot.find_element_by_link_text('Annulla').send_keys(Keys.RETURN)
        bot.switch_to_default_content()
        # ########################################


    def login(self):
      bot = self.bot
      bot.get('link') # aggiungere il link
      time.sleep(5)
      email = bot.find_element_by_class_name('nome classe')
      password = bot.find_element_by_name('nome classe')
      email.clear()
      password.clear()
      email.send_keys(self.username)
      password.send_keys(self.password)
      password.send_keys(Keys.RETURN)
      time.sleep(5)

log = loginBot('username', 'password')
log.goToPage()

