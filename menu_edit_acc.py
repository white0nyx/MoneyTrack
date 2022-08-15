# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_menu_edit_acc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_menu_edit_account(object):

    def __init__(self, parent_window):
        self.parent_window = parent_window

    def setupUi(self, menu_edit_account):
        self.menu_edit_account = menu_edit_account
        menu_edit_account.setObjectName("menu_edit_account")
        menu_edit_account.setEnabled(True)
        menu_edit_account.resize(450, 280)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        menu_edit_account.setFont(font)
        menu_edit_account.setToolTip("")
        menu_edit_account.setStatusTip("")
        menu_edit_account.setAccessibleName("")
        self.verticalLayout = QtWidgets.QVBoxLayout(menu_edit_account)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_title_account = QtWidgets.QLabel(menu_edit_account)
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
        self.label_title = QtWidgets.QLabel(menu_edit_account)
        self.label_title.setObjectName("label_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.line_title = QtWidgets.QLineEdit(menu_edit_account)
        self.line_title.setObjectName("line_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_title)
        self.label_type = QtWidgets.QLabel(menu_edit_account)
        self.label_type.setObjectName("label_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.type_selection = QtWidgets.QComboBox(menu_edit_account)
        self.type_selection.setObjectName("type_selection")
        self.type_selection.addItem("")
        self.type_selection.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_selection)
        self.label_currency = QtWidgets.QLabel(menu_edit_account)
        self.label_currency.setObjectName("label_currency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_currency)
        self.currency_selection = QtWidgets.QComboBox(menu_edit_account)
        self.currency_selection.setObjectName("currency_selection")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currency_selection)
        self.label_description = QtWidgets.QLabel(menu_edit_account)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_description)
        self.line_description = QtWidgets.QLineEdit(menu_edit_account)
        self.line_description.setObjectName("line_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_description)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.main_title_balance = QtWidgets.QLabel(menu_edit_account)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_balance.setFont(font)
        self.main_title_balance.setObjectName("main_title_balance")
        self.verticalLayout.addWidget(self.main_title_balance)
        self.remains = QtWidgets.QFormLayout()
        self.remains.setObjectName("remains")
        self.remains_layout = QtWidgets.QLabel(menu_edit_account)
        self.remains_layout.setObjectName("remains_layout")
        self.remains.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.remains_layout)
        self.remains_line = QtWidgets.QLineEdit(menu_edit_account)
        self.remains_line.setObjectName("remains_line")
        self.remains.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.remains_line)
        self.verticalLayout.addLayout(self.remains)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.check_add_in_all_balance = QtWidgets.QLabel(menu_edit_account)
        self.check_add_in_all_balance.setObjectName("check_add_in_all_balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_add_in_all_balance)
        self.r_btn_check_in_all_balance = QtWidgets.QCheckBox(menu_edit_account)
        self.r_btn_check_in_all_balance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_btn_check_in_all_balance.setText("")
        self.r_btn_check_in_all_balance.setObjectName("r_btn_check_in_all_balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.r_btn_check_in_all_balance)
        self.hide_acc = QtWidgets.QLabel(menu_edit_account)
        self.hide_acc.setObjectName("hide_acc")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hide_acc)
        self.r_btn_check_hide_acc = QtWidgets.QCheckBox(menu_edit_account)
        self.r_btn_check_hide_acc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_btn_check_hide_acc.setText("")
        self.r_btn_check_hide_acc.setObjectName("r_btn_check_hide_acc")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.r_btn_check_hide_acc)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(17, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.h_layout_for_buttons = QtWidgets.QHBoxLayout()
        self.h_layout_for_buttons.setObjectName("h_layout_for_buttons")
        self.btn_delete = QtWidgets.QPushButton(menu_edit_account)
        self.btn_delete.setFlat(False)
        self.btn_delete.setObjectName("btn_delete")
        self.h_layout_for_buttons.addWidget(self.btn_delete)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_for_buttons.addItem(spacerItem2)
        self.btn_accept = QtWidgets.QPushButton(menu_edit_account)
        self.btn_accept.setDefault(True)
        self.btn_accept.setObjectName("btn_add")
        self.h_layout_for_buttons.addWidget(self.btn_accept)
        self.btn_cancel = QtWidgets.QPushButton(menu_edit_account)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_layout_for_buttons.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.h_layout_for_buttons)

        self.retranslateUi(menu_edit_account)
        QtCore.QMetaObject.connectSlotsByName(menu_edit_account)

    def fill_in_with_data(self, account_btn):
        self.account_btn = account_btn
        self.account_data = account_btn['acc_data']
        self.account_index = self.parent_window.all_accs_buttons.index(account_btn)
        self.acccout_frame = self.parent_window.all_accs_buttons[self.account_index]['frame']

        title = self.account_data['title']
        type_ = self.account_data['type']
        currency_index = self.account_data['currency_index']
        description = self.account_data['description']
        balance = self.account_data['balance']
        add_to_all_balance = self.account_data['add_to_all_balance']
        hide = self.account_data['hide']

        self.line_title.setText(title)

        type_index = 0
        if type_ == 'Обычный':
            type_index = 0
        elif type_ == 'Накопительный':
            type_index = 1

        self.type_selection.setCurrentIndex(type_index)
        self.currency_selection.setCurrentIndex(currency_index)
        self.line_description.setText(description)
        self.remains_line.setText(str(balance))
        self.r_btn_check_in_all_balance.setChecked(add_to_all_balance)
        self.r_btn_check_hide_acc.setChecked(hide)
        self.add_functions_to_buttons()

    def add_functions_to_buttons(self):
        self.btn_cancel.clicked.connect(lambda: self.menu_edit_account.close())
        self.btn_delete.clicked.connect(lambda: self.delete_acc_with_ask())
        self.btn_accept.clicked.connect(lambda: self.accept_changes())

    def delete_acc(self):

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)
        self.btn_delete.deleteLater()

        accounts = accounts_data['accounts']
        accounts.remove(self.account_data)
        accounts_data['accounts'] = accounts

        with open('app_data/all_accounts.json', 'w', encoding='utf-8') as file:
            json.dump(accounts_data, file, indent=4, ensure_ascii=False)

        self.acccout_frame.deleteLater()
        self.parent_window.frames_accs.remove(self.acccout_frame)
        del self.parent_window.all_accs_buttons[self.account_index]

    def delete_acc_with_ask(self):
        # Позже здесь будет реализован функционал диалогового окна для удаления счёта
        self.delete_acc()
        self.menu_edit_account.close()
        self.parent_window.update_balances()

    def accept_changes(self):
        self.delete_acc()

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)
        accounts = accounts_data['accounts']
        accounts.insert(
            self.account_index,
            {
                'id': accounts_data['new_id'],
                'title': self.line_title.text(),
                'type': self.type_selection.currentText(),
                'currency_full': self.currency_selection.currentText(),
                'currency_index': self.currency_selection.currentIndex(),
                'currency_short': self.currency_selection.currentText().split()[-1],
                'description': self.line_description.text(),
                'balance': float(self.remains_line.text()),
                'add_to_all_balance': self.r_btn_check_in_all_balance.isChecked(),
                'hide': self.r_btn_check_hide_acc.isChecked()
            }
        )

        with open('app_data/all_accounts.json', 'w', encoding='utf-8') as file:
            json.dump(accounts_data, file, indent=4, ensure_ascii=False)

        self.parent_window.update_accounts_gui()
        self.parent_window.add_functions_to_buttons()
        self.parent_window.update_balances()
        self.menu_edit_account.close()

    def retranslateUi(self, menu_edit_account):
        _translate = QtCore.QCoreApplication.translate
        menu_edit_account.setWindowTitle(_translate("menu_edit_account", "Редактирование счёта"))
        self.menu_title_account.setText(_translate("menu_edit_account", "Счёт"))
        self.label_title.setText(_translate("menu_edit_account", "Название"))
        self.label_type.setText(_translate("menu_edit_account", "Тип"))
        self.type_selection.setItemText(0, _translate("menu_edit_account", "Обычный"))
        self.type_selection.setItemText(1, _translate("menu_edit_account", "Накопительный"))
        self.label_currency.setText(_translate("menu_edit_account", "Валюта счёта"))
        self.currency_selection.setItemText(0, _translate("menu_edit_account", "Российский рубль ₽"))
        self.currency_selection.setItemText(1, _translate("menu_edit_account", "Доллар США $"))
        self.currency_selection.setItemText(2, _translate("menu_edit_account", "Евро €"))
        self.label_description.setText(_translate("menu_edit_account", "Описание"))
        self.main_title_balance.setText(_translate("menu_edit_account", "Баланс"))
        self.remains_layout.setText(_translate("menu_edit_account", "Остаток на счёте"))
        self.check_add_in_all_balance.setText(_translate("menu_edit_account", "Учитывать в общем балансе"))
        self.hide_acc.setText(_translate("menu_edit_account", "Скрыть счёт"))
        self.btn_delete.setText(_translate("menu_edit_account", "Удалить счёт"))
        self.btn_accept.setText(_translate("menu_edit_account", "Применить"))
        self.btn_cancel.setText(_translate("menu_edit_account", "Отменить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menu_edit_account = QtWidgets.QDialog()
    ui = Ui_menu_edit_account()
    ui.setupUi(menu_edit_account)
    menu_edit_account.show()
    sys.exit(app.exec_())
