from bs4 import BeautifulSoup
import requests
from _datetime import datetime

url = "https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/385100/orariolezioni#404521"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table', {"id": "elenco"})
orario = []
orarioInizio = []
orarioFine = []
notallowed = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì']
TraduzioneMesi = {'febbraio': 'Feb',
                  'marzo': 'Mar',
                  'aprile': 'Apr',
                  'maggio': 'May'}


def scissioneOrario(lista_orario):
    for data in lista_orario:
        h1 = data[-11:-6]
        h2 = data[-5:]
        day = data[:-12]
        day1 = day + " " + h1
        day2 = day + " " + h2

        orarioInizio.append(datetime.strptime(day1, '%d %b %Y %H:%M'))
        orarioFine.append(datetime.strptime(day2, '%d %b %Y %H:%M'))


def formattazioneOrario(text):
    for giorno in notallowed:
        text = text.replace(giorno, '')

    return text.replace(" ", "").replace("\n", ' ').replace(',', ' ')


def meseToMonth(text):
    for mese in TraduzioneMesi:
        if mese in text:
            text = text.replace(mese, TraduzioneMesi[mese] + ' ')
            return text


for tr in table[0].findAll('tr'):
    tds = tr.find_all('td')
    for td in tds:
        if "La lezione si svolge solo online" not in td.text:
            orario.append(formattazioneOrario(td.text).strip())

scissioneOrario([meseToMonth(orario[i]) + ' ' + orario[i+1] for i in range(0, len(orario)-1, 2)])
del orario
