from apscheduler.schedulers.background import BackgroundScheduler
import csv
from scrape import WebScraper
from datetime import datetime, date


class Scheduler:
    sched = None
    orariOggiFine = None

    def __init__(self):
        self.scrape = WebScraper(self.leggiFile()[f'Corso {1}'][1])
        # orariOggiInizio = {k for k in scrape.orarioInizio if datetime(2021, 3, 4).date() == k.date()}
        # orariOggiFine = {k for k in scrape.orarioFine if datetime(2021, 3, 4).date() == k.date()}
        # print(orariOggiInizio)
        # print(orariOggiFine)

    def leggiFile(self):
        with open('pyschedule.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            d = {}
            for k, t, o in reader:
                d[k] = t, o
            return d

    def routine(self):
        orariOggiInizio = [k for k in self.scrape.orarioInizio if datetime(2021, 3, 4).date() == k.date()]
        self.sched.add_job(lambda: print('Anthony'), 'date', run_date=str(orariOggiInizio[0]))
        # self.sched.add_job(lambda: print('Anthony'), 'interval', seconds=1)

    def accensione(self):
        self.sched = BackgroundScheduler(daemon=True)
        self.routine()
        self.sched.start()

    def spegnimento(self):
        self.sched.shutdown()
