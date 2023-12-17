import ipaddress
import json
from random import shuffle, choice
import json
import sys
from PyQt5 import QtWidgets, QtGui
from graph import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_checked_checkboxes_to_textedit)
        self.ui.pushButton_2.clicked.connect(self.result)
        self.count = 0
        
    def read_and_shuffle(self):
        filename = "./generated_ip_pairs.json"
        enter_add = []
        
        with open(filename, 'r') as file:
            data = json.load(file)

        ip_pairs_list = choice(data["ip_pairs"])
        shuffle(ip_pairs_list)
        print(json.dumps(ip_pairs_list, indent=2))
        for item in ip_pairs_list:
            enter_add.append(item["ip1"])
            enter_add.append(item["ip2"])
        shuffle(enter_add)
        print(enter_add)
        self.items = []
        # Перемешиваем все IP-адреса
        #Вывод всех IP-адресов в случайном порядке
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
        
        [checkbox.setDisabled(True) for checkbox in self.findChildren(QtWidgets.QCheckBox) if checkbox.isChecked()]
        
        checked_items = [checkbox.text() for checkbox in self.findChildren(QtWidgets.QCheckBox) if checkbox.isChecked()]
        

        # Получаем текст из отмеченных чекбоксов и добавляем в QTextEdit
        if checked_items:
            if self.are_networks_in_same_subnet(checked_items[0], checked_items[1]):
                self.count += 1
            else:
                pass

    
    def result(self):
        QtWidgets.QMessageBox.information(self.ui.centralwidget, "Результат", f"Ваша оценка {self.count}")
        return
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.read_and_shuffle()
    w.show()
    sys.exit(app.exec_())
