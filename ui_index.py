# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 886)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        MainWindow.setContextMenuPolicy(Qt.PreventContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(-10, 0, 1150, 915))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_only_widget = QWidget(self.layoutWidget1)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(61, 0))
        self.icon_only_widget.setMaximumSize(QSize(61, 911))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"\n"
"	background-color: rgb(13, 13, 13);\n"
"}")
        self.layoutWidget2 = QWidget(self.icon_only_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 54, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/icons/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.layoutWidget3 = QWidget(self.icon_only_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 70, 35, 221))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 35, 0, 0)
        self.dashboard_1 = QPushButton(self.layoutWidget3)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/icons/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(21, 21))
        self.dashboard_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.dashboard_1)

        self.institutuion_1 = QPushButton(self.layoutWidget3)
        self.institutuion_1.setObjectName(u"institutuion_1")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/institutionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/newPrefix/icons/institutionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.institutuion_1.setIcon(icon1)
        self.institutuion_1.setIconSize(QSize(21, 21))
        self.institutuion_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.institutuion_1)

        self.students_1 = QPushButton(self.layoutWidget3)
        self.students_1.setObjectName(u"students_1")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/studentssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/newPrefix/icons/studentssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_1.setIcon(icon2)
        self.students_1.setIconSize(QSize(21, 21))
        self.students_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.students_1)

        self.teacher_1 = QPushButton(self.layoutWidget3)
        self.teacher_1.setObjectName(u"teacher_1")
        self.teacher_1.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/teacherssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/newPrefix/icons/financessmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.teacher_1.setIcon(icon3)
        self.teacher_1.setIconSize(QSize(21, 21))
        self.teacher_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.teacher_1)

        self.layoutWidget4 = QWidget(self.icon_only_widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 803, 35, 71))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.settings_1 = QPushButton(self.layoutWidget4)
        self.settings_1.setObjectName(u"settings_1")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/settingssmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/newPrefix/icons/settingssmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon4)
        self.settings_1.setIconSize(QSize(21, 21))
        self.settings_1.setCheckable(True)

        self.verticalLayout_4.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.layoutWidget4)
        self.signout_1.setObjectName(u"signout_1")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/signoutsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/newPrefix/icons/signoutsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_1.setIcon(icon5)
        self.signout_1.setIconSize(QSize(21, 21))
        self.signout_1.setCheckable(True)

        self.verticalLayout_4.addWidget(self.signout_1)


        self.horizontalLayout_5.addWidget(self.icon_only_widget)

        self.icon_text_widget = QWidget(self.layoutWidget1)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(171, 911))
        self.icon_text_widget.setMaximumSize(QSize(171, 911))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"\n"
