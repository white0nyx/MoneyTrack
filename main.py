import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import UiMainWindow
from menu_crt_new_acc import Ui_menu_create_account

import os.path
import json

if not os.path.exists('app_data/all_accounts.json'):
    with open('app_data/all_accounts.json', 'w', encoding='utf-8') as file:
        json.dump({
            'accounts': [],
            }, file, indent=4, ensure_ascii=False)

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow(MainWindow)
ui.setupUi(MainWindow)
MainWindow.show()


def openWindowCrtNewAcc():
    global menu_create_account
    menu_create_account = QtWidgets.QDialog()
    window_crt_new_acc = Ui_menu_create_account(ui)
    window_crt_new_acc.setupUi(menu_create_account)
    menu_create_account.show()


ui.btn_crt_new_acc.clicked.connect(openWindowCrtNewAcc)

sys.exit(app.exec_())
