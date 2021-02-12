
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
 
class loginBot:
   def __init__(self, mail, password):
      self.mail = mail
      self.password = password
      self.caps = webdriver.DesiredCapabilities.CHROME.copy()
      self.caps['acceptInsecureCerts'] = True
      self.bot = webdriver.Chrome(desired_capabilities=self.caps)     
      self.bot.maximize_window()

   def goToPage(self):
      bot = self.bot
      """ # Accesso alla pagina 'Orari Corso'
      -> non più necessaria, si accede direttamente alla stanza teams
      bot.get('https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/461145/orariolezioni')
      time.sleep(5)
      elearning = bot.find_element_by_class_name('elearning a')
      elearning.send_keys(Keys.RETURN)
      time.sleep(5)
      """
      #bot.get('https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_Y2NmOTBlYzEtN2M2MC00ZGVmLTliOTAtMjI0NTJjN2IyNzk0%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%2522e99647dc-1b08-454a-bf8c-699181b389ab%2522%252c%2522Oid%2522%253a%2522080683d2-51aa-4842-aa73-291a43203f71%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=5ca1d260-d778-4949-b842-ec516db7edd0&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true')
      bot.get('https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_MTZlZmUyMmUtNzdhMi00ZjE2LThmMDMtOGQ3NDc4NjM1NmVk%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%2522e99647dc-1b08-454a-bf8c-699181b389ab%2522%252c%2522Oid%2522%253a%2522080683d2-51aa-4842-aa73-291a43203f71%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=2832b5cb-1985-4487-a563-e8201c84744c&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true')
      join = bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[3]/button[2]')
      join.send_keys(Keys.RETURN)
      time.sleep(10)

      attempt = 0
      while(attempt == 0):
         try:
            continueJoin = bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')
            continueJoin.send_keys(Keys.RETURN)
            if(continueJoin):
               attempt = 1
               print('done!!!')
         except:
            print('none')
            time.sleep(10)

   # script per login
   def login(self):
      bot = self.bot
      userName = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[1]/input')
      userName.clear()
      userName.send_keys(self.mail)
      time.sleep(3)
      join = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button')
      join.send_keys(Keys.RETURN)
      time.sleep(3)
      enter = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[1]/p[2]/a')
      enter.send_keys(Keys.RETURN)
      time.sleep(10)
      email = bot.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
      email.clear()
      email.send_keys(self.mail)
      time.sleep(3)
      email.send_keys(Keys.RETURN)
      time.sleep(5)
      password = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[2]/input')
      password.clear()
      password.send_keys(self.password)
      time.sleep(3)
      password.send_keys(Keys.RETURN)
      time.sleep(10)

      

      time.sleep(10)
      joinLast = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button')
      joinLast.send_keys(Keys.RETURN)
      time.sleep(3)

# Chiamata delle funzioni
log = loginBot('matteo.sacco4@studio.unibo.it', 'UniBo/2018')
log.goToPage()
log.login()
time.sleep(10)
