# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.GqGui import QBrush, QPalette, QImage
from PyQt5.QtCore import QSize


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(791, 710)

        background_img = QImage("graphics/background.jpg")
        scaled_img = background_img.scaled(QSize(791, 710))

        palette = QPalette()
        palette.setBrush(10,QBrush(scaled_img))
        Dialog.setPalette(palette)


        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 10, 91, 81))
        self.lcdNumber.setStyleSheet("QLCDNumber{background-color: rgb(16,164,255)}")
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(580, 20, 91, 81))
        self.lcdNumber_2.setStyleSheet("QLCDNumber{background-color: rgb(16,164,255)}")
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 100, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color: rgb(85,0,0)}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(510, 110, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color: rgb(85,0,0)}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 270, 121, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("graphics/ROCK.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(590, 270, 81, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("graphics/SCISSORS.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(560, 210, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(280, 10, 201, 231))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("graphics/rps_img.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(230, 260, 311, 141))
        self.frame.setStyleSheet("QFrame{background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69)) ;border:3px solid yellow}\n"
"\n"
"QToolButton{border: none}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 91, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/scissor_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(110, 10, 91, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/paper_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(210, 10, 91, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_3.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphics/rock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 410, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{color: rgb(85,0,0)}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(150, 500, 301, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{color: rgb(255,172,37)}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(460, 490, 121, 161))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("graphics/rock_win.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RPS Game"))
        self.label.setText(_translate("Dialog", "You"))
        self.label_2.setText(_translate("Dialog", "Computer"))
        self.label_3.setText(_translate("Dialog", "You Picked: "))
        self.label_6.setText(_translate("Dialog", "Computer Picked:"))
        self.toolButton.setText(_translate("Dialog", "Scissors"))
        self.toolButton_2.setText(_translate("Dialog", "Paper"))
        self.toolButton_3.setText(_translate("Dialog", "Rock"))
        self.label_8.setText(_translate("Dialog", "Rock Crushes Scissors"))
        self.label_9.setText(_translate("Dialog", "You Win!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
