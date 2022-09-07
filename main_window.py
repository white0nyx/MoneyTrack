# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from acc_object import Ui_Form
from menu_crt_new_acc import Ui_menu_create_account
from menu_edit_acc import UiMenuEditAccount
from menu_settings import Ui_SettingsMenu
from operation_object import Ui_frame_operation


class UiMainWindow(object):

    def __init__(self, user_interface):
        user_interface.setObjectName("MainWindow")
        user_interface.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        user_interface.setWindowIcon(icon)
        user_interface.setWindowOpacity(1.0)
        self.layout_main_window = QtWidgets.QWidget(user_interface)
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
        self.frame_panel_acs = QtWidgets.QFrame(self.tab_accounts)
        self.frame_panel_acs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_panel_acs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panel_acs.setObjectName("frame_panel_acs")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_panel_acs)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_panel_acs = QtWidgets.QLabel(self.frame_panel_acs)
        self.name_panel_acs.setObjectName("name_panel_acs")
        self.horizontalLayout_3.addWidget(self.name_panel_acs)
        self.all_acs_balance = QtWidgets.QLabel(self.frame_panel_acs)
        self.all_acs_balance.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.all_acs_balance.setObjectName("all_acs_balance")
        self.horizontalLayout_3.addWidget(self.all_acs_balance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_panel_acs)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 812, 191))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_13.addWidget(self.frame)
        spacer_item0 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacer_item0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.frame_panel_acs)
        self.frame_panel_savings = QtWidgets.QFrame(self.tab_accounts)
        self.frame_panel_savings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_panel_savings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panel_savings.setObjectName("frame_panel_savings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_panel_savings)
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
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_panel_savings)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 812, 190))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14.addWidget(self.frame_2)
        spacer_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacer_item1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout_3.addWidget(self.frame_panel_savings)
        self.tab_main_menu.addTab(self.tab_accounts, "")
        self.tab_categories = QtWidgets.QWidget()
        self.tab_categories.setObjectName("tab_categories")
        self.tab_main_menu.addTab(self.tab_categories, "")
        self.tab_operations = QtWidgets.QWidget()
        self.tab_operations.setObjectName("tab_operations")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_operations)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.h_layout_top_panel_2 = QtWidgets.QHBoxLayout()
        self.h_layout_top_panel_2.setObjectName("h_layout_top_panel_2")
        self.btn_settings_3 = QtWidgets.QToolButton(self.tab_operations)
        self.btn_settings_3.setObjectName("btn_settings_3")
        self.h_layout_top_panel_2.addWidget(self.btn_settings_3)
        self.all_accounts_balance_3 = QtWidgets.QLabel(self.tab_operations)
        self.all_accounts_balance_3.setAlignment(QtCore.Qt.AlignCenter)
        self.all_accounts_balance_3.setObjectName("all_accounts_balance_3")
        self.h_layout_top_panel_2.addWidget(self.all_accounts_balance_3)
        self.btn_search_operation = QtWidgets.QToolButton(self.tab_operations)
        self.btn_search_operation.setObjectName("btn_search_operation")
        self.h_layout_top_panel_2.addWidget(self.btn_search_operation)
        self.verticalLayout_4.addLayout(self.h_layout_top_panel_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item2)
        self.btn_date = QtWidgets.QToolButton(self.tab_operations)
        self.btn_date.setObjectName("btn_date")
        self.horizontalLayout_2.addWidget(self.btn_date)
        spacer_item3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.scroll_area_operations = QtWidgets.QScrollArea(self.tab_operations)
        self.scroll_area_operations.setWidgetResizable(True)
        self.scroll_area_operations.setObjectName("scroll_area_operations")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 832, 415))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_operations = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_operations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_operations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_operations.setObjectName("frame_operations")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_operations)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5.addWidget(self.frame_operations)
        spacer_item4 = QtWidgets.QSpacerItem(20, 345, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacer_item4)
        self.scroll_area_operations.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scroll_area_operations)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacer_item5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item5)
        self.btn_add_operation = QtWidgets.QToolButton(self.tab_operations)
        self.btn_add_operation.setObjectName("btn_add_operation")
        self.horizontalLayout.addWidget(self.btn_add_operation)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tab_main_menu.addTab(self.tab_operations, "")
        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.tab_main_menu.addTab(self.tab_overview, "")
        self.gridLayout.addWidget(self.tab_main_menu, 0, 0, 1, 1)
        user_interface.setCentralWidget(self.layout_main_window)

        self.set_all_text(user_interface)
        self.tab_main_menu.setCurrentIndex(0)

        self.all_acs_buttons = []
        self.frames_acs = []

        self.add_accounts_to_gui()
        self.update_balances()
        self.add_functions_to_buttons()

        self.btn_crt_new_acc.clicked.connect(self.open_crt_new_acc_menu)
        self.btn_settings.clicked.connect(self.open_settings_menu)

        self.btn_add_operation.clicked.connect(self.draw_new_operation)

        QtCore.QMetaObject.connectSlotsByName(user_interface)

    def setupUi(self, user_interface):
        """Метод для прорисовки основного окна"""

    def open_crt_new_acc_menu(self):
        menu_create_account = QtWidgets.QDialog()
        window_crt_new_acc = Ui_menu_create_account(self)
        window_crt_new_acc.setupUi(menu_create_account)
        menu_create_account.show()

    def open_edit_acc_menu(self, account_btn):
        """Открытие меню редактирования счёта"""
        menu_edit_account = QtWidgets.QDialog()
        UiMenuEditAccount(self, account_btn, menu_edit_account)
        menu_edit_account.show()

    @staticmethod
    def open_settings_menu():
        """Открытие меню настроек"""
        settings_menu = QtWidgets.QMainWindow()
        settings_ui = Ui_SettingsMenu()
        settings_ui.setupUi(settings_menu)
        settings_menu.show()

    def add_new_account(self, acc_object):
        """Прорисовка счета на главном окне
        и связывание кнопки счетов с необходимыми функциями"""
        global ui
        if acc_object['type'] == 'Обычный':
            account_object = QtWidgets.QWidget()
            ui = Ui_Form(acc_object)
            ui.setupUi(account_object)
            self.verticalLayout_16.addWidget(account_object)

        elif acc_object['type'] == 'Накопительный':
            account_object = QtWidgets.QWidget()
            ui = Ui_Form(acc_object)
            ui.setupUi(account_object)
            self.verticalLayout_15.addWidget(account_object)

        self.all_acs_buttons.append({'btn_acc': ui.btn_more_info, 'title': acc_object['title']})
        self.frames_acs.append(ui.frame)
        self.link_buttons_to_frames()

    def add_accounts_to_gui(self, only_last=False):
        """Метод для прорисовки всех имеющихся счетов"""
        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts_data = json.load(file)['accounts']

        if only_last:
            accounts_data = (accounts_data[-1],)

        for account in accounts_data:
            if not account['hide']:
                self.add_new_account(account)

    def update_balances(self):
        """Метод для обновления балансов на главном окне"""
        all_balance = all_accounts_balance = all_savings_balance = 0

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            all_accounts = json.load(file)['accounts']

        for account in all_accounts:
            if account['type'] == 'Обычный':
                all_accounts_balance += account['balance']
            elif account['type'] == 'Накопительный':
                all_savings_balance += account['balance']

            if account['add_to_all_balance']:
                all_balance += account['balance']

        self.all_acs_balance.setText(f'{self.remove_extra_zeros(round(all_accounts_balance, 2))} ₽')
        self.all_savings_balance.setText(f'{self.remove_extra_zeros(round(all_savings_balance, 2))} ₽')
        self.all_accounts_balance.setText(f'{self.remove_extra_zeros(round(all_balance, 2))} ₽')

    def update_accounts_gui(self):
        """Перепрорисовка всех счетов на главном экране"""
        for account_frame in self.frames_acs:
            account_frame.deleteLater()
        self.frames_acs = []
        self.all_acs_buttons = []
        self.add_accounts_to_gui()

    @staticmethod
    def remove_extra_zeros(number):
        """Удаление незначащих нулей из баланса"""
        return int(number) if int(number) - number == 0.0 else number

    def add_functions_to_buttons(self, only_last=False):
        """Присвоение кнопке/кнопкам функций"""

        with open('app_data/all_accounts.json', 'r', encoding='utf-8') as file:
            accounts = json.load(file)['accounts']

        if only_last:
            accounts = (accounts[-1],)

        for btn_data in self.all_acs_buttons:
            for acc in accounts:
                if btn_data['title'] == acc['title']:
                    btn_data.update({'acc_data': acc})

        for button in self.all_acs_buttons:
            button['btn_acc'].released.connect(
                lambda btn=button: self.open_edit_acc_menu(btn))

    def link_buttons_to_frames(self):
        """Установка связи между кнопками и соответствующими им счетами"""
        for i in range(len(self.frames_acs)):
            self.all_acs_buttons[i]['frame'] = self.frames_acs[i]

    def draw_new_operation(self):
        """Прорисовка новой операции"""
        frame_operation = QtWidgets.QFrame(self.scroll_area_operations)
        frame_operation_ui = Ui_frame_operation()
        frame_operation_ui.setupUi(frame_operation)
        self.verticalLayout_7.addWidget(frame_operation)

    def set_all_text(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MoneyTrack"))
        self.btn_settings.setText(_translate("MainWindow", "S"))
        self.all_accounts_balance.setText(_translate("MainWindow", "0"))
        self.btn_crt_new_acc.setText(_translate("MainWindow", "+"))
        self.name_panel_acs.setText(_translate("MainWindow", "СЧЕТА"))
        self.all_acs_balance.setText(_translate("MainWindow", "0"))
        self.name_panel_savings.setText(_translate("MainWindow", "СБЕРЕЖЕНИЯ"))
        self.all_savings_balance.setText(_translate("MainWindow", "0"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_accounts), _translate("MainWindow", "Счета"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_categories),
                                      _translate("MainWindow", "Категории"))
        self.btn_settings_3.setText(_translate("MainWindow", "S"))
        self.all_accounts_balance_3.setText(_translate("MainWindow", "0"))
        self.btn_search_operation.setText(_translate("MainWindow", "S"))
        self.btn_date.setText(_translate("MainWindow", "Date"))
        self.btn_add_operation.setText(_translate("MainWindow", "+"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_operations),
                                      _translate("MainWindow", "Операции"))
        self.tab_main_menu.setTabText(self.tab_main_menu.indexOf(self.tab_overview), _translate("MainWindow", "Обзор"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
