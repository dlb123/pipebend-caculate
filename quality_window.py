# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quality.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 677)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        #MainWindow.setWindowFlags(QtCore.Qt.Dialog)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 311))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(160, 40, 93, 28))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setIconSize(QtCore.QSize(30, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 80, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 200, 93, 28))
        self.pushButton_5.setObjectName('pushButton_5')
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 40, 91, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 91, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 120, 91, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 16, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(50, 190, 51, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 160, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 31, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 240, 181, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(290, 10, 441, 311))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 330, 731, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 731, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 431, 261))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(441, 0, 731, 261))
        self.tableWidget_4.setObjectName('table_4')
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(10)
        #self.tableWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 =QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setCheckable(False)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setCheckable(False)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setCheckable(True)
        self.action_4.setChecked(True)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setCheckable(True)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setCheckable(True)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "弯管坐标转换"))
        self.groupBox.setTitle(_translate("MainWindow", "工作区"))
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "插入"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_5.setText(_translate("MainWindow", "运行"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.label_3.setText(_translate("MainWindow", "Z:"))
        self.label_4.setText(_translate("MainWindow", "R:"))
        self.pushButton_4.setText(_translate("MainWindow", "全部删除"))
        self.label_5.setText(_translate("MainWindow", "设备:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "理论值"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "修正值"))
        self.menu.setTitle(_translate("MainWindow", "设备..."))
        self.menu_2.setTitle(_translate("MainWindow", "精确度"))
        self.menu_3.setTitle(_translate("MainWindow", '从文件读取...'))
        self.action.setText(_translate("MainWindow", "添加设备"))
        self.action_2.setText(_translate("MainWindow", "修改设备"))
        self.action_3.setText(_translate("MainWindow", "删除设备"))
        self.action_4.setText(_translate("MainWindow", " 保留整数"))
        self.action_5.setText(_translate("MainWindow", " 保留两位小数"))
        self.action_6.setText(_translate("MainWindow", " 保留三位小数"))
        self.action_7.setText(_translate("MainWindow", "从Excel读取"))

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())