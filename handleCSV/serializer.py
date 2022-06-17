from PyQt5 import uic, QtWidgets
import pandas as pd
import os.path


class Serializer(QtWidgets.QDialog):
    def __init__(self):
        super(Serializer, self).__init__()
        uic.loadUi('templates/serialView.ui', self)

        self.tableWidget = self.findChild(
            QtWidgets.QTableWidget, 'tableWidget')

        cancelar = self.findChild(QtWidgets.QPushButton, 'pushButton')
        exportar = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        cancelar.clicked.connect(self.kill)
        exportar.clicked.connect(self.export)

        self.show()

    def serialize(self, filename: str):
        table = self.tableWidget
        rows = table.rowCount()
        cols = table.columnCount()

        data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(table.item(i, j).text())
            data.append(row)

        pd.DataFrame(data).to_csv(filename, index=False, header=False)

    def kill(self):
        self.close()

    def export(self):
        box = QtWidgets.QMessageBox()
        option = box.question(self, 'Confirmação', 'Deseja exportar o arquivo?', QtWidgets.QMessageBox.Yes |
                              QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)

        if option == QtWidgets.QMessageBox.Yes:
            text, ok = QtWidgets.QInputDialog.getText(
                self, 'Nomeie o arquivo', 'Digite o nome:')
            if ok:
                text = text.replace(' ', '_')
                text = text + '.csv'

                if os.path.isfile(text):
                    box = QtWidgets.QMessageBox()
                    option = box.question(self, 'Confirmação', 'O arquivo já existe. Deseja substituí-lo?', QtWidgets.QMessageBox.Yes |
                                          QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)

                    if option == QtWidgets.QMessageBox.Yes:
                        QtWidgets.QMessageBox.information(
                            self, 'Exportado', 'Arquivo exportado com sucesso!')
                        self.serialize(text)
                        self.close()

                    if option == QtWidgets.QMessageBox.No:
                        self.close()

                    if option == QtWidgets.QMessageBox.Cancel:
                        QtWidgets.QMessageBox.information(
                            self, 'Aviso', 'Operação cancelada.')
                        self.close()

                else:
                    QtWidgets.QMessageBox.information(
                        self, 'Exportado', 'Arquivo exportado com sucesso!')

                    self.serialize(text)
                    self.close()

        if option == QtWidgets.QMessageBox.No:
            box.close()
        if option == QtWidgets.QMessageBox.Cancel:
            box.close()
