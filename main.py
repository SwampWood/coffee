import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class AddSubject(QWidget):
    def __init__(self, cursor, mainwindow):
        super().__init__()
        uic.loadUi("add_subject.ui", self)
        self.cursor = cursor
        self.mainwindow = mainwindow
        self.buttonBox.accepted.connect(self.accept2)
        self.buttonBox.rejected.connect(self.close)

        self.spinBox.valueChanged.connect(self.autofill)

        self.spinBox_2.valueChanged.connect(self.find_id)
        self.lineEdit.textEdited.connect(self.find_id)
        self.lineEdit_2.textEdited.connect(self.find_id)

    def autofill(self):
        try:
            if not self.spinBox.value():
                raise IndexError
            class_ = self.cursor.execute(f"""SELECT class, parallel, school from classes
            WHERE id = {self.spinBox.value()}""").fetchall()[0]
            self.spinBox_2.blockSignals(True)
            self.lineEdit.blockSignals(True)
            self.lineEdit_2.blockSignals(True)
            self.spinBox_2.setValue(class_[0])
            self.lineEdit.setText(class_[1])
            self.lineEdit_2.setText(str(class_[2]))
            self.spinBox_2.blockSignals(False)
            self.lineEdit.blockSignals(False)
            self.lineEdit_2.blockSignals(False)

        except IndexError:
            self.spinBox_2.setValue(0)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')

    def find_id(self):
        if self.spinBox_2.value() and self.lineEdit.text() and self.lineEdit_2.text():
            try:
                id_ = self.cursor.execute(f"""SELECT id from classes
                WHERE class = {self.spinBox_2.value()} AND parallel = '{self.lineEdit.text()}' AND
                school = '{self.lineEdit_2.text()}'""").fetchall()[0][0]
                self.spinBox.blockSignals(True)
                self.spinBox.setValue(id_)
                self.spinBox.blockSignals(False)
            except IndexError:
                pass

    def getInputs(self):
        tup = tuple()
        self.inputs = [self.spinBox, self.lineEdit_3, self.lineEdit_4]
        for i in range(len(self.inputs)):
            if i == 0:
                tup = tup + (self.inputs[i].value(),)
            else:
                tup = tup + (self.inputs[i].text(),)
        return tup

    def accept2(self):
        res = self.getInputs()
        message = QMessageBox()
        message.setWindowTitle('Ошибка')
        try:
            if not all(res):
                raise IndexError
            id_class_exists = self.cursor.execute(f"""SELECT id FROM classes
            WHERE id = {res[0]}""").fetchall()
            if not id_class_exists:
                message.setText('Класса с таким id не существует')
                message.exec()
            elif res[2] not in ['5', '10', '100', 'рейтинговая']:
                message.setText(f'''Недопустимое значение пункта "Система": {res[2]}.
Допустимые значения: 5, 10, 100, рейтинговая''')
                message.exec()
            else:
                self.cursor.execute("""INSERT INTO subjects(subject, class, system)
                        VALUES (?, ?, ?)""", (res[1], res[0], res[2]))
                self.mainwindow.con.commit()
                self.mainwindow.update_table_subjects()
                self.close()
        except IndexError:
            message.setText('Не все данные введены')
            message.exec()


class EditSubject(AddSubject):
    def __init__(self, subject_id, cursor, mainwindow):
        super().__init__(cursor, mainwindow)
        self.setWindowTitle('Изменить предмет')
        self.subject_id = subject_id

        info = self.cursor.execute("""SELECT * FROM subjects
                WHERE id = ?""", (subject_id,)).fetchall()[0]
        self.spinBox.setValue(info[2])
        self.lineEdit_3.setText(info[1])
        self.lineEdit_4.setText(str(info[3]))

    def accept2(self):
        res = self.getInputs()
        message = QMessageBox()
        message.setWindowTitle('Ошибка')
        try:
            if not all(res):
                raise IndexError
            id_class_exists = self.cursor.execute(f"""SELECT id FROM classes
            WHERE id = {res[0]}""").fetchall()
            if not id_class_exists:
                message.setText('Класса с таким id не существует')
                message.exec()
            elif res[2] not in ['5', '10', '100', 'рейтинговая']:
                message.setText(f'''Недопустимое значение пункта "Система": {res[2]}.
Допустимые значения: 5, 10, 100, рейтинговая''')
                message.exec()
            else:
                self.cursor.execute("""UPDATE subjects
                SET subject = ?, class = ?, system = ?
                WHERE id = ?""", (res[1], res[0], res[2], self.subject_id))
                self.mainwindow.con.commit()
                self.mainwindow.update_table_subjects()
                self.close()
        except IndexError:
            message.setText('Не все данные введены')
            message.exec()


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.filters = []
        self.update_table_subjects()
        self.button_add_subject.clicked.connect(self.add_subjects)
        self.button_change_subject.clicked.connect(self.edit_subjects)
        self.button_delete_subject.clicked.connect(self.delete_subjects)

    def update_table_subjects(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT subjects.id as ИД, subjects.subject as Предмет, classes.class as Класс,
        classes.parallel as 'Буква класса', subjects.system as Система
        FROM subjects INNER JOIN classes ON subjects.class = classes.id""").fetchall()
        self.table_subjects.setRowCount(len(result))
        self.table_subjects.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.table_subjects.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table_subjects.setItem(i, j, QTableWidgetItem(str(val)))

    def add_subjects(self):
        self.widget_add_subjects = AddSubject(self.con, self)
        self.widget_add_subjects.show()

    def edit_subjects(self):
        row = self.table_subjects.currentRow()
        if row < 0:
            message = QMessageBox()
            message.setWindowTitle('Ошибка')
            message.setText('Выделите строку для изменения')
            message.exec()
            pass
        else:
            table_item = self.table_subjects.item(row, 0).text()
            self.widget_edit_subjects = EditSubject(table_item, self.con, self)
            self.widget_edit_subjects.show()

    def delete_subjects(self):
        rows = list(set([i.row() for i in self.table_subjects.selectedItems()]))
        ids = [self.table_subjects.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, 'Подтверждение', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE FROM subjects WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()
        self.update_table_subjects()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = Coffee()
    exe.show()
    sys.exit(app.exec())