# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from acc_object import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Метод для прорисовки основного окна"""
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
        self.all_accs_balance.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
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
        self.all_savings_balance.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
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

        self.all_accs_buttons = []

        self.add_all_accs_to_gui()
        self.refresh_balances()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_new_account(self, acc_object):
        """Метод для прорисовки счёта на главном окне"""

        if acc_object._type == 'Обычный':
            self.frame1 = QtWidgets.QFrame(self.frame_panel_accs)
            self.frame1.setEnabled(True)
            self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame1.setObjectName("frame11")
            self.gridLayout1 = QtWidgets.QGridLayout(self.frame1)
            self.gridLayout1.setContentsMargins(0, 0, 0, -1)
            self.gridLayout1.setObjectName("gridLayout1")
            self.verticalLayout1 = QtWidgets.QVBoxLayout()
            self.verticalLayout1.setObjectName("verticalLayout1")
            self.horizontalLayout1 = QtWidgets.QHBoxLayout()
            self.horizontalLayout1.setObjectName("horizontalLayout1")
            self.title1 = QtWidgets.QLabel(self.frame1)
            self.title1.setObjectName("title1")
            self.horizontalLayout1.addWidget(self.title1)
            self.desription1 = QtWidgets.QLabel(self.frame1)
            self.desription1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.desription1.setObjectName("desription")
            self.horizontalLayout1.addWidget(self.desription1)
            self.verticalLayout1.addLayout(self.horizontalLayout1)
            self.horizontalLayout1 = QtWidgets.QHBoxLayout()
            self.horizontalLayout1.setObjectName("horizontalLayout1")
            self.balancecurrency1 = QtWidgets.QLabel(self.frame1)
            self.balancecurrency1.setObjectName("balancecurrency1")
            self.horizontalLayout1.addWidget(self.balancecurrency1)
            self.btn_more_info1 = QtWidgets.QToolButton(self.frame1)
            self.btn_more_info1.setObjectName("btn_more_info1")
            self.horizontalLayout1.addWidget(self.btn_more_info1)
            self.verticalLayout1.addLayout(self.horizontalLayout1)
            self.gridLayout1.addLayout(self.verticalLayout1, 0, 0, 1, 1)
            self.verticalLayout_2.addWidget(self.frame1)

            self.all_accs_buttons.append([self.btn_more_info1, self.title1])

            self.title1.setText(acc_object._title)
            self.desription1.setText(acc_object._description)
            self.balancecurrency1.setText(f'{acc_object._balance} {acc_object._currency_short}')
            self.btn_more_info1.setText("...")

        elif acc_object._type == 'Накопительный':
            self.frame2 = QtWidgets.QFrame(self.frame_panel_savings)
            self.frame2.setEnabled(True)
            self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame2.setObjectName("frame2")
            self.gridLayout2 = QtWidgets.QGridLayout(self.frame2)
            self.gridLayout2.setContentsMargins(0, 0, 0, -1)
            self.gridLayout2.setObjectName("gridLayout2")
            self.verticalLayout2 = QtWidgets.QVBoxLayout()
            self.verticalLayout2.setObjectName("verticalLayout2")
            self.horizontalLayout2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout2.setObjectName("horizontalLayout2")
            self.title2 = QtWidgets.QLabel(self.frame2)
            self.title2.setObjectName("title2")
            self.horizontalLayout2.addWidget(self.title2)
            self.desription2 = QtWidgets.QLabel(self.frame2)
            self.desription2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.desription2.setObjectName("desription2")
            self.horizontalLayout2.addWidget(self.desription2)
            self.verticalLayout2.addLayout(self.horizontalLayout2)
            self.horizontalLayout2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout2.setObjectName("horizontalLayout2")
            self.balancecurrency2 = QtWidgets.QLabel(self.frame2)
            self.balancecurrency2.setObjectName("balancecurrency2")
            self.horizontalLayout2.addWidget(self.balancecurrency2)
            self.btn_more_info2 = QtWidgets.QToolButton(self.frame2)
            self.btn_more_info2.setObjectName("btn_more_info2")
            self.horizontalLayout2.addWidget(self.btn_more_info2)
            self.verticalLayout2.addLayout(self.horizontalLayout2)
            self.gridLayout2.addLayout(self.verticalLayout2, 0, 0, 1, 1)
            self.verticalLayout.addWidget(self.frame2)

            self.all_accs_buttons.append([self.btn_more_info2, self.title2])

            self.title2.setText(acc_object._title)
            self.desription2.setText(acc_object._description)
            self.balancecurrency2.setText(f'{acc_object._balance} {acc_object._currency_short}')
            self.btn_more_info2.setText("...")

        print(self.all_accs_buttons)

    def add_last_acc(self):
        """Метод для создания и последующей прорисовки объекта-счёта"""
        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            acc = json.load(file)['accounts'][-1]
            acc_obj = Ui_Form(acc['title'], acc['type'], acc['currency_full'], acc['currency_short'],
                              acc['description'], acc['balance'], acc['add_to_all_balance'])
            self.add_new_account(acc_obj)

    def add_all_accs_to_gui(self):
        """Метод для прорисовки всех имеющихся счетов"""
        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)

        for acc in accounts_data['accounts']:
            acc_obj = Ui_Form(acc['title'], acc['type'], acc['currency_full'], acc['currency_short'],
                              acc['description'], acc['balance'], acc['add_to_all_balance'])
            self.add_new_account(acc_obj)

    def refresh_balances(self):
        """Метод для обновления балансов на главном окне"""
        all_balance = all_accs_balance = all_savings_balance = 0

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accs = json.load(file)['accounts']

        if len(accs) > 0:
            for acc in accs:
                if acc['type'] == 'Обычный':
                    all_accs_balance += acc['balance']
                elif acc['type'] == 'Накопительный':
                    all_savings_balance += acc['balance']

                if acc['add_to_all_balance']:
                    all_balance += acc['balance']
        if all_accs_balance == 0:
            self.all_accs_balance.setText('0 ₽')
        else:
            self.all_accs_balance.setText(f'{round(all_balance, 2)} ₽')

        if all_savings_balance == 0:
            self.all_savings_balance.setText('0 ₽')
        else:
            self.all_savings_balance.setText(f'{round(all_savings_balance, 2)} ₽')

        if all_balance == 0:
            self.all_accounts_balance.setText('0 ₽')
        else:
            self.all_accounts_balance.setText(f'{round(all_balance, 2)} ₽')

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
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_categories),
                                      _translate("MainWindow", "Категории"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_operations),
                                      _translate("MainWindow", "Операции"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_overview), _translate("MainWindow", "Обзор"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
