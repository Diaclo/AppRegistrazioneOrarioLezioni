from apscheduler.schedulers.background import BackgroundScheduler
from threading import Thread
import csv
from scrape import WebScraper
from navigator import Navigator
from datetime import datetime, date


class Scheduler:
    sched = None
    # orariOggiFine = None

    def __init__(self):
        self.sched = BackgroundScheduler(daemon=True)
        thread = Thread(target=self.settaggioJobs)
        print("waiting... scheduler is loading")
        thread.start()
        thread.join()
        print("scheduler is ready... ")

    def settaggioJobs(self):
        corsi = self.leggiFile()
        for i in corsi:
            scrape = WebScraper(corsi[i][1])
            # date.today()
            # datetime(2021, 3, 4).date()
            orariOggiInizio = [k for k in scrape.orarioInizio if datetime(2021, 3, 4).date() == k.date()]
            # orariOggiFine = [k for k in scrape.orarioFine if datetime(2021, 3, 4).date() == k.date()]

            if orariOggiInizio:
                for j in orariOggiInizio:
                    self.sched.add_job(self.driver, 'interval', [corsi[i][0]], seconds=1)
                    self.sched.add_job(lambda: print('Anthony'), 'date', run_date=str(j))

    def leggiFile(self):
        with open('pyschedule.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            d = {}
            for k, t, o in reader:
                d[k] = t, o
                print(d[k])
            return d

    def driver(self, urlTeams):
        import credentials
        navigator = Navigator(credentials.account, credentials.password, urlTeams)

    def accensione(self):
        self.sched.start()

    def spegnimento(self):
        self.sched.shutdown()
