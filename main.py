import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainWindow
from menu_crt_new_acc import Ui_menu_create_account

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openWindowCrtNewAcc():
    global menu_create_account
    menu_create_account = QtWidgets.QDialog()
    window_crt_new_acc = Ui_menu_create_account()
    window_crt_new_acc.setupUi(menu_create_account)
    menu_create_account.show()




ui.btn_crt_new_acc.clicked.connect(openWindowCrtNewAcc)

sys.exit(app.exec_())
