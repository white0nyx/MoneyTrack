from PyQt5 import QtCore, QtGui, QtWidgets


class UiFrameOperation(object):

    def __init__(self, frame_operation):
        """Инициализация операции"""
        frame_operation.setObjectName("frame_operation")
        frame_operation.resize(400, 63)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frame_operation)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IMAGE = QtWidgets.QLabel(frame_operation)
        self.IMAGE.setObjectName("IMAGE")
        self.horizontalLayout.addWidget(self.IMAGE)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(frame_operation)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(frame_operation)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(frame_operation)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(size_policy)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(frame_operation)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.set_all_text(frame_operation)
        QtCore.QMetaObject.connectSlotsByName(frame_operation)

    def set_all_text(self, frame_operation):
        """Установка всего текста"""
        _translate = QtCore.QCoreApplication.translate
        frame_operation.setWindowTitle(_translate("frame_operation", "Frame"))
        self.IMAGE.setText(_translate("frame_operation", "IMAGE"))
        self.label.setText(_translate("frame_operation", "Category (Under category)"))
        self.label_2.setText(_translate("frame_operation", "Account"))
        self.label_3.setText(_translate("frame_operation", "amount"))
        self.label_4.setText(_translate("frame_operation", "Date"))
