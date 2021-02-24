import sys
import csv
import os
from scheduler import Scheduler
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# System Tray
class App(QMainWindow):

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
        dialog.exec()

    def eseguiScheduler(self):
        # TODO: guardare bene la creazione e la cancellazione di una class
        # sched = Scheduler()
        if self.esegui.isChecked():
            self.esegui.setChecked(True)
            self.esegui.setText('In esecuzione...')
        else:
            self.esegui.setChecked(False)
            self.esegui.setText('Esegui in background')
            # del sched


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
        self.buttonBox.addWidget(self.UrlOrario, 2, 1)
        self.buttonBox.addWidget(self.UrlTeams, 2, 0)

        self.layout.addLayout(self.buttonBox)
        self.setLayout(self.layout)

    def aggiungiLinea(self):
        self.Rimuovi.setDisabled(False)
        self.Salva.setDisabled(False)

        hbox = QHBoxLayout()

        textCorso = QLabel(f'Corso {len(self.layout)}')
        editOrario = QLineEdit(self)
        editTeams = QLineEdit(self)
        hbox.addWidget(textCorso)
        hbox.addWidget(editOrario)
        hbox.addWidget(editTeams)

        self.layout.addLayout(hbox)
        if len(self.layout) >= 6:
            self.Aggiungi.setDisabled(True)

    def rimuoviLinea(self):
        self.Aggiungi.setDisabled(False)

        hbox = self.layout.itemAt(len(self.layout) - 1)
        self.pulisciLayout(hbox)
        hbox.deleteLater()
        self.adjustSize()
        if len(self.layout) <= 2:
            self.Salva.setDisabled(True)
            self.Rimuovi.setDisabled(True)

    def pulisciLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            widget.deleteLater()

    def save(self):
        # path = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'), 'CSV(*.csv')
        widget = []
        counter = 0
        # if path[0] != '':
        with open('pyschedule.csv', "w") as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            # skip QGridLayout
            hbox = (self.layout.itemAt(i) for i in range(1, self.layout.count()))
            for w in hbox:
                for j in range(w.count()):
                    widget.append(w.itemAt(j).widget().text())
                writer.writerow(widget[counter:])
                counter += 3


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
