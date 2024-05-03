# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_StudentsDialog(object):
    def setupUi(self, StudentsDialog):
        if not StudentsDialog.objectName():
            StudentsDialog.setObjectName(u"StudentsDialog")
        StudentsDialog.resize(521, 628)
        StudentsDialog.setMinimumSize(QSize(81, 51))
        StudentsDialog.setMaximumSize(QSize(521, 16777215))
        font = QFont()
        font.setPointSize(12)
        StudentsDialog.setFont(font)
        StudentsDialog.setStyleSheet(u"QDialog{\n"
"\n"
"    background-color:white;\n"
"}\n"
"QLineEdit{ \n"
"        \n"
"     border: 1px solid gray;\n"
"    border-radius:6px;\n"
"    padding-left:15px;\n"
"    height:35px;\n"
"}\n"
"\n"
"\n"
"QDateEdit{ \n"
"\n"
"    border: 1px solid gray;\n"
"    border-radius:6px;\n"
"    padding-left:15px;\n"
"    height:31px;\n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"     \n"
"     border: 2px solid white;\n"
"    border-radius: 8px;\n"
"    pandding :1px 18px 1px 3px;\n"
"    background-color:black;\n"
"     color: white;\n"
" height: 30px;\n"
" padding-left:15px;\n"
"font weight: bold ;\n"
"selection-background-color : #2980B9;\n"
"}")
        self.line = QFrame(StudentsDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 70, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(StudentsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 301, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.lineEdit = QLineEdit(StudentsDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 120, 0, 31))
        self.layoutWidget = QWidget(StudentsDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 501, 441))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit_2 = QLineEdit(self.layoutWidget)
        self.name_lineEdit_2.setObjectName(u"name_lineEdit_2")
        self.name_lineEdit_2.setMinimumSize(QSize(0, 31))
        self.name_lineEdit_2.setMaximumSize(QSize(521, 16777215))

        self.verticalLayout.addWidget(self.name_lineEdit_2)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setFont(font)

        self.verticalLayout_7.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox_2 = QComboBox(self.layoutWidget)
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.setObjectName(u"class_comboBox_2")

        self.verticalLayout_6.addWidget(self.class_comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.label_8)

        self.date_dateEdit = QDateEdit(self.layoutWidget)
        self.date_dateEdit.setObjectName(u"date_dateEdit")

        self.verticalLayout_5.addWidget(self.date_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.adrs_lineEdit_3 = QLineEdit(self.layoutWidget)
        self.adrs_lineEdit_3.setObjectName(u"adrs_lineEdit_3")
        self.adrs_lineEdit_3.setMinimumSize(QSize(0, 31))
        self.adrs_lineEdit_3.setMaximumSize(QSize(521, 16777215))

        self.verticalLayout_2.addWidget(self.adrs_lineEdit_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 31))
        self.lineEdit_4.setMaximumSize(QSize(521, 16777215))

        self.verticalLayout_3.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.email_lineEdit_5 = QLineEdit(self.layoutWidget)
        self.email_lineEdit_5.setObjectName(u"email_lineEdit_5")
        self.email_lineEdit_5.setMinimumSize(QSize(0, 31))
        self.email_lineEdit_5.setMaximumSize(QSize(521, 16777215))

        self.verticalLayout_4.addWidget(self.email_lineEdit_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(StudentsDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 550, 201, 53))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.savestudents_btn = QPushButton(self.layoutWidget1)
        self.savestudents_btn.setObjectName(u"savestudents_btn")
        self.savestudents_btn.setMinimumSize(QSize(101, 51))
        self.savestudents_btn.setStyleSheet(u"QPushButton{ \n"
"       background-color:#34D841;\n"
"       color: white;\n"
"       border : none;\n"
"      border-radius: 8px;\n"
"       font-weight:bold;\n"
"      font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.savestudents_btn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(81, 51))
        self.cancel_btn.setStyleSheet(u"QPushButton{ \n"
"	font: 12pt \"Segoe UI\";\n"
"       background-color:#585858;\n"
"       color: white;\n"
"       border : none;\n"
"      border-radius: 8px;\n"
"       font-weight:bold;\n"
"      font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi(StudentsDialog)

        QMetaObject.connectSlotsByName(StudentsDialog)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Select Gender ", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Select Class ", None))
        self.class_comboBox_2.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade1", None))
        self.class_comboBox_2.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade2", None))
        self.class_comboBox_2.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade3", None))
        self.class_comboBox_2.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade4", None))
        self.class_comboBox_2.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade5", None))
        self.class_comboBox_2.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade6", None))
        self.class_comboBox_2.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade7", None))
        self.class_comboBox_2.setItemText(7, QCoreApplication.translate("StudentsDialog", u"Grade8", None))
        self.class_comboBox_2.setItemText(8, QCoreApplication.translate("StudentsDialog", u"Grade9", None))
        self.class_comboBox_2.setItemText(9, QCoreApplication.translate("StudentsDialog", u"Grade10", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date of Birth ", None))
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Address:", None))
        self.label_4.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number:", None))
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Email : ", None))
        self.savestudents_btn.setText(QCoreApplication.translate("StudentsDialog", u" Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel ", None))
    # retranslateUi

