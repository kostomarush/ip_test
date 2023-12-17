import ipaddress
import random
import sys
from PyQt5 import QtWidgets, QtGui
from graph import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def generate_ip_addresses(self):
        # Генерация случайной базовой сети
        base_network = ipaddress.IPv4Network(f'{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0/24', strict=False)

        # Список различных масок подсетей
        subnet_masks = [24, 25, 26, 27, 28]

        # Выбираем случайные 5 подсетей с разными масками
        selected_subnets = random.sample(subnet_masks, 5)

        # Создаем список для хранения всех IP-адресов
        all_ip_addresses = []

        # Генерация IP-адресов и добавление их в список
        for subnet_mask in selected_subnets:
            subnet = f'{base_network.network_address}/{subnet_mask}'
            subnet_obj = ipaddress.IPv4Network(subnet, strict=False)

            for _ in range(2):
                random_ip = ipaddress.IPv4Address(random.randint(int(subnet_obj.network_address), int(subnet_obj.broadcast_address)))
                all_ip_addresses.append(str(random_ip))

        # Перемешиваем все IP-адреса
        random.shuffle(all_ip_addresses)

        # Вывод всех IP-адресов в случайном порядке
        self.ui.checkBox_3.setText(f'{all_ip_addresses[0]}')
        self.ui.checkBox_4.setText(f'{all_ip_addresses[1]}')
        self.ui.checkBox_7.setText(f'{all_ip_addresses[2]}')
        self.ui.checkBox.setText(f'{all_ip_addresses[3]}')
        self.ui.checkBox_2.setText(f'{all_ip_addresses[4]}')
        self.ui.checkBox_8.setText(f'{all_ip_addresses[5]}')
        self.ui.checkBox_9.setText(f'{all_ip_addresses[6]}')
        self.ui.checkBox_10.setText(f'{all_ip_addresses[7]}')
        
        for i in all_ip_addresses:
            print(i)

            
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.generate_ip_addresses()
    w.show()
    sys.exit(app.exec_())
