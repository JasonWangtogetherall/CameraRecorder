# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ptz_camera_controller.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.resources_rc

class Ui_PTZCameraController(object):
    def setupUi(self, PTZCameraController):
        if not PTZCameraController.objectName():
            PTZCameraController.setObjectName(u"PTZCameraController")
        PTZCameraController.resize(874, 697)
        self.widget = QWidget(PTZCameraController)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton#pan_minus\n"
"{\n"
"border-size: 0px 0px 0px 0x;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.video_frame = QLabel(self.widget)
        self.video_frame.setObjectName(u"video_frame")
        self.video_frame.setScaledContents(False)
        self.video_frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.video_frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pan_minus = QPushButton(self.frame)
        self.pan_minus.setObjectName(u"pan_minus")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pan_minus.sizePolicy().hasHeightForWidth())
        self.pan_minus.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/utils/arrow_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pan_minus.setIcon(icon)
        self.pan_minus.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pan_minus, 3, 2, 1, 1)

        self.pan_plus = QPushButton(self.frame)
        self.pan_plus.setObjectName(u"pan_plus")
        sizePolicy.setHeightForWidth(self.pan_plus.sizePolicy().hasHeightForWidth())
        self.pan_plus.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/images/utils/arrow_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pan_plus.setIcon(icon1)
        self.pan_plus.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pan_plus, 1, 2, 1, 1)

        self.tilt_plus = QPushButton(self.frame)
        self.tilt_plus.setObjectName(u"tilt_plus")
        sizePolicy.setHeightForWidth(self.tilt_plus.sizePolicy().hasHeightForWidth())
        self.tilt_plus.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/images/utils/arrow_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tilt_plus.setIcon(icon2)
        self.tilt_plus.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.tilt_plus, 2, 3, 1, 1)

        self.tilt_minus = QPushButton(self.frame)
        self.tilt_minus.setObjectName(u"tilt_minus")
        sizePolicy.setHeightForWidth(self.tilt_minus.sizePolicy().hasHeightForWidth())
        self.tilt_minus.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u":/images/utils/arrow_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tilt_minus.setIcon(icon3)
        self.tilt_minus.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.tilt_minus, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 5, 2, 1)

        self.record = QPushButton(self.widget)
        self.record.setObjectName(u"record")
        sizePolicy.setHeightForWidth(self.record.sizePolicy().hasHeightForWidth())
        self.record.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/images/utils/record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.record.setIcon(icon4)
        self.record.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.record, 3, 1, 1, 1)

        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u":/images/utils/settings2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon5)
        self.settings.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.settings, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.zoom_minus = QPushButton(self.widget)
        self.zoom_minus.setObjectName(u"zoom_minus")
        sizePolicy.setHeightForWidth(self.zoom_minus.sizePolicy().hasHeightForWidth())
        self.zoom_minus.setSizePolicy(sizePolicy)
        icon6 = QIcon()
        icon6.addFile(u":/images/utils/zoomout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_minus.setIcon(icon6)
        self.zoom_minus.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.zoom_minus, 3, 2, 1, 1)

        self.zoom_plus = QPushButton(self.widget)
        self.zoom_plus.setObjectName(u"zoom_plus")
        sizePolicy.setHeightForWidth(self.zoom_plus.sizePolicy().hasHeightForWidth())
        self.zoom_plus.setSizePolicy(sizePolicy)
        icon7 = QIcon()
        icon7.addFile(u":/images/utils/zoomin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_plus.setIcon(icon7)
        self.zoom_plus.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.zoom_plus, 3, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 11)
        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        PTZCameraController.setCentralWidget(self.widget)

        self.retranslateUi(PTZCameraController)

        QMetaObject.connectSlotsByName(PTZCameraController)
    # setupUi

    def retranslateUi(self, PTZCameraController):
        PTZCameraController.setWindowTitle(QCoreApplication.translate("PTZCameraController", u"MainWindow", None))
        self.video_frame.setText("")
        self.pan_minus.setText("")
        self.pan_plus.setText("")
        self.tilt_plus.setText("")
        self.tilt_minus.setText("")
        self.record.setText("")
        self.settings.setText("")
        self.zoom_minus.setText("")
        self.zoom_plus.setText("")
    # retranslateUi

