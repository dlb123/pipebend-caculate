import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QHeaderView, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from quality_window import Ui_MainWindow
from PyQt5.QtCore import Qt
import numpy as np
from bendpipe import BendPipe, Correct
import json
import xlrd
from dialog import Ui_Dialog
from myPlusFactory import MyPlusFactory
from del_factory import Del_Dialog
from update_factory import Update_Dialog
app = QApplication(sys.argv)
MainWindow = QMainWindow()


class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
        self.data = None
        with open('./factories.json', 'r+') as f:
            try:
                self.dcs = json.load(f)
            except json.decoder.JSONDecodeError:
                self.dcs = {}

    def fit(self):
        header = ['X', 'Y', 'Z']
        header2 = ['直线段长度','弧长','弯曲角度', '旋转角度']
        header3 = ['直线段长度','弧长','弯曲角度', '旋转角度']
        header3 = [string + '修正值' for string in header3[:-1]]
        r_list = [10, 16, 20, 30, 40, 50, 60, 70,]
        r_list = list(map(str, r_list))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:8pt '宋体';color: black;};")
        self.tableWidget.horizontalHeader().setFixedHeight(30)
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels(header)

        self.tableWidget_2.setColumnCount(len(header2))
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:8pt '宋体';color: black;};")
        self.tableWidget_2.setHorizontalHeaderLabels(header2)
        self.tableWidget_2.horizontalHeader().setFixedHeight(30)
        self.tableWidget_3.setColumnCount(len(header3))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setHorizontalHeaderLabels(header3)
        self.tableWidget_3.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:8pt '宋体';color: black;};")
        self.tableWidget_3.horizontalHeader().setFixedHeight(30)
        self.pushButton.setFocus()

        self.pushButton.setShortcut(Qt.Key_Enter)
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.add_items)

        self.pushButton_2.clicked.connect(self.insert_items)
        self.pushButton_3.clicked.connect(self.delete_items)
        self.pushButton_4.clicked.connect(self.clear_items)
        self.pushButton_5.clicked.connect(self.run)
        self.comboBox.addItems(r_list)
        self.comboBox.setAutoFillBackground(False)
        try:
            self.radius = int(self.comboBox.currentText())
        except ValueError:
            self.radius = 10
            self.comboBox.clearEditText()
        self.action.triggered.connect(self.add_factory)
        self.action_2.triggered.connect(self.update_factory)
        self.action_3.triggered.connect(lambda: self.del_factory())
        self.action_4.triggered.connect(lambda: self.action_triger(self.action_4))
        self.action_5.triggered.connect(lambda: self.action_triger(self.action_5))
        self.action_6.triggered.connect(lambda: self.action_triger(self.action_6))
        self.action_7.triggered.connect(self.read_excel)
        QMessageBox.warning(MainWindow, 'warning', ' 没有设备选择', QMessageBox.Ok)
        self.comboBox_2.addItems(sorted(list(self.dcs.keys())))
        self.tableWidget_4.setHorizontalHeaderLabels(['理论值', '实际值'])
        self.tableWidget_4.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:8pt '宋体';color: black;};")
        self.tableWidget_4.horizontalHeader().setFixedHeight(30)
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.returnPressed.connect(self.lineEdit_3.setFocus)
        self.lineEdit_3.returnPressed.connect(lambda: (self.add_items(), self.lineEdit.setFocus()))
    def read_excel(self):
        filename, filetype = QFileDialog.getOpenFileName(MainWindow, '选取Excel文件', os.getcwd())
        if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
            book = xlrd.open_workbook(filename)
            try:
                sheets = book.sheets()
                sheet = sheets[0]
                rows = list(sheet.get_rows())
                data = []
                if not len(rows):
                    raise ValueError('这是空数据表')
                for row in rows:
                    row_data = []
                    for cell in row:
                        if cell.value and cell.ctype:
                            row_data.append(cell.value)
                    data.append(row_data)
                    print(data)
                self.show_table(data)
            except:
                self.dialog_show(message='请选择数据表格'.center(15))
                return

    def update_factory(self):
        self.read_kv()
        if not self.dcs:
            self.dialog_show("warning", "没有设备可修改")
            return
        ui = Update_Dialog()
        Dialog = QDialog()
        ui.setupUi(Dialog)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowModality(Qt.ApplicationModal)
        ui.comboBox.addItems(sorted(list(self.dcs.keys())))

        def reshow(dc, combox, combox1):
            text = combox.currentText()
            combox1.clear()
            if text:
                combox1.addItems(sorted(list(dc[text].keys())))

            else:
                self.dialog_show(title='警告', message='没有选中的设备'.center(15))

            return

        ui.comboBox.currentIndexChanged.connect(lambda: reshow(self.dcs, ui.comboBox, ui.comboBox_1))
        ui.comboBox_1.currentIndexChanged.connect(lambda: reshow(self.dcs[ui.comboBox_1.currentText()],
                                                                ui.comboBox_1, ui.comboBox_2))
        text = ui.comboBox.currentText()
        data_fac = self.dcs[text]
        table = ui.tableWidget
        table.setVerticalHeaderLabels(['理论值', '修正值'])
        data = data_fac[2]
        table.clearContents()
        table.horizontalHeader().setVisible(False)
        table.setColumnCount(12)
        for i in range(table.columnCount()):
            table.setColumnWidth(i, 50)
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
                item = QTableWidgetItem(str(data[i][j]))
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                table.setItem(j, i, item)
        Dialog.show()
        u = ui
        d = Dialog
        if Dialog.exec_():
            text = u.comboBox.currentText()
            text1 = ui.lineEdit.text()
            text2 = ui.lineEdit_2.text()
            list3 = self.get_tabledata(ui.tableWidget)
            new_data = {text: [text1, text2, list3]}
            print('----++++')
            print(new_data)
            self.dcs.update(new_data)
            self.save_kv()
            self.dialog_show(title='信息', message='更新成功!'.center(15))
            del u, d

    def get_tabledata(self, table):
        rows, columns = table.rowCount(), table.columnCount()
        data = []
        for i in range(columns):
            item = []
            for j in range(rows):
                if table.item(j, i) and table.item(j, i).text():
                    print(table.item(j, i).text())
                    item.append(float(table.item(j, i).text()))
            if item:
                data.append(tuple(item))
        return data

    def add_factory(self):
        ui = MyPlusFactory()
        ui.fit()
        ui.Dialog.setWindowModality(Qt.ApplicationModal)
        ui.Dialog.show()
        if ui.Dialog.exec_():
            dc = ui.dc
            if not dc:
                self.dialog_show(message='请先添加设备信息'.center(15))
                return
            self.dcs.update(dc)
            self.save_kv()
            try:
                text = list(dc.keys())[0]
                self.comboBox_2.addItem(text)
                self.comboBox_2.setCurrentText(text)
            except IndexError:
                self.dialog_show('error', message='添加设备失败'.center(15))
                return
            self.dialog_show(title='信息', message='添加成功!'.center(15))

    def dialog_show(self, title='', message=''):
        dialog = Ui_Dialog()
        Dialog = QDialog()
        dialog.setupUi(Dialog)
        dialog.label.setText(message)
        Dialog.setWindowTitle(title)
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.show()
        Dialog.exec_()

    def del_factory(self):
        self.read_kv()
        ui = Del_Dialog()
        Dialog = QDialog()
        ui.setupUi(Dialog)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowModality(Qt.ApplicationModal)
        ui.comboBox.addItems(sorted(list(self.dcs.keys())))
        Dialog.show()
        d = Dialog
        u = ui
        if Dialog.exec_():
            self.del_text = u.comboBox.currentText()
            self.dcs.pop(self.del_text)
            self.save_kv()
            del d, ui
        self.comboBox_2.clear()
        self.comboBox_2.addItems(sorted(list(self.dcs.keys())))

    def read_kv(self):
        with open('./factories.json', 'r', encoding='UTF-8') as f:
            try:
                self.dcs = json.load(f)
            except json.decoder.JSONDecodeError:
                self.dcs = {}

    def save_kv(self):
        with open('./factories.json', 'w+', encoding='UTF-8') as f:
            json.dump(self.dcs, f)

    def action_triger(self, action):
        action.setChecked(True)
        for a in [self.action_4, self.action_5,self.action_6]:
            if a is not action:
                a.setChecked(False)

    def run(self):
        key = np.argmax([self.action_4.isChecked(), self.action_5.isChecked(), self.action_6.isChecked()])
        dc = {0: 0, 1: 2, 2: 3}
        self.precision = dc[key]
        self.change_radius()
        self.data = self.table_data()
        print(self.data)
        data = self.format_data()
        try:
            self.bendpipe = BendPipe(data, self.radius)
            data2, total2 = self.bendpipe.fit()
            self._show_table(self.tableWidget_2, data2)

            self.read_kv()


            if not self.comboBox_2.currentText():
                self.dialog_show(message='请先选择设备!')
                return
            dc = self.dcs.get(self.comboBox_2.currentText())
            data = dc[2]
            if not data:
                self.dialog_show(message="该设备无修正值")
                return
            theory, reality = [i for i, j in data], [j for i, j in data]
            self._show_table(self.tableWidget_4, [theory, reality])
            self.correct = Correct(self.bendpipe, theory, reality)
            data3 = self.correct.fit()

            self._show_table(self.tableWidget_3, data3)
        except ValueError as e:
            print(e)
            self.dialog_show(message=str(e))
        except Warning as w:
            self.dialog_show(message=str(w))

    def format_data(self):
        new_data = []
        if not self.data:
            return
        for row in self.data:
            row_data = []
            if not row:
                return
            for value in row:
                row_data.append(float(value))
            row_data = np.array(row_data)
            new_data.append(row_data)
        return np.array(new_data)

    def change_radius(self):
        try:
            self.radius = int(self.comboBox.currentText())
        except ValueError:
            self.radius = 10
            self.comboBox.clearEditText()

    def show_table(self, data):
        self.tableWidget.clearContents()
        rows = len(data)
        try:
            columns = len(data[0])
        except IndexError:
            columns = -1
        if rows > 10:
            self.tableWidget.setRowCount(rows)
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(str(data[i][j]))
                item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, item)

    def _show_table(self, table, data):
        format1 = '{{:.{}f}}'.format(self.precision)
        table.clearContents()
        rows = len(data)
        columns = len(data[0]) if data[0] else -1

        if rows > 10:
            table.setRowCount(rows)
        for i in range(columns):
            for j in range(rows):
                try:
                    if not data[j][i]:
                        continue
                    else:
                        item = QTableWidgetItem(format1.format(data[j][i]))
                        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        table.setItem(i, j, item)
                except IndexError:
                    continue

    def add_items(self):
        self.data = self.table_data()
        items = self.get_xyz()
        self.data.append(items)
        self.show_table(self.data)

    def delete_items(self):
        self.data = self.table_data()
        data_row = len(self.data)
        if not data_row:
            return
        row = self.tableWidget.currentRow()
        if row > data_row - 1 or row == -1:
            return
        try:
            self.data.pop(row)

        except IndexError:
            self.show_table(self.data)
        self.show_table(self.data)

    def clear_items(self):
        self.tableWidget.clearContents()

    def insert_items(self):
        self.data = self.table_data()
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        items = self.get_xyz()
        self.data.insert(row, items)
        self.show_table(self.data)

    def get_xyz(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        z = self.lineEdit_3.text()
        if not x:
            x = 0
        if not y:
            y = 0
        if not z:
            z = 0
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        return [x, y, z]

    def table_data(self):
        data = []
        for i in range(self.tableWidget.rowCount()):
            row = []
            for j in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(i, j) is not None:
                    row.append(self.tableWidget.item(i, j).text())
            if row:
                data.append(row)
        self.data = data
        return data


ui = MyMainWindow()
ui.fit()
MainWindow.show()
sys.exit(app.exec_())

