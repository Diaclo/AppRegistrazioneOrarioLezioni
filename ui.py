import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# System Tray
class App(QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.tray = QSystemTrayIcon(QIcon("icon.png"))
        self.tray.setVisible(True)

        menu = QMenu()
        configurazione = menu.addAction('Configurazione')
        configurazione.triggered.connect(self.openDialog)

        menu.addSeparator()
        esci = menu.addAction('Esci dal programma')
        esci.triggered.connect(lambda: sys.exit())

        self.tray.setContextMenu(menu)

    def openDialog(self):
        dialog = CustomDialog(self)
        dialog.exec()


# Dialog
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.setFixedWidth(420)
        self.setUI()

    def setUI(self):
        self.layout = QVBoxLayout()
        self.buttonBox = QHBoxLayout()

        self.Aggiungi = QPushButton('Aggiungi corso')
        self.Rimuovi = QPushButton('Rimuovi corso')
        self.Rimuovi.setDisabled(True)
        self.Aggiungi.clicked.connect(self.aggiungiLinea)
        self.Rimuovi.clicked.connect(self.rimuoviLinea)

        self.buttonBox.addWidget(self.Aggiungi)
        self.buttonBox.addWidget(self.Rimuovi)

        self.layout.addLayout(self.buttonBox)
        self.setLayout(self.layout)

    def aggiungiLinea(self):
        self.Rimuovi.setDisabled(False)

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
        print(len(self.layout))
        if len(self.layout) <= 2:
            self.Rimuovi.setDisabled(True)

    def pulisciLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            widget.deleteLater()

    # def accept(self):

    # def reject(self:


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Lesson Recorder")
    app.setApplicationVersion("0.1")
    app.setOrganizationName("Arcara&Sacco")

    win = App()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
