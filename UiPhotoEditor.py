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
import res_rc

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
        self.openFileButton.setGeometry(QRect(625, 50, 150, 40))
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
        icon.addFile(u":/icon/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileButton.setIcon(icon)
        self.applyFilterButton = QPushButton(self.centralwidget)
        self.applyFilterButton.setObjectName(u"applyFilterButton")
        self.applyFilterButton.setGeometry(QRect(750, 300, 41, 40))
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
        icon1.addFile(u":/icon/icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.applyFilterButton.setIcon(icon1)
        self.filterHeader = QLabel(self.centralwidget)
        self.filterHeader.setObjectName(u"filterHeader")
        self.filterHeader.setGeometry(QRect(625, 250, 150, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.filterHeader.setFont(font1)
        self.filterHeader.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.filterHeader.setScaledContents(False)
        self.filterHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filterBox = QComboBox(self.centralwidget)
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.setObjectName(u"filterBox")
        self.filterBox.setGeometry(QRect(625, 300, 121, 40))
        self.filterBox.setFont(font)
        self.filterBox.setStyleSheet(u"background-color: #3C3C3C;\n"
"color: #FFFFFF;\n"
"border: 1px solid #5A5A5A;\n"
"padding-left: 5px;")
        self.saveFileButton = QPushButton(self.centralwidget)
        self.saveFileButton.setObjectName(u"saveFileButton")
        self.saveFileButton.setGeometry(QRect(625, 200, 150, 40))
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
        icon2.addFile(u":/icon/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveFileButton.setIcon(icon2)
        self.fileHeader = QLabel(self.centralwidget)
        self.fileHeader.setObjectName(u"fileHeader")
        self.fileHeader.setGeometry(QRect(625, 0, 150, 40))
        self.fileHeader.setFont(font1)
        self.fileHeader.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.fileHeader.setScaledContents(False)
        self.fileHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.optionsHeader = QLabel(self.centralwidget)
        self.optionsHeader.setObjectName(u"optionsHeader")
        self.optionsHeader.setGeometry(QRect(625, 400, 150, 40))
        self.optionsHeader.setFont(font1)
        self.optionsHeader.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.optionsHeader.setScaledContents(False)
        self.optionsHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reflectVertButton = QPushButton(self.centralwidget)
        self.reflectVertButton.setObjectName(u"reflectVertButton")
        self.reflectVertButton.setGeometry(QRect(625, 450, 150, 40))
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
        icon3.addFile(u":/icon/icons/reflect_vertically.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reflectVertButton.setIcon(icon3)
        self.reflectHorizonButton = QPushButton(self.centralwidget)
        self.reflectHorizonButton.setObjectName(u"reflectHorizonButton")
        self.reflectHorizonButton.setGeometry(QRect(625, 500, 150, 40))
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
        icon4.addFile(u":/icon/icons/reflect_horizontally.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reflectHorizonButton.setIcon(icon4)
        self.rotateButton = QPushButton(self.centralwidget)
        self.rotateButton.setObjectName(u"rotateButton")
        self.rotateButton.setGeometry(QRect(625, 550, 150, 40))
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
        icon5.addFile(u":/icon/icons/rotate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rotateButton.setIcon(icon5)
        self.openURLButton = QPushButton(self.centralwidget)
        self.openURLButton.setObjectName(u"openURLButton")
        self.openURLButton.setGeometry(QRect(625, 150, 150, 40))
        self.openURLButton.setFont(font)
        self.openURLButton.setStyleSheet(u"QPushButton\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/url.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openURLButton.setIcon(icon6)
        self.pasteImageButton = QPushButton(self.centralwidget)
        self.pasteImageButton.setObjectName(u"pasteImageButton")
        self.pasteImageButton.setGeometry(QRect(625, 100, 150, 40))
        self.pasteImageButton.setFont(font)
        self.pasteImageButton.setStyleSheet(u"QPushButton\n"
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
        self.pasteImageButton.setIcon(icon)
        self.brushButton = QPushButton(self.centralwidget)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setGeometry(QRect(750, 350, 41, 40))
        self.brushButton.setFont(font)
        self.brushButton.setStyleSheet(u"QPushButton\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/brush.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.brushButton.setIcon(icon7)
        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setGeometry(QRect(10, 0, 41, 40))
        self.undoButton.setFont(font)
        self.undoButton.setStyleSheet(u"QPushButton\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.undoButton.setIcon(icon8)
        self.colorBox = QComboBox(self.centralwidget)
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.setObjectName(u"colorBox")
        self.colorBox.setGeometry(QRect(625, 350, 121, 40))
        self.colorBox.setFont(font)
        self.colorBox.setStyleSheet(u"background-color: #3C3C3C;\n"
"color: #FFFFFF;\n"
"border: 1px solid #5A5A5A;\n"
"padding-left: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Photo Editor", None))
        self.imageWidget.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.applyFilterButton.setText("")
        self.filterHeader.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.filterBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Blur", None))
        self.filterBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BoxBlur", None))
        self.filterBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))
        self.filterBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Detail", None))
        self.filterBox.setItemText(4, QCoreApplication.translate("MainWindow", u"EdgeEnhance", None))
        self.filterBox.setItemText(5, QCoreApplication.translate("MainWindow", u"EdgeEnhanceMore", None))
        self.filterBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Emboss", None))
        self.filterBox.setItemText(7, QCoreApplication.translate("MainWindow", u"FindEdges", None))
        self.filterBox.setItemText(8, QCoreApplication.translate("MainWindow", u"GaussianBlur", None))
        self.filterBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Kernel", None))
        self.filterBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Sharpen", None))
        self.filterBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.filterBox.setItemText(12, QCoreApplication.translate("MainWindow", u"SmoothMore", None))

        self.filterBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Filter", None))
        self.saveFileButton.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.fileHeader.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.optionsHeader.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.reflectVertButton.setText(QCoreApplication.translate("MainWindow", u"Reflect vertically", None))
        self.reflectHorizonButton.setText(QCoreApplication.translate("MainWindow", u"Reflect horizontally", None))
        self.rotateButton.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.openURLButton.setText(QCoreApplication.translate("MainWindow", u"Open via URL", None))
        self.pasteImageButton.setText(QCoreApplication.translate("MainWindow", u"Paste image", None))
        self.brushButton.setText("")
        self.undoButton.setText("")
        self.colorBox.setItemText(0, QCoreApplication.translate("MainWindow", u"White", None))
        self.colorBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Black", None))
        self.colorBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Red", None))
        self.colorBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.colorBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.colorBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Green", None))
        self.colorBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Azure", None))
        self.colorBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.colorBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Purple", None))

        self.colorBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose color", None))
    # retranslateUi

