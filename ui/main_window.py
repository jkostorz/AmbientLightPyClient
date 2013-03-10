# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Mar 10 21:53:50 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(680, 585)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(680, 585))
        MainWindow.setStyleSheet(_fromUtf8("#contentFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(53, 58, 62, 0), \n"
"    stop:0.05 rgba(53, 58, 62, 0), \n"
"    stop:0.051 rgba(53, 58, 62, 255), \n"
"    stop:0.96 rgba(53, 58, 62, 255), \n"
"    stop:0.961 rgba(53, 58, 62, 0), \n"
"    stop:1 rgba(53, 58, 62, 0));\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin: 0 3px 0 3px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg_fill.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin: 1px 0 2px 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(:ui/resources/slider_handle.png);\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    margin: -2px -14px -4px -9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-image: url(:ui/resources/slider_handle_hover.png);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(:ui/resources/slider_handle_pressed.png);\n"
"}\n"
"\n"
"\n"
"\n"
"#hueSlider::groove:horizontal {\n"
"    border-image: url(:ui/resources/slider_bg_hue.png) 0 8 0 8;\n"
"}\n"
"\n"
"#hueSlider::sub-page:horizontal {\n"
"    border-image: none;\n"
"}"))
        MainWindow.setAnimated(True)
        self.shadowPadding = QtGui.QWidget(MainWindow)
        self.shadowPadding.setStyleSheet(_fromUtf8("#centralWidget { background-color: #ffffff; }    "))
        self.shadowPadding.setObjectName(_fromUtf8("shadowPadding"))
        self.shadowPad = QtGui.QVBoxLayout(self.shadowPadding)
        self.shadowPad.setSpacing(0)
        self.shadowPad.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.shadowPad.setMargin(20)
        self.shadowPad.setObjectName(_fromUtf8("shadowPad"))
        self.contentFrame = QtGui.QFrame(self.shadowPadding)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setMinimumSize(QtCore.QSize(640, 545))
        self.contentFrame.setMaximumSize(QtCore.QSize(640, 545))
        self.contentFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.contentFrame.setLineWidth(0)
        self.contentFrame.setObjectName(_fromUtf8("contentFrame"))
        self.titleBar = QtGui.QFrame(self.contentFrame)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 640, 40))
        self.titleBar.setStyleSheet(_fromUtf8("#titleBar {\n"
"    border-image: url(:ui/resources/titlebar_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-family: Arial, sans-serif;\n"
"    color: #e4e4e4;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"#closeButton {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg.png) 0 6 0 6;\n"
"    border-left: 6px;\n"
"    border-right: 6px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"#closeButton:hover {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg_hover.png) 0 6 0 6;\n"
"}\n"
"\n"
"#closeButton:pressed {\n"
"    border-image: url(:ui/resources/titlebar_closebutton_bg_pressed.png) 0 6 0 6;\n"
"}"))
        self.titleBar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtGui.QFrame.Raised)
        self.titleBar.setObjectName(_fromUtf8("titleBar"))
        self.titleLabel = QtGui.QLabel(self.titleBar)
        self.titleLabel.setGeometry(QtCore.QRect(20, 13, 131, 16))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.closeButton = QtGui.QPushButton(self.titleBar)
        self.closeButton.setGeometry(QtCore.QRect(580, 0, 48, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(48, 22))
        self.closeButton.setMaximumSize(QtCore.QSize(22, 16777215))
        self.closeButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(20, 20))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.tabWidget = QtGui.QTabWidget(self.contentFrame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 12, 640, 508))
        self.tabWidget.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 0px;\n"
"}\n"
" \n"
"QTabWidget::tab-bar  {\n"
"    left: 212px;\n"
"}\n"
" \n"
"QTabBar::tab  {\n"
"    font-size: 8pt;\n"
"    color: #ffffff;\n"
"    border-image: url(:ui/resources/titlebar_button_bg.png) 0 8 0 8;\n"
"    border-left: 8px;\n"
"    border-right: 8px;\n"
"    margin-right: 10px;\n"
"    padding: 1px 0 0 3px;\n"
"    height: 27px;\n"
"}\n"
" \n"
"QTabBar::tab:hover  {\n"
"    border-image: url(:ui/resources/titlebar_button_bg_hover.png) 0 8 0 8;\n"
"}\n"
" \n"
"QTabBar::tab:selected  {\n"
"    border-image: url(:ui/resources/titlebar_button_bg_selected.png) 0 8 0 8;\n"
"}"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 18))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.samplerTab = QtGui.QWidget()
        self.samplerTab.setObjectName(_fromUtf8("samplerTab"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_sampler.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.samplerTab, icon1, _fromUtf8(""))
        self.colorsTab = QtGui.QWidget()
        self.colorsTab.setObjectName(_fromUtf8("colorsTab"))
        self.horizontalSlider = QtGui.QSlider(self.colorsTab)
        self.horizontalSlider.setGeometry(QtCore.QRect(243, 113, 171, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setProperty("value", 100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.hueSlider = QtGui.QSlider(self.colorsTab)
        self.hueSlider.setGeometry(QtCore.QRect(243, 146, 171, 22))
        self.hueSlider.setStyleSheet(_fromUtf8(""))
        self.hueSlider.setMaximum(100)
        self.hueSlider.setProperty("value", 50)
        self.hueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hueSlider.setObjectName(_fromUtf8("hueSlider"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_colors.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.colorsTab, icon2, _fromUtf8(""))
        self.serverTab = QtGui.QWidget()
        self.serverTab.setObjectName(_fromUtf8("serverTab"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/ui/resources/icon_server.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.serverTab, icon3, _fromUtf8(""))
        self.titleBarShadow = QtGui.QFrame(self.contentFrame)
        self.titleBarShadow.setGeometry(QtCore.QRect(0, 39, 640, 8))
        self.titleBarShadow.setStyleSheet(_fromUtf8("#titleBarShadow {\n"
"    background: url(:ui/resources/titlebar_shadow.png);\n"
"    background-position: top;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}"))
        self.titleBarShadow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.titleBarShadow.setFrameShadow(QtGui.QFrame.Raised)
        self.titleBarShadow.setLineWidth(0)
        self.titleBarShadow.setObjectName(_fromUtf8("titleBarShadow"))
        self.tabSelectionArrow = QtGui.QFrame(self.contentFrame)
        self.tabSelectionArrow.setGeometry(QtCore.QRect(352, 35, 20, 10))
        self.tabSelectionArrow.setStyleSheet(_fromUtf8("#tabSelectionArrow {\n"
"    width: 20px;\n"
"    height: 10px;\n"
"    background: url(:ui/resources/titlebar_button_arrow.png);\n"
"    background-position: top left;\n"
"}"))
        self.tabSelectionArrow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tabSelectionArrow.setFrameShadow(QtGui.QFrame.Raised)
        self.tabSelectionArrow.setObjectName(_fromUtf8("tabSelectionArrow"))
        self.shadowPad.addWidget(self.contentFrame)
        MainWindow.setCentralWidget(self.shadowPadding)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.titleLabel.setText(_translate("MainWindow", "Ambient Light Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.samplerTab), _translate("MainWindow", "SAMPLER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colorsTab), _translate("MainWindow", "COLORS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serverTab), _translate("MainWindow", "SERVER", None))

import ui.main_window_rc
import titlebar_rc
