import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSizePolicy, QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QColor
from designewidgets import *
import random
import sqlite3

PICTURES = ['imagin/p9.jpg', 'imagin/p3.jpg', 'imagin/p2.jpg', 'imagin/1p88.jpg']  # фоны


class BD:  # класс базы данных
    def giveAllPlace(self, id=''):
        self.start()
        f = 'SELECT name FROM place WHERE id IN (SELECT id_place FROM things WHERE inlis="no") ' + id
        lis = self.cur.execute(f).fetchall()
        self.end()
        return lis

    def appendInformation(self, text):
        self.start()
        self.cur.execute('INSERT INTO dinfo(inf) VALUES(?)', [text])
        self.end()

    def giveItemInLower(self, t):
        self.start()
        lis = self.cur.execute(
            f'SELECT name FROM things WHERE id = (SELECT id_thing FROM namelower WHERE name="{t}")').fetchall()
        self.end()
        return lis[0][0]

    def start(self):
        self.con = sqlite3.connect('forward.db')
        self.cur = self.con.cursor()
        self.con("PRAGMA foreign_keys = 1")
        self.cur = self.con.cursor()

    def end(self):
        self.con.commit()
        self.con.close()

    def cgangeElementFromPerem(self, t, p):
        self.start()
        try:
            self.cur.execute('INSERT INTO place(name) VALUES(?)', [p])
        except Exception:
            pass
        self.cur.execute(f'''UPDATE things SET id_place=(SELECT id FROM place WHERE name="{p}")
        WHERE id=(SELECT id_thing FROM namelower WHERE name="{t.lower()}")''')
        self.cur.execute('DELETE FROM place WHERE id NOT IN (SELECT id_place FROM things)')
        self.end()

    def listWithLisinFalse(self, text, inl='no'):
        self.start()
        self.cur.execute(f'''UPDATE things SET inlis="{inl}" WHERE id=
        (SELECT id_thing FROM namelower WHERE name="{text.lower()}")''')
        self.end()

    def listWithLisinTrue(self, t):
        self.start()
        lis = self.cur.execute(f'SELECT name FROM things WHERE inlis="{t}"').fetchall()
        self.end()
        return lis

    def giveNameList(self, t):
        self.start()
        self.cur.execute(f'UPDATE things SET inlis="yes" WHERE id=(SELECT id_thing FROM namelower WHERE name="{t}")')
        self.end()

    def delElement(self, things):
        self.start()
        f = f'''DELETE FROM things WHERE id = (SELECT id_thing FROM namelower WHERE name="{things.lower()}")'''
        self.cur.execute(f)
        lis = tuple(map(lambda x: x[0], self.cur.execute('SELECT id_place FROM things').fetchall()))
        self.cur.execute('DELETE FROM place WHERE id NOT IN (SELECT id_place FROM things)')
        # f = f'''DELETE FROM things WHERE namelower="{things.lower()}"'''
        # self.cur.execute(f'DELETE FROM dinfo WHERE id=(SELECT id FROM things WHERE namelower="{things.lower()}")')
        # self.cur.execute(f)
        self.end()

    def givePlaceFromThings(self, things):
        self.start()
        f = f'''SELECT name FROM place WHERE id = (SELECT id_place FROM things WHERE
         id = (SELECT id_thing FROM namelower WHERE name LIKE "%{things.lower()}%") AND inlis="no")'''
        lis = self.cur.execute(f).fetchall()
        self.end()
        return lis

    def giveItemFromRun(self, place):
        self.start()
        if place == 'Полный список':
            f = f'''SELECT name, id_place FROM things WHERE inlis="no"'''
        else:
            f = f'''SELECT name FROM things WHERE id_place = (SELECT id FROM place WHERE name = "{place}") AND inlis="no"'''
        lis = self.cur.execute(f).fetchall()
        self.end()
        return lis

    def giveItemFromChange(self, t, place):
        self.start()
        if place.lower() == 'полный список' or place == 'del':
            f = f'''SELECT name, id_place FROM things WHERE id IN (SELECT id_thing FROM namelower WHERE name LIKE "%{t}%")
             AND inlis="no"'''
        else:
            f = f'''SELECT name FROM things WHERE id IN (SELECT id_thing FROM namelower WHERE name LIKE "%{t}%")
             AND inlis="no" AND id_place = (SELECT id FROM place WHERE name = "{place}")'''
        lis = self.cur.execute(f).fetchall()
        self.end()
        return lis

    def givePhotoFromSearch(self, text, place, label, w, h):  # поиск без учёта регистра
        self.start()
        f = f'''SELECT name FROM photo WHERE id_thing = (SELECT id FROM things WHERE id = (SELECT id_thing FROM namelower WHERE name = "{text.lower()}"))'''
        pht = self.cur.execute(f).fetchall()
        try:
            qimg = QtGui.QImage.fromData(pht[0][0])
            pixmap = QtGui.QPixmap(qimg)
            pixmap4 = pixmap.scaled(int(w * 0.4), int(h * 0.4), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap4)
        except Exception:
            label.clear()
        finally:
            self.end()

    def appendElementInBase(self, name, place, file):
        self.start()
        try:
            self.cur.execute(f'INSERT INTO place(name) VALUES(?)', [place])
        except Exception:
            pass
        self.cur.execute('INSERT INTO things(name, inlis, id_place) VALUES(?, ?, ?)',
                         [name, 'no', self.cur.execute(f'SELECT id FROM place WHERE name="{place}"').fetchone()[0]])
        if file:
            pht = open(file, 'rb')
            h = pht.read()
            self.cur.execute('INSERT INTO photo(name, id_thing) VALUES(?, ?)',
                             [h, self.cur.execute(f'SELECT id FROM things WHERE name="{name}"').fetchone()[0]])
            # self.cur.execute('INSERT INTO things(name, place, photo, namelower, inlis) VALUES(?, ?, ?, ?, ?)',
            #                 [name, place, h, name.lower(), 'no'])
        self.cur.execute('INSERT INTO namelower(name, id_thing) VALUES(?, ?)',
                         [name.lower(), self.cur.execute(f'SELECT id FROM things WHERE name="{name}"').fetchone()[0]])
        self.end()


