from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 70, 821, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.menubar.setObjectName("menubar")
        self.menubbbb = QtWidgets.QMenu(self.menubar)
        self.menubbbb.setObjectName("menubbbb")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menubbbb.addAction(self.action)
        self.menubbbb.addAction(self.action_2)
        self.menubbbb.addAction(self.action_3)
        self.menubbbb.addSeparator()
        self.menubbbb.addAction(self.action_6)
        self.menubbbb.addAction(self.action_7)
        self.menubbbb.addAction(self.action_4)
        self.menubar.addAction(self.menubbbb.menuAction())

        self.gridLayout.setContentsMargins(30, 0, 30, 0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menubbbb.setTitle(_translate("MainWindow", "Инструменты"))
        self.action.setText(_translate("MainWindow", "Добавить"))
        self.action_2.setText(_translate("MainWindow", "Убрать"))
        self.action_3.setText(_translate("MainWindow", "Переместить"))
        self.action_6.setText(_translate("MainWindow", "Закрепить"))
        self.action_7.setText(_translate("MainWindow", "Закрепить по файлу"))
        self.action_4.setText(_translate("MainWindow", "Вещи в походе"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 549)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.namethings = QtWidgets.QLineEdit(Form)
        self.namethings.setGeometry(QtCore.QRect(180, 110, 201, 31))
        self.namethings.setObjectName("namethings")
        self.placethings = QtWidgets.QLineEdit(Form)
        self.placethings.setGeometry(QtCore.QRect(180, 170, 201, 31))
        self.placethings.setObjectName("placethings")
        self.addbtn = QtWidgets.QPushButton(Form)
        self.addbtn.setGeometry(QtCore.QRect(30, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addbtn.setFont(font)
        self.addbtn.setObjectName("addbtn")
        self.oke = QtWidgets.QPushButton(Form)
        self.oke.setGeometry(QtCore.QRect(394, 510, 71, 23))
        self.oke.setObjectName("oke")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(310, 510, 75, 23))
        self.exit.setObjectName("exit")
        self.photo = QtWidgets.QLabel(Form)
        self.photo.setGeometry(QtCore.QRect(230, 320, 201, 131))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 230, 281, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Добавить вещь"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_3.setText(_translate("Form", "Место"))
        self.addbtn.setText(_translate("Form", "Добавить фото"))
        self.oke.setText(_translate("Form", "ok"))
        self.exit.setText(_translate("Form", "cancel"))
        self.label_4.setText(_translate("Form", "Информация"))


class Ui_Form_Del(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 547)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 201, 351, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 130, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 510, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Удалить вещь"))
        self.label_2.setText(_translate("Form", "Название"))
        self.pushButton.setText(_translate("Form", "ok"))
        self.pushButton_2.setText(_translate("Form", "cancel"))


class Ui_MainWindowGarage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonback = QtWidgets.QPushButton(self.centralwidget)
        self.buttonback.setGeometry(QtCore.QRect(910, 730, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonback.setFont(font)
        self.buttonback.setObjectName("buttonback")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 461, 671))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(540, 370, 441, 281))
        self.photo.setObjectName("photo")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(540, 110, 441, 151))
        self.info.setObjectName("info")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.poisk = QtWidgets.QLineEdit(self.centralwidget)
        self.poisk.setGeometry(QtCore.QRect(760, 0, 271, 31))
        self.poisk.setObjectName("poisk")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 0, 31, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonback.setText(_translate("MainWindow", "назад"))
        self.pushButton.setText(_translate("MainWindow", "->"))


class Ui_Form_List(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 297)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
