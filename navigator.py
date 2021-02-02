
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.common.by import By     
from selenium.webdriver.support import expected_conditions as EC

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
      # elearning = bot.find_element(By.XPATH('//*[@id="u-content-large"]/div[2]/div/div/ul/li[1]/p/a')).get_attribute('herf')
      bot.get(bot.find_element(By.XPATH('//*[@id="u-content-large"]/div[2]/div/div/ul/li[1]/p/a')).get_attribute('herf'))

      join = bot.find_element_by_link_text('Continua in questo browser')
      join.send_keys(Keys.RETURN)


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