class Table:  # класс таблицы вещей и мест
    def __init__(self, tb):
        self.tb = tb

    def makeTable(self, items, place_in, tbold=''):
        self.tb.setRowCount(len(items))
        self.tb.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tb.horizontalHeader().setVisible(False)

        if place_in.lower() == 'полный список':
            self.tb.setColumnCount(2)
        else:
            self.tb.setColumnCount(1)
        row = 0

        for tup in items:
            if tbold != '' and len(tbold) != 1:
                word = tup[0]
                h = word.lower()
                new_word = word[:h.index(tbold.lower())] + tbold.upper() + word[h.index(tbold.lower()) + len(tbold):]
            else:
                new_word = tup[0]
            self.tb.setItem(row, 0, QTableWidgetItem(new_word))
            if place_in.lower() == 'полный список':
                self.tb.setItem(row, 1, QTableWidgetItem((DATABASE.giveAllPlace(f'AND id="{tup[1]}"'))[0][0]))
            row += 1


class Garage(Ui_MainWindowGarage, QMainWindow):  # класс,показывающий именно то место, на кнопку которого ткнули
    def __init__(self, x, n_wind):
        super(Garage, self).__init__()
        if n_wind == 'Список':
            n_wind = 'Полный список'
        self.n_wind = n_wind
        self.setupUi(self)
        self.setGeometry(x)
        self.label.setText(n_wind)

        self.table = Table(self.tableWidget)

        self.buttonback.clicked.connect(self.goMainw)
        self.pushButton.clicked.connect(self.search)

        self.poisk.textChanged.connect(self.textChang)

        self.tableWidget.cellClicked.connect(self.tabletsignal)

        self.run()

    def tabletsignal(self, x, y):  # улавливание сигналов нажатий на ячейки таблицы
        try:
            text = self.tableWidget.item(x, y).text()  # заглавные буквы при выводе
            self.plreturne(text)
            DATABASE.givePhotoFromSearch(text, DATABASE.givePlaceFromThings(text)[0][0], self.photo,
                                         self.size().width(),
                                         self.size().height())
        except Exception:
            print('error')

    def plreturne(self, text):  # вывод информации
        t = DATABASE.giveItemInLower(text.lower())
        self.info.setText(
            f'{t[0].upper() + t[1:]}:\nМесто: {DATABASE.givePlaceFromThings(text)[0][0]}')
        self.info.setStyleSheet('font-size: 40px')
        self.poisk.setText('')
        self.statusbar.showMessage('')

    def keyPressEvent(self, event):  # улавливание сигнала нажатия на Enter при поиске вещей
        if event.key() == event.key() == Qt.Key_Return:
            if self.poisk.text() != '':
                self.search()

    def textChang(self):  # улавливание сигнала изменения текста при поиске вещей
        text = self.poisk.text().lower()
        lis = DATABASE.giveItemFromChange(text, self.label.text())

        self.table.makeTable(lis, self.label.text(), text)

    def resizeEvent(self, event):  # динамическое изменение размеров всех объектов
        width = self.size().width()
        height = self.size().height()

        self.tableWidget.resize(int(width * 0.4), int(height * 0.88))
        self.info.resize(int(width * 0.48), int(height * 0.3))
        self.info.move(int(width * 0.48), 100)
        self.photo.resize(int(width * 0.48), int(height * 0.4))
        self.photo.move(int(width * 0.48), 450)

        self.buttonback.move(width - 116, height - 56)
        self.poisk.move(width - 200, 0)
        self.pushButton.move(width - 30, 0)

    def goMainw(self):  # возвращение к главному окуну при нажатии на кнопку назад
        size = self.geometry()
        self.mainw = Mainw(size)
        self.mainw.show()
        self.close()

    def run(self):
        place_in = self.label.text()
        self.result = DATABASE.giveItemFromRun(place_in)
        self.table.makeTable(self.result, place_in.lower())

    def search(self):  # поиск вещей в виджете ввода
        lis = list(map(lambda x: x[0].lower(), self.result))
        text = self.poisk.text().lower()

        if text != '':
            if text in lis:
                self.plreturne(text)
                DATABASE.givePhotoFromSearch(text, DATABASE.givePlaceFromThings(text)[0][0], self.photo,
                                             self.size().width(), self.size().height())
            else:
                self.statusbar.showMessage('Такой вещи тут нет')


