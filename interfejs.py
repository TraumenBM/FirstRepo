from PyQt5.QtWidgets import QApplication, QWidget , QLabel, QGridLayout , QLineEdit, QPushButton,QHBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# V 1.0.0 Bmaturist

class Okno_IO(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()


    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def koniec(self):
            self.close()

    def interfejs(self):
        # przyciski
        dodajBtn = QPushButton("&Dodaj plik", self)
        wzBtn = QPushButton("&Wyswietl zaleznosci", self)
        pgBtn = QPushButton("&Pokaz graf", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(wzBtn)
        ukladH.addWidget(pgBtn)

        ukladT = QGridLayout()

        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)

        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)
        ukladT.addLayout(ukladH, 2, 0, 1, 3)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Program IO")
        self.show()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Okno_IO()
    sys.exit(app.exec_())
