# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_menu_crt_new_acc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import json


class Ui_menu_create_account(object):

    def __init__(self, parent_window):
        """Сохранение главного окна для взаимодействия с ним через окно для создания нового счёта"""
        self.parent_window = parent_window

    def setupUi(self, menu_create_account):
        """Прорисовка окна для создания нового счёта"""
        self.menu_create_account = menu_create_account
        menu_create_account.setObjectName("menu_create_account")
        menu_create_account.setEnabled(True)
        menu_create_account.resize(424, 264)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        menu_create_account.setFont(font)
        menu_create_account.setToolTip("")
        menu_create_account.setStatusTip("")
        menu_create_account.setAccessibleName("")
        self.verticalLayout = QtWidgets.QVBoxLayout(menu_create_account)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_title_account = QtWidgets.QLabel(menu_create_account)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menu_title_account.setFont(font)
        self.menu_title_account.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.menu_title_account.setObjectName("menu_title_account")
        self.verticalLayout.addWidget(self.menu_title_account)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_title = QtWidgets.QLabel(menu_create_account)
        self.label_title.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.line_title = QtWidgets.QLineEdit(menu_create_account)
        self.line_title.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_title)
        self.label_type = QtWidgets.QLabel(menu_create_account)
        self.label_type.setObjectName("label_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.type_selection = QtWidgets.QComboBox(menu_create_account)
        self.type_selection.setObjectName("type_selection")
        self.type_selection.addItem("")
        self.type_selection.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_selection)
        self.label_currency = QtWidgets.QLabel(menu_create_account)
        self.label_currency.setObjectName("label_currency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_currency)
        self.currency_selection = QtWidgets.QComboBox(menu_create_account)
        self.currency_selection.setObjectName("currency_selection")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currency_selection)
        self.label_description = QtWidgets.QLabel(menu_create_account)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_description)
        self.line_description = QtWidgets.QLineEdit(menu_create_account)
        self.line_description.setObjectName("line_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_description)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.layout_balance = QtWidgets.QVBoxLayout()
        self.layout_balance.setObjectName("layout_balance")
        self.main_title_balance = QtWidgets.QLabel(menu_create_account)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_balance.setFont(font)
        self.main_title_balance.setObjectName("main_title_balance")
        self.layout_balance.addWidget(self.main_title_balance)
        self.remains_and_all_balance = QtWidgets.QVBoxLayout()
        self.remains_and_all_balance.setObjectName("remains_and_all_balance")
        self.remains = QtWidgets.QFormLayout()
        self.remains.setObjectName("remains")
        self.remains_layout = QtWidgets.QLabel(menu_create_account)
        self.remains_layout.setObjectName("remains_layout")
        self.remains.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.remains_layout)
        self.line_balance = QtWidgets.QLineEdit(menu_create_account)
        self.line_balance.setObjectName("remains_line")
        self.remains.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_balance)
        self.remains_and_all_balance.addLayout(self.remains)
        self.add_in_all_balance_menu = QtWidgets.QHBoxLayout()
        self.add_in_all_balance_menu.setObjectName("add_in_all_balance_menu")
        self.check_add_in_all_balance = QtWidgets.QLabel(menu_create_account)
        self.check_add_in_all_balance.setObjectName("check_add_in_all_balance")
        self.add_in_all_balance_menu.addWidget(self.check_add_in_all_balance)
        self.r_btn_check_in_all_balance = QtWidgets.QCheckBox(menu_create_account)
        self.r_btn_check_in_all_balance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_btn_check_in_all_balance.setText("")
        self.r_btn_check_in_all_balance.setObjectName("r_btn_check_in_all_balance")
        self.add_in_all_balance_menu.addWidget(self.r_btn_check_in_all_balance)
        self.remains_and_all_balance.addLayout(self.add_in_all_balance_menu)
        self.layout_balance.addLayout(self.remains_and_all_balance)
        self.verticalLayout.addLayout(self.layout_balance)
        spacerItem1 = QtWidgets.QSpacerItem(17, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.h_layout_for_buttons = QtWidgets.QHBoxLayout()
        self.h_layout_for_buttons.setObjectName("h_layout_for_buttons")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_for_buttons.addItem(spacerItem2)
        self.btn_add = QtWidgets.QPushButton(menu_create_account)
        self.btn_add.setObjectName("btn_add")
        self.h_layout_for_buttons.addWidget(self.btn_add)
        self.btn_cancel = QtWidgets.QPushButton(menu_create_account)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_layout_for_buttons.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.h_layout_for_buttons)

        self.retranslateUi(menu_create_account)
        QtCore.QMetaObject.connectSlotsByName(menu_create_account)

        self.btn_cancel.clicked.connect(lambda: menu_create_account.close())
        self.btn_add.clicked.connect(lambda: self.get_data_acc())

    def get_data_acc(self):
        """Получение данных из полей и сохранение их в файл app_data/all_accounts.json"""
        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)

        accounts_data['accounts'].append(
            {
                'id': accounts_data['new_id'],
                'title': self.line_title.text(),
                'type': self.type_selection.currentText(),
                'currency_full': self.currency_selection.currentText(),
                'currency_index': self.currency_selection.currentIndex(),
                'currency_short': self.currency_selection.currentText().split()[-1],
                'description': self.line_description.text(),
                'balance': float(self.line_balance.text()),
                'add_to_all_balance': self.r_btn_check_in_all_balance.isChecked(),
                'hide': False

            }
        )

        accounts_data['new_id'] += 1

        with open('app_data/all_accounts.json', 'w', encoding='utf-8') as file:
            json.dump(accounts_data, file, indent=4, ensure_ascii=False)

        self.parent_window.add_accounts_to_gui(only_last=True)
        self.parent_window.update_balances()
        self.parent_window.add_functions_to_buttons(only_last=True)
        self.parent_window.update_accounts_gui()
        self.parent_window.add_functions_to_buttons()
        self.parent_window.update_balances()

        self.menu_create_account.close()

    def retranslateUi(self, menu_create_account):
        _translate = QtCore.QCoreApplication.translate
        menu_create_account.setWindowTitle(_translate("menu_create_account", "Новый счёт"))
        self.menu_title_account.setText(_translate("menu_create_account", "Счёт"))
        self.label_title.setText(_translate("menu_create_account", "Название"))
        self.label_type.setText(_translate("menu_create_account", "Тип"))
        self.type_selection.setItemText(0, _translate("menu_create_account", "Обычный"))
        self.type_selection.setItemText(1, _translate("menu_create_account", "Накопительный"))
        self.label_currency.setText(_translate("menu_create_account", "Валюта счёта"))
        self.currency_selection.setItemText(0, _translate("menu_create_account", "Российский рубль ₽"))
        self.currency_selection.setItemText(1, _translate("menu_create_account", "Доллар США $"))
        self.currency_selection.setItemText(2, _translate("menu_create_account", "Евро €"))
        self.label_description.setText(_translate("menu_create_account", "Описание"))
        self.main_title_balance.setText(_translate("menu_create_account", "Баланс"))
        self.remains_layout.setText(_translate("menu_create_account", "Остаток на счёте"))
        self.check_add_in_all_balance.setText(_translate("menu_create_account", "Учитывать в общем балансе"))
        self.btn_add.setText(_translate("menu_create_account", "Добавить"))
        self.btn_cancel.setText(_translate("menu_create_account", "Отменить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menu_create_account = QtWidgets.QDialog()
    ui = Ui_menu_create_account()
    ui.setupUi(menu_create_account)
    menu_create_account.show()
    sys.exit(app.exec_())
