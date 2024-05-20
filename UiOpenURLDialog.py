# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenURLDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: #2E2E2E;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 360, 260))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.URLEdit = QLineEdit(self.frame)
        self.URLEdit.setObjectName(u"URLEdit")
        self.URLEdit.setGeometry(QRect(50, 80, 250, 40))
        font = QFont()
        font.setPointSize(10)
        self.URLEdit.setFont(font)
        self.URLEdit.setStyleSheet(u"background-color: #3C3C3C;\n"
"color: #FFFFFF;\n"
"border: 1px solid #5A5A5A;\n"
"border-radius: 10px;\n"
"padding-left: 5px;")
        self.URLButton = QPushButton(self.frame)
        self.URLButton.setObjectName(u"URLButton")
        self.URLButton.setGeometry(QRect(100, 140, 150, 40))
        self.URLButton.setFont(font)
        self.URLButton.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u":/icon/icons/url.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.URLButton.setIcon(icon)
        self.URLHeader = QLabel(self.frame)
        self.URLHeader.setObjectName(u"URLHeader")
        self.URLHeader.setGeometry(QRect(75, 20, 200, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.URLHeader.setFont(font1)
        self.URLHeader.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.URLHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.URLError = QLabel(self.frame)
        self.URLError.setObjectName(u"URLError")
        self.URLError.setGeometry(QRect(50, 200, 250, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.URLError.setFont(font2)
        self.URLError.setStyleSheet(u"background-color: none;\n"
"color: #FF0000;")
        self.URLError.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open Image via URL", None))
        self.URLEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type URL", None))
        self.URLButton.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.URLHeader.setText(QCoreApplication.translate("Dialog", u"Open Image via URL", None))
        self.URLError.setText("")
    # retranslateUi