class Action(Ui_Form, QWidget):  # окно добавления вещей
    sig = pyqtSignal()  # сигнал закрытия

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = False

        self.addbtn.clicked.connect(self.addphoto)
        self.oke.clicked.connect(self.add)
        self.exit.clicked.connect(self.ex)

    def add(self):
        name = self.namethings.text()
        place = self.placethings.text()
        info = self.lineEdit.text()
        if len(place) > 12:
            place = place[:12] + '.'
        DATABASE.appendElementInBase(name, place, self.fname)
        self.sig.emit()
        self.close()

    def addphoto(self):
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.jpeg);;Все файлы (*)')[0]
        print(self.fname)
        pixmap = QPixmap(self.fname)
        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.photo.setPixmap(pixmap)

    def ex(self):
        self.close()


class Action2(Ui_Form_Del, QWidget):  # окно удаления и закрепления вещей
    sig = pyqtSignal()  # улавливание сигнала выхода

    def __init__(self, text):
        super().__init__()
        self.lis = []
        self.setupUi(self)
        self.tb = Table(self.tableWidget)

        self.pushButton_2.clicked.connect(self.ex)
        self.pushButton.clicked.connect(self.ex)

        self.lineEdit.textChanged.connect(self.textChang)
        self.tableWidget.cellClicked.connect(self.tabletsignal)

        if text != 'Убрать':
            self.label.setText('Закрепить')
            self.tb.makeTable(DATABASE.listWithLisinTrue('no'), '-')
            self.pushButton.clicked.connect(self.okeZakrep)
        else:
            self.label.setText('Удалить')
            self.tb.makeTable(DATABASE.giveItemFromChange(self.lineEdit.text().lower(), 'del'), '-')
            self.pushButton.clicked.connect(self.okeDelete)

    def textChang(self):
        text = self.lineEdit.text().lower()
        lis = DATABASE.giveItemFromChange(text, 'del')
        self.tb.makeTable(lis, '-', text)

    def tabletsignal(self, x, y):
        text = self.tableWidget.item(x, y).text().lower()
        self.tableWidget.item(x, 0).setBackground(QtGui.QColor(180, 180, 180))
        self.lis.append(text)

    def okeDelete(self):
        lastname = self.lineEdit.text()
        for el in self.lis:
            DATABASE.delElement(el)
        try:
            DATABASE.delElement(lastname)
        except Exception:
            pass
        self.sig.emit()
        self.ex()

    def okeZakrep(self):
        lastname = self.lineEdit.text()
        for el in self.lis:
            DATABASE.giveNameList(el)
        try:
            DATABASE.giveNameList(lastname)
        except Exception:
            pass
        self.sig.emit()
        self.ex()

    def ex(self):
        self.close()


