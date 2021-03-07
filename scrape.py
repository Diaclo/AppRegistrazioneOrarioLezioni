from bs4 import BeautifulSoup
import requests
from _datetime import datetime

exceptions = ['online', 'AULA', 'LAB']
notallowed = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì']
TraduzioneMesi = {'febbraio': 'Feb',
                  'marzo': 'Mar',
                  'aprile': 'Apr',
                  'maggio': 'May',
                  'giugno': 'Jun'}


class WebScraper:

    orarioInizio = []
    orarioFine = []

    def __init__(self, url):
        self.url = url
        if self.url.startswith("https://"):
            orario = []
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.findAll('table', {"id": "elenco"})
            for tr in table[0].findAll('tr'):
                tds = tr.find_all('td')
                for td in tds:
                    if not any(ext in td.text for ext in exceptions):
                        orario.append(self.formattazioneOrario(td.text).strip())
            self.scissioneOrario([self.meseToMonth(orario[i]) + ' ' + orario[i + 1] for i in range(0, len(orario) - 1, 2)])
            del orario
        else:
            print("Not valid URL")
            self.orarioInizio.clear()
            self.orarioFine.clear()

    def scissioneOrario(self, lista_orario):
        for data in lista_orario:
            h1 = data[-11:-6]
            h2 = data[-5:]
            day = data[:-12]
            day1 = day + " " + h1
            day2 = day + " " + h2

            self.orarioInizio.append(datetime.strptime(day1, '%d %b %Y %H:%M'))
            self.orarioFine.append(datetime.strptime(day2, '%d %b %Y %H:%M'))

    def formattazioneOrario(self, text):
        for giorno in notallowed:
            text = text.replace(giorno, '')

        return text.replace(" ", "").replace("\n", ' ').replace(',', ' ')

    def meseToMonth(self, text):
        for mese in TraduzioneMesi:
            if mese in text:
                text = text.replace(mese, TraduzioneMesi[mese] + ' ')
                return text
