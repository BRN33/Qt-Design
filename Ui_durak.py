# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ugur.baran\Desktop\Qt Design\durak.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DurakEkle(object):
    def setupUi(self, DurakEkle):
        DurakEkle.setObjectName("DurakEkle")
        DurakEkle.resize(980, 645)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DurakEkle.sizePolicy().hasHeightForWidth())
        DurakEkle.setSizePolicy(sizePolicy)
        DurakEkle.setAutoFillBackground(True)
        self.gridLayout = QtWidgets.QGridLayout(DurakEkle)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(DurakEkle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 50, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lblSes = QtWidgets.QLabel(self.groupBox_3)
        self.lblSes.setGeometry(QtCore.QRect(70, 40, 31, 16))
        self.lblSes.setObjectName("lblSes")
        self.sesScroll = QtWidgets.QSlider(self.groupBox_3)
        self.sesScroll.setGeometry(QtCore.QRect(10, 60, 160, 22))
        self.sesScroll.setOrientation(QtCore.Qt.Horizontal)
        self.sesScroll.setObjectName("sesScroll")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.lblKapDurumu = QtWidgets.QLabel(self.groupBox)
        self.lblKapDurumu.setGeometry(QtCore.QRect(50, 50, 55, 16))
        self.lblKapDurumu.setObjectName("lblKapDurumu")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 50, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblAracDurumu = QtWidgets.QLabel(self.groupBox_2)
        self.lblAracDurumu.setGeometry(QtCore.QRect(40, 50, 55, 16))
        self.lblAracDurumu.setObjectName("lblAracDurumu")
        self.btnTako = QtWidgets.QPushButton(self.tab)
        self.btnTako.setGeometry(QtCore.QRect(680, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnTako.setFont(font)
        self.btnTako.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(255, 15, 71);")
        self.btnTako.setObjectName("btnTako")
        self.btnAnonsKapat = QtWidgets.QPushButton(self.tab)
        self.btnAnonsKapat.setGeometry(QtCore.QRect(680, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnAnonsKapat.setFont(font)
        self.btnAnonsKapat.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(255, 15, 71);")
        self.btnAnonsKapat.setObjectName("btnAnonsKapat")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 200, 841, 121))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_7.setObjectName("groupBox_7")
        self.lbllkstasyon = QtWidgets.QLabel(self.groupBox_7)
        self.lbllkstasyon.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.lbllkstasyon.setObjectName("lbllkstasyon")
        self.lblikincistasyon = QtWidgets.QLabel(self.groupBox_7)
        self.lblikincistasyon.setGeometry(QtCore.QRect(180, 80, 55, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblikincistasyon.sizePolicy().hasHeightForWidth())
        self.lblikincistasyon.setSizePolicy(sizePolicy)
        self.lblikincistasyon.setObjectName("lblikincistasyon")
        self.lblUcIstasyon = QtWidgets.QLabel(self.groupBox_7)
        self.lblUcIstasyon.setGeometry(QtCore.QRect(350, 80, 55, 16))
        self.lblUcIstasyon.setObjectName("lblUcIstasyon")
        self.lblHedef = QtWidgets.QLabel(self.groupBox_7)
        self.lblHedef.setGeometry(QtCore.QRect(550, 80, 101, 16))
        self.lblHedef.setObjectName("lblHedef")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 380, 161, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lblGelecekstasyon = QtWidgets.QLabel(self.groupBox_4)
        self.lblGelecekstasyon.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.lblGelecekstasyon.setObjectName("lblGelecekstasyon")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(200, 380, 181, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.lblHedefstasyon = QtWidgets.QLabel(self.groupBox_5)
        self.lblHedefstasyon.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.lblHedefstasyon.setObjectName("lblHedefstasyon")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(460, 380, 131, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.lblKalanMesafe = QtWidgets.QLabel(self.groupBox_6)
        self.lblKalanMesafe.setGeometry(QtCore.QRect(40, 40, 55, 16))
        self.lblKalanMesafe.setObjectName("lblKalanMesafe")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(610, 380, 131, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_8.setObjectName("groupBox_8")
        self.lblToplamMesafe = QtWidgets.QLabel(self.groupBox_8)
        self.lblToplamMesafe.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.lblToplamMesafe.setObjectName("lblToplamMesafe")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.hatcombobox = QtWidgets.QComboBox(self.tab_3)
        self.hatcombobox.setGeometry(QtCore.QRect(20, 40, 171, 22))
        self.hatcombobox.setStyleSheet("color: rgb(255, 255, 255);")
        self.hatcombobox.setEditable(False)
        self.hatcombobox.setObjectName("hatcombobox")
        self.hatcombobox.addItem("")
        self.hatcombobox.addItem("")
        self.hatcombobox.addItem("")
        self.hatcombobox.addItem("")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.biLabel = QtWidgets.QLabel(self.tab_3)
        self.biLabel.setGeometry(QtCore.QRect(130, 80, 131, 16))
        self.biLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.biLabel.setObjectName("biLabel")
        self.hiLabel = QtWidgets.QLabel(self.tab_3)
        self.hiLabel.setGeometry(QtCore.QRect(130, 110, 121, 16))
        self.hiLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.hiLabel.setObjectName("hiLabel")
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(0, 130, 761, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(0, 70, 761, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.onaybtn = QtWidgets.QPushButton(self.tab_3)
        self.onaybtn.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.onaybtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.onaybtn.setObjectName("onaybtn")
        self.iptalbtn = QtWidgets.QPushButton(self.tab_3)
        self.iptalbtn.setGeometry(QtCore.QRect(390, 100, 75, 23))
        self.iptalbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.iptalbtn.setObjectName("iptalbtn")
        self.grBoxStation = QtWidgets.QGroupBox(self.tab_3)
        self.grBoxStation.setGeometry(QtCore.QRect(10, 150, 931, 431))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.grBoxStation.setFont(font)
        self.grBoxStation.setStyleSheet("background-color: rgb(207, 207, 213);")
        self.grBoxStation.setObjectName("grBoxStation")
        self.gridLayoutWidget = QtWidgets.QWidget(self.grBoxStation)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(2, 20, 931, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.btnAracDepo = QtWidgets.QPushButton(self.tab_4)
        self.btnAracDepo.setEnabled(True)
        self.btnAracDepo.setGeometry(QtCore.QRect(10, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAracDepo.setFont(font)
        self.btnAracDepo.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAracDepo.setToolTip("")
        self.btnAracDepo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.btnAracDepo.setObjectName("btnAracDepo")
        self.btnAracServisDisi = QtWidgets.QPushButton(self.tab_4)
        self.btnAracServisDisi.setGeometry(QtCore.QRect(250, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAracServisDisi.setFont(font)
        self.btnAracServisDisi.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAracServisDisi.setToolTip("")
        self.btnAracServisDisi.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnAracServisDisi.setObjectName("btnAracServisDisi")
        self.btnAracAriza = QtWidgets.QPushButton(self.tab_4)
        self.btnAracAriza.setGeometry(QtCore.QRect(480, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAracAriza.setFont(font)
        self.btnAracAriza.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAracAriza.setToolTip("")
        self.btnAracAriza.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnAracAriza.setObjectName("btnAracAriza")
        self.btnOncelikTani = QtWidgets.QPushButton(self.tab_4)
        self.btnOncelikTani.setGeometry(QtCore.QRect(710, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnOncelikTani.setFont(font)
        self.btnOncelikTani.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnOncelikTani.setToolTip("")
        self.btnOncelikTani.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.btnOncelikTani.setObjectName("btnOncelikTani")
        self.btnCoronaVirus = QtWidgets.QPushButton(self.tab_4)
        self.btnCoronaVirus.setGeometry(QtCore.QRect(710, 110, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCoronaVirus.setFont(font)
        self.btnCoronaVirus.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnCoronaVirus.setToolTip("")
        self.btnCoronaVirus.setStyleSheet("background-color: rgb(255, 85, 0);color: rgb(255, 255, 255);")
        self.btnCoronaVirus.setObjectName("btnCoronaVirus")
        self.btnKapiYaslanma = QtWidgets.QPushButton(self.tab_4)
        self.btnKapiYaslanma.setGeometry(QtCore.QRect(480, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnKapiYaslanma.setFont(font)
        self.btnKapiYaslanma.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnKapiYaslanma.setToolTip("")
        self.btnKapiYaslanma.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(255, 85, 0);")
        self.btnKapiYaslanma.setObjectName("btnKapiYaslanma")
        self.btnKapiKapanma = QtWidgets.QPushButton(self.tab_4)
        self.btnKapiKapanma.setGeometry(QtCore.QRect(10, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnKapiKapanma.setFont(font)
        self.btnKapiKapanma.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnKapiKapanma.setToolTip("")
        self.btnKapiKapanma.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(255, 85, 0);")
        self.btnKapiKapanma.setObjectName("btnKapiKapanma")
        self.btnKapiOnunde = QtWidgets.QPushButton(self.tab_4)
        self.btnKapiOnunde.setGeometry(QtCore.QRect(250, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnKapiOnunde.setFont(font)
        self.btnKapiOnunde.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnKapiOnunde.setToolTip("")
        self.btnKapiOnunde.setStyleSheet("background-color: rgb(255, 85, 0);color: rgb(255, 255, 255);")
        self.btnKapiOnunde.setObjectName("btnKapiOnunde")
        self.btnSigaraYasak = QtWidgets.QPushButton(self.tab_4)
        self.btnSigaraYasak.setEnabled(True)
        self.btnSigaraYasak.setGeometry(QtCore.QRect(10, 190, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSigaraYasak.setFont(font)
        self.btnSigaraYasak.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnSigaraYasak.setMouseTracking(False)
        self.btnSigaraYasak.setToolTip("")
        self.btnSigaraYasak.setStyleSheet("background-color: rgb(255, 85, 0);color: rgb(255, 255, 255);")
        self.btnSigaraYasak.setObjectName("btnSigaraYasak")
        self.btnSinyalKapali = QtWidgets.QPushButton(self.tab_4)
        self.btnSinyalKapali.setGeometry(QtCore.QRect(250, 190, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSinyalKapali.setFont(font)
        self.btnSinyalKapali.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnSinyalKapali.setToolTip("")
        self.btnSinyalKapali.setStyleSheet("background-color: rgb(255, 85, 0);color: rgb(255, 255, 255);")
        self.btnSinyalKapali.setObjectName("btnSinyalKapali")
        self.btnYasliEngelli = QtWidgets.QPushButton(self.tab_4)
        self.btnYasliEngelli.setGeometry(QtCore.QRect(480, 190, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnYasliEngelli.setFont(font)
        self.btnYasliEngelli.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnYasliEngelli.setToolTip("")
        self.btnYasliEngelli.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.btnYasliEngelli.setObjectName("btnYasliEngelli")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(DurakEkle)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DurakEkle)

    def retranslateUi(self, DurakEkle):
        _translate = QtCore.QCoreApplication.translate
        DurakEkle.setWindowTitle(_translate("DurakEkle", "DurakEkle"))
        self.groupBox_3.setTitle(_translate("DurakEkle", "Ses Ayarı"))
        self.lblSes.setText(_translate("DurakEkle", "%"))
        self.groupBox.setTitle(_translate("DurakEkle", "Kapı Durumu"))
        self.lblKapDurumu.setText(_translate("DurakEkle", "---"))
        self.groupBox_2.setTitle(_translate("DurakEkle", "Araç Durumu"))
        self.lblAracDurumu.setText(_translate("DurakEkle", "---"))
        self.btnTako.setText(_translate("DurakEkle", "Takometre ByPass"))
        self.btnAnonsKapat.setText(_translate("DurakEkle", "Anons Kapat"))
        self.groupBox_7.setTitle(_translate("DurakEkle", "ARACIN KONUMU"))
        self.lbllkstasyon.setText(_translate("DurakEkle", "ilk istasyon"))
        self.lblikincistasyon.setText(_translate("DurakEkle", "-----"))
        self.lblUcIstasyon.setText(_translate("DurakEkle", "-----"))
        self.lblHedef.setText(_translate("DurakEkle", "son istasyon"))
        self.groupBox_4.setTitle(_translate("DurakEkle", "Gelecek İstasyon"))
        self.lblGelecekstasyon.setText(_translate("DurakEkle", "---"))
        self.groupBox_5.setTitle(_translate("DurakEkle", "Hedef İstasyon"))
        self.lblHedefstasyon.setText(_translate("DurakEkle", "---"))
        self.groupBox_6.setTitle(_translate("DurakEkle", "Kalan Mesafae"))
        self.lblKalanMesafe.setText(_translate("DurakEkle", "---"))
        self.groupBox_8.setTitle(_translate("DurakEkle", "Toplam Mesafe"))
        self.lblToplamMesafe.setText(_translate("DurakEkle", "---"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DurakEkle", "ARAÇ BİLGİLERİ"))
        self.hatcombobox.setItemText(0, _translate("DurakEkle", "M3"))
        self.hatcombobox.setItemText(1, _translate("DurakEkle", "M9"))
        self.hatcombobox.setItemText(2, _translate("DurakEkle", "M5"))
        self.hatcombobox.setItemText(3, _translate("DurakEkle", "M6"))
        self.label.setText(_translate("DurakEkle", "Hat Seçiniz"))
        self.label_2.setText(_translate("DurakEkle", "Başlangıç İstasyonu :"))
        self.label_3.setText(_translate("DurakEkle", "Hedef İstasyon :"))
        self.biLabel.setText(_translate("DurakEkle", "ilk Durak"))
        self.hiLabel.setText(_translate("DurakEkle", "Son Durak"))
        self.onaybtn.setText(_translate("DurakEkle", "Onayla"))
        self.iptalbtn.setText(_translate("DurakEkle", "İptal"))
        self.grBoxStation.setTitle(_translate("DurakEkle", "İstasyonlar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DurakEkle", "ROTA KUR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DurakEkle", "BAŞLANGIÇ ANONSLARI"))
        self.btnAracDepo.setText(_translate("DurakEkle", "ARAÇ DEPOYA GİDER"))
        self.btnAracServisDisi.setText(_translate("DurakEkle", "ARAÇ SERVİS DIŞI"))
        self.btnAracAriza.setText(_translate("DurakEkle", "ARAÇ ARIZALIDIR"))
        self.btnOncelikTani.setText(_translate("DurakEkle", "İNENLERE ÖNCELİK \n"
"    TANIYIN"))
        self.btnCoronaVirus.setText(_translate("DurakEkle", "CORONA VİRÜS"))
        self.btnKapiYaslanma.setText(_translate("DurakEkle", "LÜTFEN KAPILARA \n"
"  YASLANMAYIN"))
        self.btnKapiKapanma.setText(_translate("DurakEkle", "KAPI KAPANIYOR"))
        self.btnKapiOnunde.setText(_translate("DurakEkle", "LÜTFEN KAPI ÖNÜNDE \n"
"    BEKLEMEYİNİZ"))
        self.btnSigaraYasak.setText(_translate("DurakEkle", "SİGARA YASAĞI"))
        self.btnSinyalKapali.setText(_translate("DurakEkle", "SİNYAL KAPALI"))
        self.btnYasliEngelli.setText(_translate("DurakEkle", "YAŞLI VE ENGELLİLER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("DurakEkle", "ÖZEL ANONSLAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("DurakEkle", "İSTASYON ANAONSLARI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("DurakEkle", "AYARLAR"))
