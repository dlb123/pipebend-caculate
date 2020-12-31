from PyQt5.QtWidgets import  QTableWidgetItem, QDialog, QHeaderView
from plus_factory import Ui_Dialog as Plus_Dialog
from PyQt5.QtCore import Qt
import json
from dialog import Ui_Dialog


class MyPlusFactory(Plus_Dialog):
    def __init__(self):
        super().__init__()
        self.Dialog = QDialog()
        self.setupUi(self.Dialog)
        self.theory = []
        self.reality = []
        self.dc = {}

    def fit(self):
        self.pushButton_2.clicked.connect(self.add_factory)
        self.pushButton.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.tableWidget.clearContents)
        self.tableWidget.horizontalHeader().setVisible(False)
        length_init = 5
        self.tableWidget.setColumnCount(54 // length_init - 1)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(i, length_init * 10)
        self.tableWidget.setVerticalHeaderLabels(['理论值', '实际值'])
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(j, i, item)

    def add_data(self):
        theory = self.lineEdit_3.text()
        reality = self.lineEdit_5.text()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        print(theory)
        print(reality)
        if not(theory and reality):
            self.dialog_show(message='请同时提交两种值'.center(15))
            return
        try:
            self.theory.append(float(theory))
            self.reality.append(float(reality))
        except TypeError:
            self.dialog_show(message = '请检查输入数据的格式是否正确!')
        #self.tableWidget.clearContents()
        self._show_table(self.tableWidget, [self.theory, self.reality])

    def add_factory(self):
        with open('./factories.json', 'r') as f:
            try:
                dcs = json.load(f)
            except json.decoder.JSONDecodeError:
                dcs = {}
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        text3 = self.lineEdit_4.text()
        if text1 == '':
            self.dialog_show(message='设备名不能为空')
            return

        if text1 not in list(dcs.keys()):
            self.dc = {text1: [text2, text3, []]}
            print(self.dc)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
        else:
            self.dialog_show(message='该设备名已存在!')

    def dialog_show(self, message):
        dialog = Ui_Dialog()
        Dialog = QDialog()
        dialog.setupUi(Dialog)
        dialog.label.setText(message)
        Dialog.show()
        Dialog.exec_()

    def _show_table(self, table, data):
        table.clearContents()
        rows = 2
        try:
            columns = len(data[0]) if data[0] else -1
        except IndexError:
            columns = -1
        print(data)
        if columns > table.columnCount():
            table.setColumnCount(columns)
        for i in range(columns):
            for j in range(rows):
                item = QTableWidgetItem(str(data[j][i]))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                table.setItem(j, i, item)