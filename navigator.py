import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.support import expected_conditions as EC


class Navigator:
    def __init__(self, mail, password, link):
        self.mail = mail
        self.password = password
        self.caps = webdriver.DesiredCapabilities.CHROME.copy()
        self.caps["acceptInsecureCerts"] = True
        self.bot = webdriver.Chrome('/Users/alessioarcara/PycharmProjects/AppRegistrazioneOrarioLezioni/chromedriver')
        # desired_capabilities=self.caps)
        self.bot.maximize_window()
        # self.bot = webdriver.Safari()
        # self.bot.maximize_window()
        self.link = link

        self.goToPage()
        self.login()
        self.lastjoin()
        self.closeTabs()

    def goToPage(self):
        bot = self.bot
        link = self.link
        bot.get(link)
        join = bot.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/div[3]/button[2]"
        )
        join.send_keys(Keys.RETURN)
        time.sleep(10)

        attempt = 0
        while attempt == 0:
            try:
                continueJoin = bot.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button"
                    # "/html/body/div[4]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button"
                )
                continueJoin.send_keys(Keys.RETURN)
                if continueJoin:
                    attempt = 1
                    print("done!!!")
            except:
                print("none")
                time.sleep(10)

    # script per login
    def login(self):
        bot = self.bot
        userName = bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[1]/input"
        )
        userName.clear()
        userName.send_keys(self.mail)
        time.sleep(3)
        join = bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button"
        )
        join.send_keys(Keys.RETURN)
        time.sleep(3)
        enter = bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[1]/p[2]/a"
        )
        enter.send_keys(Keys.RETURN)
        time.sleep(10)
        email = bot.find_element_by_xpath(
            "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
        )
        email.clear()
        email.send_keys(self.mail)
        time.sleep(3)
        email.send_keys(Keys.RETURN)
        time.sleep(5)
        password = bot.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[2]/input"
        )
        password.clear()
        password.send_keys(self.password)
        time.sleep(3)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

        bntNoPermConn = bot.find_element_by_xpath(
            "/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input"
        )
        bntNoPermConn.send_keys(Keys.RETURN)

    def lastjoin(self):
        bot = self.bot
        time.sleep(10)
        attempt = 0
        while attempt == 0:
            try:
                continueLastJoin = bot.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button"
                )
                continueLastJoin.send_keys(Keys.RETURN)
                if continueLastJoin:
                    attempt = 1
                    print("done!!!")
            except:
                print("none")
                time.sleep(10)

        time.sleep(10)
        partecipa = bot.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button"
        )
        partecipa.send_keys(Keys.RETURN)
        time.sleep(3)

    def closeTabs(self):
        bot = self.bot
        time.sleep(3)
        microphoneAd = bot.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-screen/div/div[2]/calling-unified-bar/calling-alert/div/div/div/calling-ufd-popup/div/div[2]/div[4]/button"
        )
        microphoneAd.send_keys(Keys.RETURN)

        notificationAd = bot.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/button[2]"
        )
        notificationAd.send_keys(Keys.RETURN)
        time.sleep(3)