"	background-color: rgb(13, 13, 13);\n"
"  color:white;\n"
"}\n"
"\n"
"QPushBottons{\n"
"      height:30px;\n"
"      broder:none;\n"
"}")
        self.layoutWidget5 = QWidget(self.icon_text_widget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 10, 131, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.layoutWidget5)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border-color: rgb(0, 170, 0);\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label_4)

        self.layoutWidget_2 = QWidget(self.icon_text_widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 800, 141, 81))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.settings_2 = QPushButton(self.layoutWidget_2)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButtons{\n"
"\n"
"     padding-left:-60px\n"
"}\n"
"QPushButtons: checked{\n"
"   background-color:white;\n"
"  border-radius:3px;\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/newPrefix/icons/settings1.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon6)
        self.settings_2.setIconSize(QSize(50, 50))
        self.settings_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.layoutWidget_2)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButtons{\n"
"\n"
"     padding-left:-60px\n"
"}\n"
"QPushButtons: checked{\n"
"   background-color:white;\n"
"  border-radius:3px;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/signout2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/newPrefix/icons/signout1.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_2.setIcon(icon7)
        self.signout_2.setIconSize(QSize(70, 70))
        self.signout_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.signout_2)

        self.layoutWidget6 = QWidget(self.icon_text_widget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 70, 161, 411))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 35, 0, 0)
        self.dashboard_2 = QPushButton(self.layoutWidget6)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setEnabled(True)
        self.dashboard_2.setStyleSheet(u"QPushButtons{\n"
"     padding-left: -100px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/newPrefix/icons/dashboard1.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon8)
        self.dashboard_2.setIconSize(QSize(70, 20))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.institutuion_2 = QPushButton(self.layoutWidget6)
        self.institutuion_2.setObjectName(u"institutuion_2")
        self.institutuion_2.setStyleSheet(u"QPushButtons{\n"
"     padding-left:-110px;\n"
"}\n"
"QPushButtons: checked{\n"
"   background-color:white;\n"
"  border-radius:3px;\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/institution2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/newPrefix/icons/institution1.png", QSize(), QIcon.Normal, QIcon.On)
        self.institutuion_2.setIcon(icon9)
        self.institutuion_2.setIconSize(QSize(90, 19))
        self.institutuion_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.institutuion_2)

        self.students = QFrame(self.layoutWidget6)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setGeometry(QRect(10, 30, 131, 71))
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.studnets_info = QPushButton(self.students_dropdown)
        self.studnets_info.setObjectName(u"studnets_info")
        self.studnets_info.setGeometry(QRect(20, 0, 101, 24))
        self.studnets_info.setStyleSheet(u"QPushButtons{\n"
"     padding-left: 20px\n"
"}\n"
"QPushButtons : hover{\n"
"     color:#12B298\n"
"}\n"
"")
        self.studnets_info.setCheckable(True)
        self.students_pay = QPushButton(self.students_dropdown)
        self.students_pay.setObjectName(u"students_pay")
        self.students_pay.setGeometry(QRect(20, 30, 101, 24))
        self.students_pay.setCheckable(True)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setGeometry(QRect(0, 0, 149, 28))
        self.students_2.setStyleSheet(u"QPushButtons{\n"
"\n"
"     padding-left:-60px\n"
"}\n"
"QPushButtons: checked{\n"
"   background-color:white;\n"
"  border-radius:3px;\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/students3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/newPrefix/icons/students4.png", QSize(), QIcon.Normal, QIcon.On)
        self.students_2.setIcon(icon10)
        self.students_2.setIconSize(QSize(110, 20))
        self.students_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.students)

        self.teachers = QFrame(self.layoutWidget6)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.teacher_2 = QPushButton(self.teachers)
        self.teacher_2.setObjectName(u"teacher_2")
        self.teacher_2.setGeometry(QRect(10, 0, 145, 28))
        self.teacher_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.teacher_2.setStyleSheet(u"QPushButtons{\n"
"\n"
"     padding-left:-60px\n"
"}\n"
"QPushButtons: checked{\n"
"   background-color:white;\n"
"  border-radius:3px;\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/teachers3.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/newPrefix/icons/teachers4.png", QSize(), QIcon.Normal, QIcon.On)
        self.teacher_2.setIcon(icon11)
        self.teacher_2.setIconSize(QSize(110, 20))
        self.teacher_2.setCheckable(True)
        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setGeometry(QRect(10, 40, 141, 51))
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.teacher_pay = QPushButton(self.teachers_dropdown)
        self.teacher_pay.setObjectName(u"teacher_pay")
        self.teacher_pay.setGeometry(QRect(20, 30, 111, 24))
        self.teacher_pay.setCheckable(True)
        self.teacher_infos = QPushButton(self.teachers_dropdown)
        self.teacher_infos.setObjectName(u"teacher_infos")
        self.teacher_infos.setGeometry(QRect(20, 0, 111, 24))
        self.teacher_infos.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teachers)


        self.horizontalLayout_5.addWidget(self.icon_text_widget)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.header_widget = QWidget(self.layoutWidget1)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMaximumSize(QSize(841, 60))
        self.layoutWidget7 = QWidget(self.header_widget)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(470, 10, 291, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"          pandding-left:20px;\n"
"          border: 1px solid gray;\n"
"          border-radius:10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.layoutWidget7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/newPrefix/icons/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.layoutWidget8 = QWidget(self.header_widget)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(0, 0, 201, 59))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.layoutWidget8)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label)

        self.label_3 = QLabel(self.layoutWidget8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777209, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"\n"
"color: rgb(90, 90, 90);")

        self.verticalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget1)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setMaximumSize(QSize(900, 800))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.main_screen_widget.setFont(font3)
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 841, 851))
        self.stackedWidget.setMinimumSize(QSize(841, 0))
        self.stackedWidget.setMaximumSize(QSize(841, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 110, 171, 131))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(25)
        font4.setBold(True)
        self.label_7.setFont(font4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 130, 171, 131))
        self.label_8.setFont(font4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 72, 351, 53))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.savestudents_btn = QPushButton(self.widget)
        self.savestudents_btn.setObjectName(u"savestudents_btn")
        self.savestudents_btn.setMinimumSize(QSize(101, 51))
        self.savestudents_btn.setStyleSheet(u"QPushButton{ \n"
"	background-color: rgb(0, 0, 0);\n"
"      \n"
"       color: white;\n"
"       border : none;\n"
"      border-radius: 12px;\n"
"       font-weight:bold;\n"
"      font-size:10px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/icons/add student.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savestudents_btn.setIcon(icon13)

        self.horizontalLayout_7.addWidget(self.savestudents_btn)

        self.savestudents_btn_2 = QPushButton(self.widget)
        self.savestudents_btn_2.setObjectName(u"savestudents_btn_2")
        self.savestudents_btn_2.setMinimumSize(QSize(101, 51))
        self.savestudents_btn_2.setStyleSheet(u"QPushButton{ \n"
"       background-color:#34D841;\n"
"       color: white;\n"
"       border : none;\n"
"      border-radius: 12px;\n"
"       font-weight:bold;\n"
"      font-size:10px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/icons/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savestudents_btn_2.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.savestudents_btn_2)

        self.savestudents_btn_3 = QPushButton(self.widget)
        self.savestudents_btn_3.setObjectName(u"savestudents_btn_3")
        self.savestudents_btn_3.setMinimumSize(QSize(101, 51))
        self.savestudents_btn_3.setStyleSheet(u"QPushButton{ \n"
"       \n"
"	    background-color: rgb(255, 1, 48);\n"
"       color: white;\n"
"       border : none;\n"
"      border-radius: 12px;\n"
"       font-weight:bold;\n"
"      font-size:10px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/icons/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savestudents_btn_3.setIcon(icon15)

        self.horizontalLayout_7.addWidget(self.savestudents_btn_3)

        self.tableWidget = QTableWidget(self.page_3)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 180, 800, 501))
        self.tableWidget.setMinimumSize(QSize(800, 0))
        self.tableWidget.setMaximumSize(QSize(400, 16777215))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"QTableWidget{\n"
"     alternate-background-color:#B0EDFB;\n"
"    background-color:#F4F9FA\n"
"\n"
"}\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 338, 56))
        self.verticalLayout_8 = QVBoxLayout(self.widget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(18)
        font5.setBold(False)
        self.label_9.setFont(font5)

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setFamilies([u"SimSun"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.label_14.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_14)

        self.widget2 = QWidget(self.page_3)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 130, 461, 33))
        self.horizontalLayout_8 = QHBoxLayout(self.widget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gender_comboBox = QComboBox(self.widget2)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setMinimumSize(QSize(101, 31))
        self.gender_comboBox.setMaximumSize(QSize(93, 31))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(9)
        font7.setBold(False)
        self.gender_comboBox.setFont(font7)
        self.gender_comboBox.setStyleSheet(u"QComboBox{\n"
"     \n"
"     border: 2px solid white;\n"
"    border-radius: 8px;\n"
"    pandding :1px 18px 1px 3px;\n"
"    background-color:black;\n"
"     color: white;\n"
" height: 30px;\n"
" padding-left:12px;\n"
"font weight: bold ;\n"
"selection-background-color : #2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.gender_comboBox)

        self.class_comboBox_2 = QComboBox(self.widget2)
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
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.setObjectName(u"class_comboBox_2")
        self.class_comboBox_2.setMinimumSize(QSize(101, 31))
        self.class_comboBox_2.setMaximumSize(QSize(101, 31))
        self.class_comboBox_2.setStyleSheet(u"QComboBox{\n"
"     \n"
"     border: 2px solid white;\n"
"    border-radius: 8px;\n"
"    pandding :1px 18px 1px 3px;\n"
"    background-color:black;\n"
"     color: white;\n"
" height: 30px;\n"
" padding-left:12px;\n"
"font weight: bold ;\n"
"selection-background-color : #2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.class_comboBox_2)

        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(241, 31))
        self.lineEdit_2.setMaximumSize(QSize(241, 31))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setItalic(False)
        self.lineEdit_2.setFont(font8)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"          pandding-left:20px;\n"
"          border: 1px solid gray;\n"
"          border-radius:10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 170, 271, 131))
        self.label_10.setFont(font4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 230, 201, 131))
        self.label_11.setFont(font4)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 190, 281, 131))
        self.label_12.setFont(font4)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, 290, 131, 131))
        self.label_13.setFont(font4)
        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_7.addWidget(self.main_screen_widget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.signout_1.toggled.connect(MainWindow.close)
        self.teacher_2.toggled.connect(self.teacher_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(MainWindow.close)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.close)
        self.teacher_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.institutuion_2.toggled.connect(self.institutuion_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.dashboard_1.setText("")
        self.institutuion_1.setText("")
        self.students_1.setText("")
        self.teacher_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Schol", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.dashboard_2.setText("")
        self.institutuion_2.setText("")
        self.studnets_info.setText(QCoreApplication.translate("MainWindow", u"Student Infos", None))
        self.students_pay.setText(QCoreApplication.translate("MainWindow", u"Student Payement", None))
        self.students_2.setText("")
        self.teacher_2.setText("")
        self.teacher_pay.setText(QCoreApplication.translate("MainWindow", u"Teacher Payement", None))
        self.teacher_infos.setText(QCoreApplication.translate("MainWindow", u"Teacher Infos", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Search Here..", None))
        self.label_6.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Fadoua", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.savestudents_btn.setText(QCoreApplication.translate("MainWindow", u" Add Student", None))
        self.savestudents_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.savestudents_btn_3.setText(QCoreApplication.translate("MainWindow", u"Export to Pdf", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Profile", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Infos", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" Welcome to the students informations page", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select gender", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.class_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.class_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade1", None))
        self.class_comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade2", None))
        self.class_comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade3", None))
        self.class_comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade4", None))
        self.class_comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade5", None))
        self.class_comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade6", None))
        self.class_comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade7", None))
        self.class_comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade8", None))
        self.class_comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade9", None))
        self.class_comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade10", None))

        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Search Student...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payement", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Teacher Infos", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Payement", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

