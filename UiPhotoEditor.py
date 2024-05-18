# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PhotoEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_rs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #2E2E2E;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.imageWidget = QLabel(self.centralwidget)
        self.imageWidget.setObjectName(u"imageWidget")
        self.imageWidget.setGeometry(QRect(0, 0, 600, 600))
        self.imageWidget.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #3C3C3C;")
        self.imageWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.openFileButton = QPushButton(self.centralwidget)
        self.openFileButton.setObjectName(u"openFileButton")
        self.openFileButton.setGeometry(QRect(625, 60, 150, 40))
        font = QFont()
        font.setPointSize(10)
        self.openFileButton.setFont(font)
        self.openFileButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #3C3C3C;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3C3C3C;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/recources/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileButton.setIcon(icon)
        self.applyFilterButton = QPushButton(self.centralwidget)
        self.applyFilterButton.setObjectName(u"applyFilterButton")
        self.applyFilterButton.setGeometry(QRect(625, 260, 150, 40))
        self.applyFilterButton.setFont(font)
        self.applyFilterButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #3C3C3C;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3C3C3C;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/recources/icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.applyFilterButton.setIcon(icon1)
        self.filterHeader = QLabel(self.centralwidget)
        self.filterHeader.setObjectName(u"filterHeader")
        self.filterHeader.setGeometry(QRect(625, 160, 150, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.filterHeader.setFont(font1)
        self.filterHeader.setStyleSheet(u"background-color: none;")
        self.filterHeader.setScaledContents(False)
        self.filterHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(625, 210, 150, 40))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: #3C3C3C;\n"
"color: #FFFFFF;\n"
"border: 1px solid #5A5A5A;\n"
"padding-left: 5px;")
        self.saveFileButton = QPushButton(self.centralwidget)
        self.saveFileButton.setObjectName(u"saveFileButton")
        self.saveFileButton.setGeometry(QRect(625, 110, 150, 40))
        self.saveFileButton.setFont(font)
        self.saveFileButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #1E88E5;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #1E88E5;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/recources/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveFileButton.setIcon(icon2)
        self.fileHeader = QLabel(self.centralwidget)
        self.fileHeader.setObjectName(u"fileHeader")
        self.fileHeader.setGeometry(QRect(625, 10, 150, 40))
        self.fileHeader.setFont(font1)
        self.fileHeader.setStyleSheet(u"background-color: none;")
        self.fileHeader.setScaledContents(False)
        self.fileHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.optionsHeader = QLabel(self.centralwidget)
        self.optionsHeader.setObjectName(u"optionsHeader")
        self.optionsHeader.setGeometry(QRect(625, 310, 150, 40))
        self.optionsHeader.setFont(font1)
        self.optionsHeader.setStyleSheet(u"background-color: none;")
        self.optionsHeader.setScaledContents(False)
        self.optionsHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reflectVertButton = QPushButton(self.centralwidget)
        self.reflectVertButton.setObjectName(u"reflectVertButton")
        self.reflectVertButton.setGeometry(QRect(625, 360, 150, 40))
        self.reflectVertButton.setFont(font)
        self.reflectVertButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #3C3C3C;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3C3C3C;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/recources/icons/reflect_vertically.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reflectVertButton.setIcon(icon3)
        self.reflectHorizonButton = QPushButton(self.centralwidget)
        self.reflectHorizonButton.setObjectName(u"reflectHorizonButton")
        self.reflectHorizonButton.setGeometry(QRect(625, 410, 150, 40))
        self.reflectHorizonButton.setFont(font)
        self.reflectHorizonButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #3C3C3C;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3C3C3C;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/recources/icons/reflect_horizontally.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reflectHorizonButton.setIcon(icon4)
        self.rotateButton = QPushButton(self.centralwidget)
        self.rotateButton.setObjectName(u"rotateButton")
        self.rotateButton.setGeometry(QRect(625, 460, 150, 40))
        self.rotateButton.setFont(font)
        self.rotateButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #3C3C3C;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #5A5A5A;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #8E24AA;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3C3C3C;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/recources/icons/rotate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rotateButton.setIcon(icon5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imageWidget.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.applyFilterButton.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.filterHeader.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Blur", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BoxBlur", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Detail", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"EdgeEnhance", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"EdgeEnhanceMore", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Emboss", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"FindEdges", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"GaussianBlur", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Kernel", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Sharpen", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"SmoothMore", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Filter", None))
        self.saveFileButton.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.fileHeader.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.optionsHeader.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.reflectVertButton.setText(QCoreApplication.translate("MainWindow", u"Reflect vertically", None))
        self.reflectHorizonButton.setText(QCoreApplication.translate("MainWindow", u"Reflect horizontally", None))
        self.rotateButton.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
    # retranslateUi

