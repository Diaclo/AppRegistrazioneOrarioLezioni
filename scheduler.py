from apscheduler.schedulers.background import BackgroundScheduler
import csv
from scrape import WebScraper
from datetime import datetime, date


class Scheduler:
    sched = None
    orariOggiFine = None

    def __init__(self):
        self.sched = BackgroundScheduler(daemon=True)

        corsi = self.leggiFile()
        for i in corsi:
            scrape = WebScraper(corsi[i][1])
            orariOggiInizio = [k for k in scrape.orarioInizio if datetime(2021, 3, 4).date() == k.date()]
            orariOggiFine = [k for k in scrape.orarioFine if datetime(2021, 3, 4).date() == k.date()]
            self.sched = BackgroundScheduler(daemon=True)

            for j in orariOggiInizio:
                print(j)
                self.sched.add_job(lambda: print('Anthony'), 'interval', seconds=1)
                self.sched.add_job(lambda: print('Anthony'), 'date', run_date=str(j))

    def leggiFile(self):
        with open('pyschedule.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            d = {}
            for k, t, o in reader:
                d[k] = t, o
                print(d)
            return d

    # def routine(self):

    def accensione(self):
        self.sched.start()

    def spegnimento(self):
        self.sched.shutdown()
