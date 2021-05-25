from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(800, 480))
        Form.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 421))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setStyleSheet("background-image: url(:/newPrefix/800x380.png);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(200, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.tab)
        self.label2.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.tab)
        self.label3.setGeometry(QtCore.QRect(10, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.tab)
        self.label4.setGeometry(QtCore.QRect(200, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.tab)
        self.label5.setGeometry(QtCore.QRect(450, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.tab)
        self.label6.setGeometry(QtCore.QRect(580, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.tab)
        self.label7.setGeometry(QtCore.QRect(10, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 181, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color:  rgb(255, 49, 35);")
        self.pushButton.setObjectName("pushButton")
        self.label8 = QtWidgets.QLabel(self.tab)
        self.label8.setGeometry(QtCore.QRect(410, 40, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.label9 = QtWidgets.QLabel(self.tab)
        self.label9.setGeometry(QtCore.QRect(410, 70, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.pushButton2 = QtWidgets.QPushButton(self.tab)
        self.pushButton2.setGeometry(QtCore.QRect(320, 290, 161, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("background-color:  rgb(255, 49, 35);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.tab)
        self.pushButton3.setGeometry(QtCore.QRect(10, 200, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(self.tab)
        self.pushButton4.setGeometry(QtCore.QRect(140, 200, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(self.tab)
        self.pushButton5.setGeometry(QtCore.QRect(410, 200, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(self.tab)
        self.pushButton6.setGeometry(QtCore.QRect(270, 200,100,70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(self.tab)
        self.pushButton7.setGeometry(QtCore.QRect(540, 200, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton7.setFont(font)
        self.pushButton7.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 200, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: yellow\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_99 = QtWidgets.QLabel(self.tab_2)
        self.label_99.setGeometry(QtCore.QRect(0, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(220, 30, 121, 31))
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 80, 113, 31))
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_100 = QtWidgets.QLabel(self.tab_2)
        self.label_100.setGeometry(QtCore.QRect(10, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 130, 113, 31))
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_101 = QtWidgets.QLabel(self.tab_2)
        self.label_101.setGeometry(QtCore.QRect(70, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_102 = QtWidgets.QLabel(self.tab_2)
        self.label_102.setGeometry(QtCore.QRect(360, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_102.setFont(font)
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.tab_2)
        self.label_103.setGeometry(QtCore.QRect(350, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.tab_2)
        self.label_104.setGeometry(QtCore.QRect(350, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setObjectName("label_104")
        self.label_105 = QtWidgets.QLabel(self.tab_2)
        self.label_105.setGeometry(QtCore.QRect(350, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_105.setFont(font)
        self.label_105.setObjectName("label_105")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 170, 51, 25))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_106 = QtWidgets.QLabel(self.tab_2)
        self.label_106.setGeometry(QtCore.QRect(10, 170, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_106.setFont(font)
        self.label_106.setObjectName("label_106")
        self.label_107 = QtWidgets.QLabel(self.tab_2)
        self.label_107.setGeometry(QtCore.QRect(10, 200, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_107.setFont(font)
        self.label_107.setObjectName("label_107")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 200, 51, 25))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_108 = QtWidgets.QLabel(self.tab_2)
        self.label_108.setGeometry(QtCore.QRect(10, 230, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_108.setFont(font)
        self.label_108.setObjectName("label_108")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 230, 51, 25))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setMaxLength(2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_109 = QtWidgets.QLabel(self.tab_2)
        self.label_109.setGeometry(QtCore.QRect(10, 260, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_109.setFont(font)
        self.label_109.setObjectName("label_109")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 260, 51, 25))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setMaxLength(2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_110 = QtWidgets.QLabel(self.tab_2)
        self.label_110.setGeometry(QtCore.QRect(10, 290, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_110.setFont(font)
        self.label_110.setObjectName("label_110")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 290, 51, 25))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setMaxLength(4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 200, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(620, 10, 161, 31))
        self.lineEdit_9.setMaxLength(30)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_111 = QtWidgets.QLabel(self.tab_2)
        self.label_111.setGeometry(QtCore.QRect(480, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_111.setFont(font)
        self.label_111.setObjectName("label_111")
        self.label_112 = QtWidgets.QLabel(self.tab_2)
        self.label_112.setGeometry(QtCore.QRect(490, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_112.setFont(font)
        self.label_112.setObjectName("label_112")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(620, 50, 161, 31))
        self.lineEdit_10.setMaxLength(30)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(620, 90, 161, 31))
        self.lineEdit_11.setMaxLength(30)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_113 = QtWidgets.QLabel(self.tab_2)
        self.label_113.setGeometry(QtCore.QRect(520, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_113.setFont(font)
        self.label_113.setObjectName("label_113")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 140, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 300,100, 31))
        self.lineEdit_12.setMaxLength(15)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_114 = QtWidgets.QLabel(self.tab_2)
        self.label_114.setGeometry(QtCore.QRect(190, 300,100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_114.setFont(font)
        self.label_114.setObjectName("label_114")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "kalan sut"))
        self.label2.setText(_translate("Form", "kalan sut miktarı:"))
        self.label3.setText(_translate("Form", "verilen sut miktari:"))
        self.label4.setText(_translate("Form", "2lt"))
        self.label5.setText(_translate("Form", "sut sicakligi:"))
        self.label6.setText(_translate("Form", "sut sicakligi"))
        self.label7.setText(_translate("Form", "tarih"))
        self.pushButton.setText(_translate("Form", "doldur"))
        self.label8.setText(_translate("Form", "hosgeldiniz"))
        self.label9.setText(_translate("Form", "secim yapiniz"))
        self.pushButton2.setText(_translate("Form", "iptal"))
        self.pushButton3.setText(_translate("Form", "0,5lt"))
        self.pushButton4.setText(_translate("Form", "1lt"))
        self.pushButton5.setText(_translate("Form", "2lt"))
        self.pushButton6.setText(_translate("Form", "3lt"))
        self.pushButton7.setText(_translate("Form", "4lt"))
        self.pushButton_8.setText(_translate("Form", "5lt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "ANA SAYFA"))
        self.label_99.setText(_translate("Form", "LİTRE İCİN PULSE DEGERİ:"))
        self.lineEdit.setText(_translate("Form", "0212"))
        self.lineEdit_2.setText(_translate("Form", "3"))
        self.label_100.setText(_translate("Form", "KARISTIRCI START-STOP "))
        self.lineEdit_3.setText(_translate("Form", "300"))
        self.label_101.setText(_translate("Form", "SÜT MİKTARI"))
        self.pushButton_2.setText(_translate("Form", "sutmatik kaydet"))
        self.label_102.setText(_translate("Form", "pulse"))
        self.label_103.setText(_translate("Form", "dakika"))
        self.label_104.setText(_translate("Form", "tank hacmi"))
        self.label_105.setText(_translate("Form", "ayarlanan"))
        self.label_106.setText(_translate("Form", "dakika:"))
        self.label_107.setText(_translate("Form", "saat:"))
        self.label_108.setText(_translate("Form", "gün"))
        self.label_109.setText(_translate("Form", "ay"))
        self.label_110.setText(_translate("Form", "yil"))
        self.pushButton_3.setText(_translate("Form", "tarihi ayarla"))
        self.lineEdit_9.setText(_translate("Form", "abdurrahmantunc@gmail.com"))
        self.label_111.setText(_translate("Form", "gonderici gmail:"))
        self.label_112.setText(_translate("Form", "mail sifre:"))
        self.lineEdit_10.setText(_translate("Form", "muhendisBey"))
        self.lineEdit_11.setText(_translate("Form", "fatihozkaymak@hotmail.com"))
        self.label_113.setText(_translate("Form", "hedef mail:"))
        self.pushButton_4.setText(_translate("Form", "mail  ayarla"))
        self.lineEdit_12.setText(_translate("Form", "111"))
        self.label_114.setText(_translate("Form", "sifre:"))
        self.pushButton_5.setText(_translate("Form", "onayla"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "ayar"))
import source

''''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

'''