class ActionList(Ui_Form_List,
                 QWidget):  # окно с таблицей вещей, которые закреплены или находятся в подвижном состоянии
    sig = pyqtSignal()  # улавливание сигнала выхода

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb = Table(self.tableWidget)
        lis = DATABASE.listWithLisinTrue('yes')
        self.tb.makeTable(lis, '-')
        self.tableWidget.cellClicked.connect(self.tabletsignal)

    def closeEvent(self, event):
        self.sig.emit()

    def tabletsignal(self, x, y):
        self.flag = True
        self.text = self.tableWidget.item(x, y).text()
        self.msgbox = QMessageBox(self)
        self.msgbox.setWindowTitle("Information")
        self.msgbox.setText(f'Убрать вещь {self.text} из списка')
        self.msgbox.addButton(QtWidgets.QMessageBox.Ok)

        yes_button = self.msgbox.addButton('cancel', QtWidgets.QMessageBox.YesRole)
        yes_button.clicked.disconnect()
        yes_button.clicked.connect(self.gor)

        bttn = self.msgbox.exec_()

        if bttn and self.flag:
            self.tableWidget.removeRow(x)
            DATABASE.listWithLisinFalse(self.text)

    def gor(self):
        self.msgbox.done(1)
        self.flag = False


class ActionPerem(Ui_Form_Del, QWidget):  # окно перемещения вещей в другие места
    sig = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb = Table(self.tableWidget)
        self.tb.makeTable(DATABASE.listWithLisinTrue('no'), '-')

        self.label.setText('Переместить')
        self.label_2.setGeometry(QtCore.QRect(70, 90, 101, 51))
        self.lineEdit.setGeometry(QtCore.QRect(210, 100, 201, 31))

        self.newplace = QLineEdit(self)
        self.newplace.setGeometry(QtCore.QRect(210, 150, 201, 31))

        self.newlabel = QLabel('Новое место', self)
        self.newlabel.setGeometry(QtCore.QRect(70, 140, 111, 51))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.newlabel.setFont(font)

        self.pushButton.clicked.connect(self.oke)
        self.pushButton_2.clicked.connect(self.ex)
        self.lineEdit.textChanged.connect(self.textChang)
        self.tableWidget.cellClicked.connect(self.tabletsignal)

    def textChang(self):
        text = self.lineEdit.text().lower()
        lis = DATABASE.giveItemFromChange(text, 'del')
        self.tb.makeTable(lis, '-', text)

    def tabletsignal(self, x, y):
        text = self.tableWidget.item(x, y).text().lower()
        self.lineEdit.setText(DATABASE.giveItemFromChange(text, 'del')[0][0])

    def oke(self):
        try:
            name = self.lineEdit.text()
            place = self.newplace.text()
            DATABASE.cgangeElementFromPerem(name, place)
        except:
            pass
        finally:
            self.sig.emit()
            self.close()

    def ex(self):
        self.close()


