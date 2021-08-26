# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setWindowModality(Qt.ApplicationModal)
        Settings.resize(727, 470)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QSize(360, 240))
        Settings.setMaximumSize(QSize(727, 470))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        Settings.setFont(font)
        Settings.setStyleSheet(u"QWidget\n"
"{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        Settings.setModal(False)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.file_path = QLineEdit(Settings)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setFont(font)

        self.horizontalLayout_2.addWidget(self.file_path)

        self.file_browser = QPushButton(Settings)
        self.file_browser.setObjectName(u"file_browser")
        self.file_browser.setFont(font)

        self.horizontalLayout_2.addWidget(self.file_browser)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(32)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.pre_record = QLineEdit(Settings)
        self.pre_record.setObjectName(u"pre_record")
        self.pre_record.setFont(font)

        self.horizontalLayout.addWidget(self.pre_record)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(32)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_fps = QLabel(Settings)
        self.lbl_fps.setObjectName(u"lbl_fps")
        sizePolicy.setHeightForWidth(self.lbl_fps.sizePolicy().hasHeightForWidth())
        self.lbl_fps.setSizePolicy(sizePolicy)
        self.lbl_fps.setFont(font)

        self.horizontalLayout_5.addWidget(self.lbl_fps)

        self.txt_fps = QLineEdit(Settings)
        self.txt_fps.setObjectName(u"txt_fps")
        self.txt_fps.setFont(font)

        self.horizontalLayout_5.addWidget(self.txt_fps)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(32)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_res = QLabel(Settings)
        self.lbl_res.setObjectName(u"lbl_res")
        sizePolicy.setHeightForWidth(self.lbl_res.sizePolicy().hasHeightForWidth())
        self.lbl_res.setSizePolicy(sizePolicy)
        self.lbl_res.setFont(font)

        self.horizontalLayout_6.addWidget(self.lbl_res)

        self.comboBox = QComboBox(Settings)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(32)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_addr = QLabel(Settings)
        self.lbl_addr.setObjectName(u"lbl_addr")
        sizePolicy.setHeightForWidth(self.lbl_addr.sizePolicy().hasHeightForWidth())
        self.lbl_addr.setSizePolicy(sizePolicy)
        self.lbl_addr.setFont(font)

        self.horizontalLayout_7.addWidget(self.lbl_addr)

        self.txt_addr = QLineEdit(Settings)
        self.txt_addr.setObjectName(u"txt_addr")
        self.txt_addr.setFont(font)

        self.horizontalLayout_7.addWidget(self.txt_addr)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(32)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_user = QLabel(Settings)
        self.lbl_user.setObjectName(u"lbl_user")
        sizePolicy.setHeightForWidth(self.lbl_user.sizePolicy().hasHeightForWidth())
        self.lbl_user.setSizePolicy(sizePolicy)
        self.lbl_user.setFont(font)

        self.horizontalLayout_8.addWidget(self.lbl_user)

        self.txt_user = QLineEdit(Settings)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setFont(font)

        self.horizontalLayout_8.addWidget(self.txt_user)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(32)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_password = QLabel(Settings)
        self.lbl_password.setObjectName(u"lbl_password")
        sizePolicy.setHeightForWidth(self.lbl_password.sizePolicy().hasHeightForWidth())
        self.lbl_password.setSizePolicy(sizePolicy)
        self.lbl_password.setFont(font)

        self.horizontalLayout_9.addWidget(self.lbl_password)

        self.txt_password = QLineEdit(Settings)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font)

        self.horizontalLayout_9.addWidget(self.txt_password)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(32)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.dlg_ok = QPushButton(Settings)
        self.dlg_ok.setObjectName(u"dlg_ok")
        self.dlg_ok.setFont(font)

        self.horizontalLayout_3.addWidget(self.dlg_ok)

        self.dlg_cancel = QPushButton(Settings)
        self.dlg_cancel.setObjectName(u"dlg_cancel")
        self.dlg_cancel.setFont(font)

        self.horizontalLayout_3.addWidget(self.dlg_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Saved recording file               ", None))
        self.file_browser.setText(QCoreApplication.translate("Settings", u"Browse", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Recording Duration (Secs)", None))
        self.lbl_fps.setText(QCoreApplication.translate("Settings", u"Frames Per Second (FPS)", None))
        self.lbl_res.setText(QCoreApplication.translate("Settings", u"Resolution                      ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Settings", u"1920x1080", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Settings", u"1280x720", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Settings", u"640x480", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Settings", u"320x240", None))

        self.lbl_addr.setText(QCoreApplication.translate("Settings", u"Camera Address             ", None))
        self.lbl_user.setText(QCoreApplication.translate("Settings", u"Cameara Username        ", None))
        self.lbl_password.setText(QCoreApplication.translate("Settings", u"Camera Password           ", None))
        self.dlg_ok.setText(QCoreApplication.translate("Settings", u"OK", None))
        self.dlg_cancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
    # retranslateUi

