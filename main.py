from PyQt5 import uic, QtWidgets
import sys

from handleCSV.filechoice import App


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('templates\main.ui', self)

        button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        cancel = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        button.clicked.connect(self.handle_click)
        cancel.clicked.connect(self.kill)

        self.show()

    def kill(self):
        self.close()

    def handle_click(self):
        self.close()

        self.app = App()
        self.app.show()
        self.app.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
