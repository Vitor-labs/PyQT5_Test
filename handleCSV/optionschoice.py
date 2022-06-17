from PyQt5 import uic, QtWidgets
from handleCSV.serializer import Serializer
import pandas as pd


# função que lê o arquivo csv para serializar
def read_csv_to_serialize(options: dict, filename: str):
    columns = list(k for k, v in options.items() if v)

    df = pd.read_csv(filename, usecols=columns)

    return list(df.values), columns


# função que carrega os dados csv na tabela
def load_serializer(options, filename):
    app = Serializer()
    app.show()

    csv_data, columns = read_csv_to_serialize(options, filename)

    app.tableWidget.setRowCount(len(csv_data))
    app.tableWidget.setColumnCount(len(csv_data[0]))

    app.tableWidget.setHorizontalHeaderLabels(columns)

    for i, row in enumerate(csv_data):
        for j, col in enumerate(row):
            app.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))

    app.exec_()


class UI(QtWidgets.QDialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('templates/tableview.ui', self)
        self.setWindowTitle('Opções de visualização')
        self.filename = ''

        self.tableWidget = self.findChild(
            QtWidgets.QTableWidget, 'TableView')

        self.aplicar = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.limpar = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.cancelar = self.findChild(QtWidgets.QPushButton, 'pushButton_3')

        self.aplicar.clicked.connect(self.handle_options)
        self.limpar.clicked.connect(self.clear_options)
        self.cancelar.clicked.connect(self.kill)

        self.show()

    def kill(self):
        self.close()

    def handle_options(self):
        tamanho = self.findChild(QtWidgets.QCheckBox, 'checkBox_tamanho')
        mensagem = self.findChild(QtWidgets.QCheckBox, 'checkBox_mensagem')
        tipo = self.findChild(QtWidgets.QCheckBox, 'checkBox_tipo')
        data = self.findChild(QtWidgets.QCheckBox, 'checkBox_data')
        codigo = self.findChild(QtWidgets.QCheckBox, 'checkBox_codigo')
        ip = self.findChild(QtWidgets.QCheckBox, 'checkBox_ip')
        porta = self.findChild(QtWidgets.QCheckBox, 'checkBox_porta')
        comando = self.findChild(QtWidgets.QCheckBox, 'checkBox_comando')

        options = {
            'date_time': data.isChecked(),
            'ip': ip.isChecked(),
            'port': porta.isChecked(),
            'command': comando.isChecked(),
            'mime_type': tipo.isChecked(),
            'file_size': tamanho.isChecked(),
            'reply_code': codigo.isChecked(),
            'reply_msg': mensagem.isChecked()
        }

        message = 'Opções selecionadas: '
        for key, value in options.items():
            if value:
                message += key + ', '

        box = QtWidgets.QMessageBox()
        option = box.question(self, 'Confirmação', message, QtWidgets.QMessageBox.Yes |
                              QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)

        if option == QtWidgets.QMessageBox.Yes:
            load_serializer(options, self.filename)
            self.close()
        if option == QtWidgets.QMessageBox.No:
            box.close()
        if option == QtWidgets.QMessageBox.Cancel:
            self.close()

    def clear_options(self):
        tamanho = self.findChild(QtWidgets.QCheckBox, 'checkBox_tamanho')
        mensagem = self.findChild(QtWidgets.QCheckBox, 'checkBox_mensagem')
        tipo = self.findChild(QtWidgets.QCheckBox, 'checkBox_tipo')
        data = self.findChild(QtWidgets.QCheckBox, 'checkBox_data')
        codigo = self.findChild(QtWidgets.QCheckBox, 'checkBox_codigo')
        ip = self.findChild(QtWidgets.QCheckBox, 'checkBox_ip')
        porta = self.findChild(QtWidgets.QCheckBox, 'checkBox_porta')
        comando = self.findChild(QtWidgets.QCheckBox, 'checkBox_comando')

        tamanho.setChecked(False)
        mensagem.setChecked(False)
        tipo.setChecked(False)
        data.setChecked(False)
        codigo.setChecked(False)
        ip.setChecked(False)
        porta.setChecked(False)
        comando.setChecked(False)
