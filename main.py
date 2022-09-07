import sys
from PyQt5 import QtWidgets
from main_window import UiMainWindow

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

sys.exit(app.exec_())
