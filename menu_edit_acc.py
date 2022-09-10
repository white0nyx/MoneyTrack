# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import json

from PyQt5.QtWidgets import QMessageBox


class UiMenuEditAccount(object):

    def __init__(self, parent_window, account_btn, edit_account_menu=None):
        """Инициализация окна для редактирования счёта"""
        self.parent_window = parent_window
        self.menu_edit_account = edit_account_menu
        edit_account_menu.setObjectName("menu_edit_account")
        edit_account_menu.setEnabled(True)
        edit_account_menu.resize(450, 280)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        edit_account_menu.setFont(font)
        edit_account_menu.setToolTip("")
        edit_account_menu.setStatusTip("")
        edit_account_menu.setAccessibleName("")
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_account_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_title_account = QtWidgets.QLabel(edit_account_menu)
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
        self.label_title = QtWidgets.QLabel(edit_account_menu)
        self.label_title.setObjectName("label_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.line_title = QtWidgets.QLineEdit(edit_account_menu)
        self.line_title.setObjectName("line_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_title)
        self.label_type = QtWidgets.QLabel(edit_account_menu)
        self.label_type.setObjectName("label_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.type_selection = QtWidgets.QComboBox(edit_account_menu)
        self.type_selection.setObjectName("type_selection")
        self.type_selection.addItem("")
        self.type_selection.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.type_selection)
        self.label_currency = QtWidgets.QLabel(edit_account_menu)
        self.label_currency.setObjectName("label_currency")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_currency)
        self.currency_selection = QtWidgets.QComboBox(edit_account_menu)
        self.currency_selection.setObjectName("currency_selection")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.currency_selection.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currency_selection)
        self.label_description = QtWidgets.QLabel(edit_account_menu)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_description)
        self.line_description = QtWidgets.QLineEdit(edit_account_menu)
        self.line_description.setObjectName("line_description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_description)
        self.verticalLayout.addLayout(self.formLayout)
        spacer_item0 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item0)
        self.main_title_balance = QtWidgets.QLabel(edit_account_menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_balance.setFont(font)
        self.main_title_balance.setObjectName("main_title_balance")
        self.verticalLayout.addWidget(self.main_title_balance)
        self.remains = QtWidgets.QFormLayout()
        self.remains.setObjectName("remains")
        self.remains_layout = QtWidgets.QLabel(edit_account_menu)
        self.remains_layout.setObjectName("remains_layout")
        self.remains.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.remains_layout)
        self.remains_line = QtWidgets.QLineEdit(edit_account_menu)
        self.remains_line.setObjectName("remains_line")
        self.remains.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.remains_line)
        self.verticalLayout.addLayout(self.remains)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.check_add_in_all_balance = QtWidgets.QLabel(edit_account_menu)
        self.check_add_in_all_balance.setObjectName("check_add_in_all_balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_add_in_all_balance)
        self.r_btn_check_in_all_balance = QtWidgets.QCheckBox(edit_account_menu)
        self.r_btn_check_in_all_balance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_btn_check_in_all_balance.setText("")
        self.r_btn_check_in_all_balance.setObjectName("r_btn_check_in_all_balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.r_btn_check_in_all_balance)
        self.hide_acc = QtWidgets.QLabel(edit_account_menu)
        self.hide_acc.setObjectName("hide_acc")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hide_acc)
        self.r_btn_check_hide_acc = QtWidgets.QCheckBox(edit_account_menu)
        self.r_btn_check_hide_acc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_btn_check_hide_acc.setText("")
        self.r_btn_check_hide_acc.setObjectName("r_btn_check_hide_acc")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.r_btn_check_hide_acc)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacer_item1 = QtWidgets.QSpacerItem(17, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item1)
        self.h_layout_for_buttons = QtWidgets.QHBoxLayout()
        self.h_layout_for_buttons.setObjectName("h_layout_for_buttons")
        self.btn_delete = QtWidgets.QPushButton(edit_account_menu)
        self.btn_delete.setFlat(False)
        self.btn_delete.setObjectName("btn_delete")
        self.h_layout_for_buttons.addWidget(self.btn_delete)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_layout_for_buttons.addItem(spacer_item2)
        self.btn_accept = QtWidgets.QPushButton(edit_account_menu)
        self.btn_accept.setDefault(True)
        self.btn_accept.setObjectName("btn_add")
        self.h_layout_for_buttons.addWidget(self.btn_accept)
        self.btn_cancel = QtWidgets.QPushButton(edit_account_menu)
        self.btn_cancel.setObjectName("btn_cancel")
        self.h_layout_for_buttons.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.h_layout_for_buttons)

        self.account_btn = account_btn
        self.account_data = account_btn['acc_data']
        self.account_index = self.parent_window.all_acs_buttons.index(account_btn)
        self.account_frame = self.parent_window.all_acs_buttons[self.account_index]['frame']

        title = self.account_data['title']  # Отсюда начинается заполнение полей данными
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

        self.set_all_text(edit_account_menu)
        QtCore.QMetaObject.connectSlotsByName(edit_account_menu)

    def add_functions_to_buttons(self):
        """Добавление функций кнопкам"""
        self.btn_cancel.clicked.connect(lambda: self.menu_edit_account.close())
        self.btn_delete.clicked.connect(lambda: self.deletion_request())
        self.btn_accept.clicked.connect(lambda: self.accept_changes())

    def delete_account_data(self):
        """Удаление данных о счёте"""
        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)

        accounts = accounts_data['accounts']
        accounts.remove(self.account_data)
        accounts_data['accounts'] = accounts

        with open('app_data/all_accounts.json', 'w', encoding='utf-8') as file:
            json.dump(accounts_data, file, indent=4, ensure_ascii=False)

        self.account_frame.deleteLater()
        self.parent_window.frames_acs.remove(self.account_frame)
        del self.parent_window.all_acs_buttons[self.account_index]

    def deletion_request(self):
        """Окно для подтверждение удаления"""
        delete_ask = QMessageBox()
        delete_ask.setWindowTitle('Подтверждение удаления')
        delete_ask.setText(f'Вы уверены, что хотите удалить счёт {self.account_data["title"]}?')
        delete_ask.setIcon(QMessageBox.Warning)
        delete_ask.setInformativeText('Все связанные с ним операции удалятся.\nРекомендуется выбрать "Скрыть счёт".')
        delete_ask.addButton('Отмена', QMessageBox.AcceptRole)
        delete_ask.addButton('Удалить', QMessageBox.RejectRole)
        delete_ask.buttonClicked.connect(self.full_delete_account)
        delete_ask.exec_()

    def full_delete_account(self, btn):
        """Полное удаление счёта"""
        if btn.text() == 'Удалить':
            self.delete_account_data()
            self.menu_edit_account.close()
            self.parent_window.update_balances()

    def accept_changes(self):
        """Сохранение новых данных счёта"""
        self.delete_account_data()

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)
        accounts = accounts_data['accounts']
        accounts.insert(
            self.account_index,
            {
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

    def set_all_text(self, edit_account_menu):
        """Установка всего текста"""
        _translate = QtCore.QCoreApplication.translate
        edit_account_menu.setWindowTitle(_translate("menu_edit_account", "Редактирование счёта"))
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
