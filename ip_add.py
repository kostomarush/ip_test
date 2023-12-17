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


    def add_checked_checkboxes_to_textedit(self):
        
        checked_items = [checkbox.text() for checkbox in self.findChildren(QtWidgets.QCheckBox) if checkbox.isChecked()]

        if len(checked_items) > 2:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget, "Предупреждение", "Выберите не более 2 чекбоксов.")
            return
        # Получаем текст из отмеченных чекбоксов и добавляем в QTextEdit
        if checked_items:
            new_add = {1: f'{checked_items[0]}',
                       2: f'{checked_items[1]}'}
            self.items.append(new_add)
            self.ui.textEdit.clear()
            for item in self.items:
                for key, value in item.items():
                    self.ui.textEdit.insertPlainText( f"{value}; ")
        else:
            self.ui.textEdit.append("Нет отмеченных чекбоксов")
            
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.read_and_shuffle()
    w.show()
    sys.exit(app.exec_())
