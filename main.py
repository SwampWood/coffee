import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add_grade = QtWidgets.QPushButton(self.tab)
        self.button_add_grade.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_grade.sizePolicy().hasHeightForWidth())
        self.button_add_grade.setSizePolicy(sizePolicy)
        self.button_add_grade.setObjectName("button_add_grade")
        self.horizontalLayout.addWidget(self.button_add_grade)
        self.button_change_grade = QtWidgets.QPushButton(self.tab)
        self.button_change_grade.setObjectName("button_change_grade")
        self.horizontalLayout.addWidget(self.button_change_grade)
        self.button_delete_grade = QtWidgets.QPushButton(self.tab)
        self.button_delete_grade.setObjectName("button_delete_grade")
        self.horizontalLayout.addWidget(self.button_delete_grade)
        self.button_student_record = QtWidgets.QPushButton(self.tab)
        self.button_student_record.setObjectName("button_student_record")
        self.horizontalLayout.addWidget(self.button_student_record)
        self.button_class_record = QtWidgets.QPushButton(self.tab)
        self.button_class_record.setObjectName("button_class_record")
        self.horizontalLayout.addWidget(self.button_class_record)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_grades = QtWidgets.QTableWidget(self.tab)
        self.table_grades.setObjectName("table_grades")
        self.table_grades.setColumnCount(0)
        self.table_grades.setRowCount(0)
        self.verticalLayout.addWidget(self.table_grades)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 183, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_add_student = QtWidgets.QPushButton(self.tab_2)
        self.button_add_student.setObjectName("button_add_student")
        self.horizontalLayout_2.addWidget(self.button_add_student)
        self.button_change_student = QtWidgets.QPushButton(self.tab_2)
        self.button_change_student.setObjectName("button_change_student")
        self.horizontalLayout_2.addWidget(self.button_change_student)
        self.button_delete_student = QtWidgets.QPushButton(self.tab_2)
        self.button_delete_student.setObjectName("button_delete_student")
        self.horizontalLayout_2.addWidget(self.button_delete_student)
        self.button_find_students = QtWidgets.QPushButton(self.tab_2)
        self.button_find_students.setObjectName("button_find_students")
        self.horizontalLayout_2.addWidget(self.button_find_students)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.table_students = QtWidgets.QTableWidget(self.tab_2)
        self.table_students.setObjectName("table_students")
        self.table_students.setColumnCount(0)
        self.table_students.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table_students)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 366, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add_class = QtWidgets.QPushButton(self.tab_3)
        self.button_add_class.setObjectName("button_add_class")
        self.horizontalLayout_3.addWidget(self.button_add_class)
        self.button_change_class = QtWidgets.QPushButton(self.tab_3)
        self.button_change_class.setObjectName("button_change_class")
        self.horizontalLayout_3.addWidget(self.button_change_class)
        self.button_delete_class = QtWidgets.QPushButton(self.tab_3)
        self.button_delete_class.setObjectName("button_delete_class")
        self.horizontalLayout_3.addWidget(self.button_delete_class)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.table_classes = QtWidgets.QTableWidget(self.tab_3)
        self.table_classes.setObjectName("table_classes")
        self.table_classes.setColumnCount(0)
        self.table_classes.setRowCount(0)
        self.verticalLayout_4.addWidget(self.table_classes)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 366, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_add_subject = QtWidgets.QPushButton(self.tab_4)
        self.button_add_subject.setObjectName("button_add_subject")
        self.horizontalLayout_4.addWidget(self.button_add_subject)
        self.button_change_subject = QtWidgets.QPushButton(self.tab_4)
        self.button_change_subject.setObjectName("button_change_subject")
        self.horizontalLayout_4.addWidget(self.button_change_subject)
        self.button_delete_subject = QtWidgets.QPushButton(self.tab_4)
        self.button_delete_subject.setObjectName("button_delete_subject")
        self.horizontalLayout_4.addWidget(self.button_delete_subject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.table_subjects = QtWidgets.QTableWidget(self.tab_4)
        self.table_subjects.setObjectName("table_subjects")
        self.table_subjects.setColumnCount(0)
        self.table_subjects.setRowCount(0)
        self.verticalLayout_3.addWidget(self.table_subjects)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дневник"))
        self.button_add_grade.setText(_translate("MainWindow", "Добавить оценку"))
        self.button_change_grade.setText(_translate("MainWindow", "Изменить"))
        self.button_delete_grade.setText(_translate("MainWindow", "Удалить оценку"))
        self.button_student_record.setText(_translate("MainWindow", "Успеваемость ученика"))
        self.button_class_record.setText(_translate("MainWindow", "Успеваемость класса"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Оценки"))
        self.button_add_student.setText(_translate("MainWindow", "Добавить ученика"))
        self.button_change_student.setText(_translate("MainWindow", "Изменить"))
        self.button_delete_student.setText(_translate("MainWindow", "Удалить ученика"))
        self.button_find_students.setText(_translate("MainWindow", "Найти учеников"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ученики"))
        self.button_add_class.setText(_translate("MainWindow", "Добавить класс"))
        self.button_change_class.setText(_translate("MainWindow", "Изменить"))
        self.button_delete_class.setText(_translate("MainWindow", "Удалить класс"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Классы"))
        self.button_add_subject.setText(_translate("MainWindow", "Добавить предмет"))
        self.button_change_subject.setText(_translate("MainWindow", "Изменить"))
        self.button_delete_subject.setText(_translate("MainWindow", "Удалить предмет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Предметы"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 192)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, -1, -1, -1)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setHorizontalSpacing(23)
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setMaximum(11)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(42)
        self.formLayout_3.setVerticalSpacing(3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить предмет"))
        self.label.setText(_translate("Form", "Класс:"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label_3.setText(_translate("Form", "Класс"))
        self.label_4.setText(_translate("Form", "Буква класса"))
        self.label_5.setText(_translate("Form", "Школа"))
        self.label_6.setText(_translate("Form", "Предмет:"))
        self.label_7.setText(_translate("Form", "Название"))
        self.label_8.setText(_translate("Form", "Система"))


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
        self.con = sqlite3.connect("data/coffee.db")
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