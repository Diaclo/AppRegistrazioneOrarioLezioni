import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.support import expected_conditions as EC


class Navigator:
    def __init__(self, mail, password, link):
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })

        self.mail = mail
        self.password = password
        self.caps = webdriver.DesiredCapabilities.CHROME.copy()
        self.caps["acceptInsecureCerts"] = True
        self.bot = webdriver.Chrome(chrome_options=opt, executable_path=r'./chromedriver')
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
        self.bot.get(self.link)
        join = self.bot.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/div/div[3]/button[2]"
        )
        join.send_keys(Keys.RETURN)
        time.sleep(10)

        attempt = 0
        while attempt == 0:
            try:
                continueJoin = self.bot.find_element_by_xpath(
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
        userName = self.bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[1]/input"
        )
        userName.clear()
        userName.send_keys(self.mail)
        time.sleep(3)
        join = self.bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button"
        )
        join.send_keys(Keys.RETURN)
        time.sleep(3)
        enter = self.bot.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[1]/p[2]/a"
        )
        enter.send_keys(Keys.RETURN)
        time.sleep(10)
        email = self.bot.find_element_by_xpath(
            "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
        )
        email.clear()
        email.send_keys(self.mail)
        time.sleep(3)
        email.send_keys(Keys.RETURN)
        time.sleep(5)
        password = self.bot.find_element_by_xpath(
            "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"
            #"/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[2]/input"
        )
        password.clear()
        password.send_keys(self.password)
        time.sleep(3)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

        bntNoPermConn = self.bot.find_element_by_xpath(
            "/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input"
        )
        bntNoPermConn.send_keys(Keys.RETURN)

    def lastjoin(self):
        time.sleep(10)
        attempt = 0
        while attempt == 0:
            try:
                continueLastJoin = self.bot.find_element_by_xpath(
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
        partecipa = self.bot.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button"
        )
        partecipa.send_keys(Keys.RETURN)
        time.sleep(3)

    def closeTabs(self):
        time.sleep(3)
        microphoneAd = self.bot.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-screen/div/div[2]/calling-unified-bar/calling-alert/div/div/div/calling-ufd-popup/div/div[2]/div[4]/button"
        )
        microphoneAd.send_keys(Keys.RETURN)

        notificationAd = self.bot.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/button[2]"
        )
        notificationAd.send_keys(Keys.RETURN)
        time.sleep(3)