class Mainw(QMainWindow, Ui_MainWindow):  # основное окно приложения
    def __init__(self, size=QtCore.QRect(200, 200, 1132, 919)):
        super().__init__()
        self.lis_place = self.giveplace()
        self.lis = []
        self.lis_buttonchics = []
        self.setupUi(self)

        self.pushButton = QPushButton('Список', self)
        self.pushButton.clicked.connect(self.goInto)

        self.make_place()
        self.setGeometry(size)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(
            QPixmap(random.choice(PICTURES))))
        self.setPalette(palette)
        style = '''
                    .QPushButton {
                    background-color: 
                    rgba(255, 219, 162, 0.5);
                    border-radius: 30px;
                    border: 3px solid black;
                    }

                    QPushButton:hover{
                    border: none;
                    opacity: 1;
                    color: rgb(44, 55, 59);
                    }

                    QLineEdit {

                    }
                    '''
        self.setStyleSheet(style)

        self.action.triggered.connect(self.toolHouse1)
        self.action_2.triggered.connect(self.toolHouse2)
        self.action_6.triggered.connect(self.toolHouse2)
        self.action_4.triggered.connect(self.listInWolk)
        self.action_3.triggered.connect(self.perem)
        self.action_7.triggered.connect(self.filetxt)

    def make_place(self):  # динамическая расстановка кнопок мест
        lkhelplis = self.lis_place
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        if len(lkhelplis) >= 12:
            lkhelplis = lkhelplis[:11]
        for i in range(len(lkhelplis)):
            pbtm = QPushButton(lkhelplis[i], self)
            pbtm.clicked.connect(self.goInto)
            self.lis_buttonchics.append(pbtm)
            if i < 3:
                self.gridLayout.addWidget(pbtm, 0, i + 1)
            elif 3 <= i <= 6:
                self.gridLayout.addWidget(pbtm, 1, (i + 1) % 4)
            elif 7 <= i <= 11:
                self.gridLayout.addWidget(pbtm, 2, (i + 1) % 4)
        self.gridLayout.addWidget(self.pushButton, 0, 0)

    def perem(self):
        self.act = ActionPerem()
        self.act.show()
        self.act.sig.connect(self.actionclose)

    def listInWolk(self):  # !!!!!!!!!!!!!!!!!!!!!!сигнал выхода
        self.act3 = ActionList()
        self.act3.show()
        self.act3.sig.connect(self.actionclose)

    def toolHouse1(self):
        self.act = Action()
        self.act.show()
        self.act.sig.connect(self.actionclose)

    def toolHouse2(self):
        text = self.sender().text()
        self.act2 = Action2(text)
        self.act2.show()
        self.act2.sig.connect(self.actionclose)

    def resizeEvent(self, event):  # динамическое изменение размеров кнопок и текста
        width = self.size().width()
        height = self.size().height()
        if len(self.lis_place) <= 3:
            k = 0.5
        elif 7 < len(self.lis_place):
            k = 0.09
        else:
            k = 0.2
        self.pushButton.setStyleSheet(f'height: {height * k} px; font-size: {int(width * 0.03)}px')
        for el in self.lis_buttonchics:
            el.setStyleSheet(f'height: {height * k} px; font-size: {int(width * 0.03)}px')
        self.gridLayout.setSpacing(int(width * 0.1) + 60)

    def goInto(self):  # открытие нового окна
        size = self.geometry()

        text = self.sender().text()
        self.garage = Garage(size, text)

        self.garage.show()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == event.key() == Qt.Key_Return:
            if self.poisk.text() != '':
                self.search()

    def giveplace(self):
        return list(set(map(lambda x: x[0], DATABASE.giveAllPlace())))

    def actionclose(self):
        self.lis_place = self.giveplace()
        self.make_place()
        self.resizeEvent(1)

    def filetxt(self):
        file = QFileDialog.getOpenFileName(
            self, 'Выбрать файл с текстом', '', 'Файл (*.txt);;Все файлы (*)')[0]
        lis = open(file, 'r', encoding='utf8').readlines()
        filefca = open('thingsWithoutPlace.txt', 'w')
        for el in lis:
            item = el.strip()
            try:
                DATABASE.listWithLisinFalse(item, 'yes')
            except Exception:
                filefca.write(item)
        filefca.close()
        self.actionclose()
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Information")
        msgbox.setText(f'Все вещи перемещены.\nВещи, которых нет в базе данных, записанны в файл thingsWithoutPlace')


def excepthook(exc_type, exc_value, exc_tb):
    enriched_tb = _add_missing_frames(exc_tb) if exc_tb else exc_tb
    # Note: sys.__excepthook__(...) would not work here.
    # We need to use print_exception(...):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Information")
    msgbox.setText(f'Error')
    # print(exc_type, exc_value, enriched_tb)


DATABASE = BD()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainw()
    ex.show()
    sys.excepthook = excepthook
    sys.exit(app.exec_())
