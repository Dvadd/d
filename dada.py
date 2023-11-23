#! python -m PyQt5.uic.pyuic -x untitled.ui -0 ui.py
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from random import choice
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generet.clicked.connect(self.exemple)
    def exemple(self):
        print(1)
        
    def generate(self):
            self.(password_len):
            alphabet:"DIAOSJDILAOSDJAISODJMASLKsndjklhdasoiuhdasiohdasuigdasyiugdsailkndsakjlhbdsaujk"
            numbers: "12231232131321"
            symbols: '!@#$%^&*\\'
            password = ''
            for i in range(password_len):
                if self.ui.cb_numbers.is_enabled():
                    digit = choice(numbers)
                    password += digit
                if self.ui.cb_aphavit.is_enabled():
                    leter = choice(alphabet)
                    password += leter
                symbol = choice(symbols)
                password += symbols
            int(password)                
                    
                    
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
