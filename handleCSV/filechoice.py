import csv
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem
from handleCSV.optionschoice import UI as ChoiceApp


def read_csv(filename: str):                # função que lê o arquivo csv
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def load_csv(filename: str):                # função que lê o arquivo csv
    csv_data = read_csv(filename)

    app = ChoiceApp()
    app.show()

    app.filename = filename

    app.tableWidget.setRowCount(len(csv_data))
    app.tableWidget.setColumnCount(len(csv_data[0]))

    for i, row in enumerate(csv_data):
        for j, col in enumerate(row):
            app.tableWidget.setItem(i, j, QTableWidgetItem(col))

    app.exec_()


class App(QWidget):                         # classe que cria a interface
    def __init__(self):
        super().__init__()
        self.title = 'Leitor de CSV'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):                       # função que cria a interface
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()

        self.show()

    def openFileNameDialog(self):           # função que abre o arquivo csv
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecione um arquivo", "",
            "All Files (*);;CSV Files (*.csv)",
            options=options)

        if filename:
            load_csv(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
