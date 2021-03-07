import sys
import csv
import os
from scheduler import Scheduler
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import credentials

# System Tray
class App(QMainWindow):

    sched = Scheduler()

    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.tray = QSystemTrayIcon(QIcon("icon.png"))
        self.tray.setVisible(True)

        menu = QMenu()
        configurazione = menu.addAction('Configurazione')
        configurazione.triggered.connect(self.openDialog)

        self.esegui = menu.addAction('Esegui in background')
        self.esegui.triggered.connect(self.eseguiScheduler)
        self.esegui.setCheckable(True)
        self.esegui.setChecked(False)

        menu.addSeparator()
        esci = menu.addAction('Esci dal programma')
        esci.triggered.connect(lambda: sys.exit())

        self.tray.setContextMenu(menu)

    def openDialog(self):
        dialog = CustomDialog(self)
        dialog.center()
        dialog.exec()

    def eseguiScheduler(self):
        if not credentials.account == "" or not credentials.password == "":
            if self.esegui.isChecked():
                self.modificaEsegui(True, 'In esecuzione...', 'icon2.png')
                self.sched.accensione()
            else:
                self.modificaEsegui(False, 'Esegui in background', 'icon.png')
                self.sched.spegnimento()
        else:
            self.esegui.setChecked(False)
            msg = QMessageBox()
            # msg.setStyleSheet("QLabel{min-width: 120px;}");
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errore")
            msg.setInformativeText('Inserisci le credenziali')
            msg.setWindowTitle("Errore")
            msg.exec_()

    def modificaEsegui(self, boolean, testo, path):
        self.esegui.setChecked(boolean)
        self.esegui.setText(testo)
        self.tray.setIcon(QIcon(path))


# Dialog
class CustomDialog(QDialog):

    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.setFixedWidth(420)
        self.setUI()

    def setUI(self):
        self.layout = QVBoxLayout()
        self.buttonBox = QGridLayout()

        self.Aggiungi = QPushButton('Aggiungi corso')
        self.Rimuovi = QPushButton('Rimuovi corso')
        self.Salva = QPushButton('Salva')
        self.Cancella = QPushButton('Cancella')
        self.UrlOrario = QLabel('Url Orario')
        self.UrlTeams = QLabel('Url Teams')

        # Account e Password
        hboxAccountPassword = QHBoxLayout()
        self.Account = QLabel('Account: ')
        self.AccountLine = QLineEdit(credentials.account)
        self.Password = QLabel('Password: ')
        self.PasswordLine = QLineEdit(credentials.password)
        self.PasswordLine.setEchoMode(QLineEdit.Password)
        hboxAccountPassword.addWidget(self.Account)
        hboxAccountPassword.addWidget(self.AccountLine)
        hboxAccountPassword.addWidget(self.Password)
        hboxAccountPassword.addWidget(self.PasswordLine)

        self.Rimuovi.setDisabled(True)
        self.Salva.setDisabled(True)
        self.Aggiungi.clicked.connect(self.aggiungiLinea)
        self.Rimuovi.clicked.connect(self.rimuoviLinea)
        self.Salva.clicked.connect(self.save)
        self.Cancella.clicked.connect(self.reject)
        self.UrlOrario.setAlignment(Qt.AlignRight)
        self.UrlTeams.setAlignment(Qt.AlignRight)

        self.buttonBox.addWidget(self.Aggiungi, 0, 0)
        self.buttonBox.addWidget(self.Rimuovi, 0, 1)
        self.buttonBox.addWidget(self.Salva, 1, 0)
        self.buttonBox.addWidget(self.Cancella, 1, 1)
        self.buttonBox.addWidget(self.UrlOrario, 3, 1)
        self.buttonBox.addWidget(self.UrlTeams, 3, 0)

        self.layout.addLayout(hboxAccountPassword)
        self.layout.addLayout(self.buttonBox)
        self.setLayout(self.layout)

        self.precaricamento()

    def aggiungiLinea(self, default=..., orario="", teams=""):
        self.Rimuovi.setDisabled(False)
        self.Salva.setDisabled(False)

        hbox = QHBoxLayout()

        textCorso = QLabel(f'Corso {len(self.layout)-1}')
        editOrario = QLineEdit(orario)
        editTeams = QLineEdit(teams)
        hbox.addWidget(textCorso)
        hbox.addWidget(editOrario)
        hbox.addWidget(editTeams)

        self.layout.addLayout(hbox)
        if len(self.layout) >= 7:
            self.Aggiungi.setDisabled(True)

    def rimuoviLinea(self):
        self.Aggiungi.setDisabled(False)

        hbox = self.layout.itemAt(len(self.layout) - 1)
        self.pulisciLayout(hbox)
        hbox.deleteLater()
        self.adjustSize()
        if len(self.layout) <= 3:
            self.Salva.setDisabled(True)
            self.Rimuovi.setDisabled(True)

    def pulisciLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            widget.deleteLater()

    def precaricamento(self):
        with open('pyschedule.csv', "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.aggiungiLinea(orario=row[1], teams=row[2])

    def save(self):
        widget = []
        counter = 0
        with open('pyschedule.csv', "w") as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            # skip hboxAccountPassword
            # skip QGridLayout
            hbox = (self.layout.itemAt(i) for i in range(2, self.layout.count()))
            for w in hbox:
                for j in range(w.count()):
                    widget.append(w.itemAt(j).widget().text())
                writer.writerow(widget[counter:])
                counter += 3

            # TODO: Account e Password provvisori
            credentials.account = self.layout.itemAt(0).itemAt(1).widget().text()
            credentials.password = self.layout.itemAt(0).itemAt(3).widget().text()
        self.close()

    def center(self):
        frameGm = self.frameGeometry()
        # Returns the index of the screen that contains cursor
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        # Returns the geometry of the screen which contains widget
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

def main():
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)
    app.setApplicationName("Lesson Recorder")
    app.setApplicationVersion("0.1")
    app.setOrganizationName("Arcara&Sacco")

    win = App()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
