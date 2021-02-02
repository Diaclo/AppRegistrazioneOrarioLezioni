
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.common.by import By     
from selenium.webdriver.support import expected_conditions as EC
import Selenium2Library

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
      time.sleep(5)
      elearning = bot.find_element_by_class_name('elearning a')
      elearning.send_keys(Keys.RETURN)
      time.sleep(5)
      
      url = bot.current_url()
      print(url)
      
      #bot.get('https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_Y2NmOTBlYzEtN2M2MC00ZGVmLTliOTAtMjI0NTJjN2IyNzk0%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%2522e99647dc-1b08-454a-bf8c-699181b389ab%2522%252c%2522Oid%2522%253a%2522080683d2-51aa-4842-aa73-291a43203f71%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=5ca1d260-d778-4949-b842-ec516db7edd0&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true')
      
      """
      join = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[3]/button[2]')
      join.send_keys(Keys.RETURN)
      time.sleep(10)
      """

      #continueJoin = bot.find_element_by_class_name('ts-btn-fluent-secondary-alternate')
      #continueJoin = bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button/text()')
      #continueJoin.send_keys(Keys.RETURN)

   # script per login qualora fosse necessario accedere
   """
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
   """

# Chiamata delle funzioni

log = loginBot('username', 'password')
log.goToPage()

