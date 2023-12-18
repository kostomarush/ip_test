import ipaddress
import json
from random import shuffle, choice
import json
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from graph import Ui_MainWindow
from info import Ui_Form


app1 = QtWidgets.QApplication(sys.argv)
app1.setWindowIcon(QtGui.QIcon('icon.ico'))

class Information(QtWidgets.QMainWindow):
    def __init__(self):
        super(Information, self).__init__()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self)
        

class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_checked_checkboxes_to_textedit)
        self.ui.pushButton_2.clicked.connect(self.result)
        self.ui.pushButton_3.clicked.connect(self.clear)
        self.ui.action.triggered.connect(self.read_and_shuffle)
        self.ui.action_2.triggered.connect(self.open_info)
        self.count = 0
        
    def read_and_shuffle(self):
        filename = "./generated_ip_pairs.json"
        enter_add = []
        
        with open(filename, 'r') as file:
            data = json.load(file)

        ip_pairs_list = choice(data["ip_pairs"])
        shuffle(ip_pairs_list)
        for item in ip_pairs_list:
            enter_add.append(item["ip1"])
            enter_add.append(item["ip2"])
        shuffle(enter_add)
        self.items = []


        self.ui.checkBox_3.setText(f'{enter_add[0]}')
        self.ui.checkBox_4.setText(f'{enter_add[1]}')
        self.ui.checkBox_7.setText(f'{enter_add[2]}')
        self.ui.checkBox.setText(f'{enter_add[3]}')
        self.ui.checkBox_2.setText(f'{enter_add[4]}')
        self.ui.checkBox_8.setText(f'{enter_add[5]}')
        self.ui.checkBox_9.setText(f'{enter_add[6]}')
        self.ui.checkBox_10.setText(f'{enter_add[7]}')
        self.ui.checkBox_5.setText(f'{enter_add[8]}')
        self.ui.checkBox_6.setText(f'{enter_add[9]}')

    def are_networks_in_same_subnet(self, network1, network2):
        network1 = ipaddress.IPv4Network(network1, strict=False)
        network2 = ipaddress.IPv4Network(network2, strict=False)

        return network1.overlaps(network2)

    def add_checked_checkboxes_to_textedit(self):
        
        checked_items = [checkbox.text() for checkbox in self.findChildren(QtWidgets.QCheckBox) if checkbox.isEnabled() and checkbox.isChecked()]
        
        if len(checked_items) > 2 or len(checked_items) < 2:
            QtWidgets.QMessageBox.critical(self.ui.centralwidget, "Ошибка", "Выберите два чекбокса.")
            return
        
        [checkbox.setDisabled(True) for checkbox in self.findChildren(QtWidgets.QCheckBox) if checkbox.isChecked()]
        
        if checked_items:
            if self.are_networks_in_same_subnet(checked_items[0], checked_items[1]):
                self.count += 1
        
        all_checkboxes_disabled = all(not checkbox.isEnabled() for checkbox in self.findChildren(QtWidgets.QCheckBox))
        
        if all_checkboxes_disabled:


            self.ui.pushButton_2.setEnabled(True)

        self.ui.statusbar.showMessage(f'Значение добавлено')
        
    
    def result(self):
        QtWidgets.QMessageBox.information(self.ui.centralwidget, "Результат", f"Ваша оценка {self.count}")
        QtCore.QCoreApplication.quit()
    
    def clear(self):
        self.count = 0
        for checkbox in self.findChildren(QtWidgets.QCheckBox):
            checkbox.setEnabled(True)
            checkbox.setChecked(False)

        self.ui.statusbar.showMessage(f'Все значения удалены')
        
    def open_info(self):
        self.second_window = Information()
        self.second_window.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Mywindow()
    w.read_and_shuffle()
    w.show()
    sys.exit(app.exec_())
