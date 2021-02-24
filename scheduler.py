# # import schedule
import csv
from scrape import WebScraper


# import time


class Scheduler:

    def __init__(self):
        scrape = WebScraper(self.leggiFile()[f'Corso {1}'][1])
        print(scrape.orarioInizio)
        print(scrape.orarioFine)

    def leggiFile(self):
        with open('pyschedule.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            d = {}
            for k, t, o in reader:
                d[k] = t, o
            return d


sched = Scheduler()
