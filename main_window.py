# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.layout_main_window = QtWidgets.QWidget(MainWindow)
        self.layout_main_window.setObjectName("layout_main_window")
        self.gridLayout = QtWidgets.QGridLayout(self.layout_main_window)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_main_menu = QtWidgets.QTabWidget(self.layout_main_window)
        self.tab_main_menu.setObjectName("tab_main_menu")
        self.tab_accounts = QtWidgets.QWidget()
        self.tab_accounts.setObjectName("tab_accounts")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_accounts)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.h_layout_top_panel = QtWidgets.QHBoxLayout()
        self.h_layout_top_panel.setObjectName("h_layout_top_panel")
        self.btn_settings = QtWidgets.QToolButton(self.tab_accounts)
        self.btn_settings.setObjectName("btn_settings")
        self.h_layout_top_panel.addWidget(self.btn_settings)
        self.all_accounts_balance = QtWidgets.QLabel(self.tab_accounts)
        self.all_accounts_balance.setAlignment(QtCore.Qt.AlignCenter)
        self.all_accounts_balance.setObjectName("all_accounts_balance")
        self.h_layout_top_panel.addWidget(self.all_accounts_balance)
        self.btn_crt_new_acc = QtWidgets.QToolButton(self.tab_accounts)
        self.btn_crt_new_acc.setObjectName("btn_crt_new_acc")
        self.h_layout_top_panel.addWidget(self.btn_crt_new_acc)
        self.verticalLayout_3.addLayout(self.h_layout_top_panel)
        self.frame_panel_accs = QtWidgets.QFrame(self.tab_accounts)
        self.frame_panel_accs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_panel_accs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panel_accs.setObjectName("frame_panel_accs")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_panel_accs)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel_accs = QtWidgets.QHBoxLayout()
        self.panel_accs.setObjectName("panel_accs")
        self.name_panel_accs = QtWidgets.QLabel(self.frame_panel_accs)
        self.name_panel_accs.setObjectName("name_panel_accs")
        self.panel_accs.addWidget(self.name_panel_accs)
        self.all_accs_balance = QtWidgets.QLabel(self.frame_panel_accs)
        self.all_accs_balance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.all_accs_balance.setObjectName("all_accs_balance")
        self.panel_accs.addWidget(self.all_accs_balance)
        self.verticalLayout_2.addLayout(self.panel_accs)
        self.frame_accs = QtWidgets.QFrame(self.frame_panel_accs)
        self.frame_accs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_accs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_accs.setObjectName("frame_accs")
        self.verticalLayout_2.addWidget(self.frame_accs)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_panel_accs)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame_panel_savings = QtWidgets.QFrame(self.tab_accounts)
        self.frame_panel_savings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_panel_savings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panel_savings.setObjectName("frame_panel_savings")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_panel_savings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.panel_savings = QtWidgets.QHBoxLayout()
        self.panel_savings.setObjectName("panel_savings")
        self.name_panel_savings = QtWidgets.QLabel(self.frame_panel_savings)
        self.name_panel_savings.setObjectName("name_panel_savings")
        self.panel_savings.addWidget(self.name_panel_savings)
        self.all_savings_balance = QtWidgets.QLabel(self.frame_panel_savings)
        self.all_savings_balance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.all_savings_balance.setObjectName("all_savings_balance")
        self.panel_savings.addWidget(self.all_savings_balance)
        self.verticalLayout.addLayout(self.panel_savings)
        self.frame_savings = QtWidgets.QFrame(self.frame_panel_savings)
        self.frame_savings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_savings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_savings.setObjectName("frame_savings")
        self.verticalLayout.addWidget(self.frame_savings)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_panel_savings)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tab_main_menu.addTab(self.tab_accounts, "")
        self.tab_categories = QtWidgets.QWidget()
        self.tab_categories.setObjectName("tab_categories")
        self.tab_main_menu.addTab(self.tab_categories, "")
        self.tab_operations = QtWidgets.QWidget()
        self.tab_operations.setObjectName("tab_operations")
        self.tab_main_menu.addTab(self.tab_operations, "")
        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.tab_main_menu.addTab(self.tab_overview, "")
        self.gridLayout.addWidget(self.tab_main_menu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.layout_main_window)

        self.retranslateUi(MainWindow)
        self.tab_main_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_new_account(self, acc_object):
        self.frame = QtWidgets.QFrame(self.frame_panel_accs)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title)
        self.desription = QtWidgets.QLabel(self.frame)
        self.desription.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.desription.setObjectName("desription")
        self.horizontalLayout_2.addWidget(self.desription)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.balancecurrency = QtWidgets.QLabel(self.frame)
        self.balancecurrency.setObjectName("balancecurrency")
        self.horizontalLayout.addWidget(self.balancecurrency)
        self.btn_more_info = QtWidgets.QToolButton(self.frame)
        self.btn_more_info.setObjectName("btn_more_info")
        self.horizontalLayout.addWidget(self.btn_more_info)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)

        # self.title.setText(title)
        # self.desription.setText(description)
        # self.balancecurrency.setText(str(balance) + currency)
        # self.btn_more_info.setText("...")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MoneyTrack"))
        self.btn_settings.setText(_translate("MainWindow", "S"))
        self.all_accounts_balance.setText(_translate("MainWindow", "0"))
        self.btn_crt_new_acc.setText(_translate("MainWindow", "+"))
        self.name_panel_accs.setText(_translate("MainWindow", "СЧЕТА"))
        self.all_accs_balance.setText(_translate("MainWindow", "0"))
        self.name_panel_savings.setText(_translate("MainWindow", "СБЕРЕЖЕНИЯ"))
        self.all_savings_balance.setText(_translate("MainWindow", "0"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_accounts), _translate("MainWindow", "Счета"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_categories), _translate("MainWindow", "Категории"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_operations), _translate("MainWindow", "Операции"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_overview), _translate("MainWindow", "Обзор"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
